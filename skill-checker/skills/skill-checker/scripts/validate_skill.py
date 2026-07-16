#!/usr/bin/env python3
"""Dependency-free structural validator for a Claude Code skill directory."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import unquote


KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK = re.compile(r"!?\[[^]]*]\(([^)]+)\)")
KNOWN_FIELDS = {
    "name",
    "description",
    "argument-hint",
    "disable-model-invocation",
    "user-invocable",
    "allowed-tools",
    "model",
    "context",
    "agent",
    "hooks",
    "license",
    "compatibility",
    "metadata",
}


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    path: str
    message: str


class Report:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.findings: list[Finding] = []

    def add(self, severity: str, code: str, path: Path, message: str) -> None:
        try:
            label = path.resolve().relative_to(self.root.parent.resolve()).as_posix()
        except ValueError:
            label = str(path)
        self.findings.append(Finding(severity, code, label, message))

    def error(self, code: str, path: Path, message: str) -> None:
        self.add("error", code, path, message)

    def warn(self, code: str, path: Path, message: str) -> None:
        self.add("warning", code, path, message)

    @property
    def errors(self) -> list[Finding]:
        return [item for item in self.findings if item.severity == "error"]


def parse_frontmatter(path: Path, report: Report) -> tuple[dict[str, str], str] | None:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        report.error("unreadable", path, f"cannot read UTF-8 text: {exc}")
        return None
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        report.error("frontmatter-opening", path, "line 1 must be the opening --- delimiter")
        return None
    try:
        closing = next(index for index, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        report.error("frontmatter-closing", path, "missing closing --- delimiter")
        return None

    fields: dict[str, str] = {}
    folded_key: str | None = None
    for number, line in enumerate(lines[1:closing], 2):
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$", line)
        if match:
            key, value = match.group(1), match.group(2).strip()
            if key in fields:
                report.error("duplicate-field", path, f"frontmatter field '{key}' is duplicated at line {number}")
            folded_key = key if value in {">", ">-", "|", "|-"} else None
            if folded_key:
                value = ""
            elif len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
                value = value[1:-1]
            fields[key] = value
        elif folded_key and line.startswith((" ", "\t")):
            if line.strip():
                fields[folded_key] = f"{fields[folded_key]} {line.strip()}".strip()
        elif line.strip() and not line.lstrip().startswith("#") and not line.startswith((" ", "\t")):
            report.error("frontmatter-syntax", path, f"cannot parse frontmatter line {number}")
    return fields, "\n".join(lines[closing + 1 :])


def normalize_target(raw: str) -> str | None:
    value = raw.strip()
    if value.startswith("<") and ">" in value:
        value = value[1:value.index(">")]
    else:
        value = value.split(maxsplit=1)[0]
    if not value or value.startswith(("#", "http://", "https://", "mailto:")):
        return None
    return unquote(value.split("#", 1)[0].split("?", 1)[0]) or None


def check_links(path: Path, report: Report) -> None:
    try:
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return
    for raw in LINK.findall(content):
        target = normalize_target(raw)
        if target is None:
            continue
        candidate = (path.parent / target).resolve()
        try:
            candidate.relative_to(report.root.resolve())
        except ValueError:
            report.warn("link-outside-skill", path, f"local link points outside the skill directory: {raw}")
            continue
        if not candidate.exists():
            report.error("broken-link", path, f"local link does not resolve: {raw}")


def check_structure(root: Path, report: Report) -> Path | None:
    if not root.exists():
        report.error("missing-path", root, "skill path does not exist")
        return None
    if not root.is_dir():
        report.error("not-directory", root, "expected a skill directory or SKILL.md")
        return None
    if not KEBAB.fullmatch(root.name):
        report.error("folder-name", root, "skill directory must use lowercase kebab-case")
    skill = root / "SKILL.md"
    if not skill.is_file():
        alternatives = [path.name for path in root.iterdir() if path.name.lower() == "skill.md"]
        detail = f"; found {', '.join(alternatives)}" if alternatives else ""
        report.error("missing-skill", root, f"SKILL.md is required with exact case{detail}")
        return None
    for directory in ("scripts", "references", "assets"):
        candidate = root / directory
        if candidate.exists() and not candidate.is_dir():
            report.error("resource-type", candidate, f"{directory} must be a directory")
    return skill


def check_manifest(skill: Path, report: Report) -> None:
    parsed = parse_frontmatter(skill, report)
    if parsed is None:
        return
    fields, body = parsed
    name = fields.get("name", "")
    description = fields.get("description", "").strip()
    if not name:
        report.error("missing-name", skill, "frontmatter requires a name")
    elif not KEBAB.fullmatch(name):
        report.error("invalid-name", skill, "name must use lowercase kebab-case")
    elif name != report.root.name:
        report.error("name-mismatch", skill, f"name '{name}' must match folder '{report.root.name}'")
    if not description:
        report.error("missing-description", skill, "frontmatter requires a description")
    elif len(description) > 1024:
        report.error("description-length", skill, f"description is {len(description)} characters; maximum is 1024")
    elif not any(term in description.lower() for term in ("use when", "use for", "use this", "trigger", "invoke")):
        report.warn("description-trigger", skill, "description may not clearly say when the skill applies")
    for field in sorted(set(fields) - KNOWN_FIELDS):
        report.warn("unknown-frontmatter", skill, f"verify target runtime support for frontmatter field '{field}'")

    total_lines = len(skill.read_text(encoding="utf-8").splitlines())
    if total_lines > 500:
        report.warn("body-length", skill, f"SKILL.md has {total_lines} lines; consider progressive disclosure")
    if re.search(r"^## When to (?:Use|use)\s*$", body, re.MULTILINE):
        report.warn("duplicate-trigger-section", skill, "invocation criteria are usually more effective in the description")
    check_links(skill, report)


def check_resources(root: Path, report: Report) -> None:
    references = root / "references"
    if references.is_dir():
        for path in references.rglob("*.md"):
            check_links(path, report)
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
            first = "\n".join(lines[:120]).lower()
            if len(lines) > 500 and "## contents" not in first and "table of contents" not in first:
                report.warn("reference-navigation", path, f"long reference has {len(lines)} lines without a contents section")


def check_scripts(root: Path, report: Report) -> None:
    scripts = root / "scripts"
    if not scripts.is_dir():
        return
    for path in scripts.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix == ".py":
            try:
                compile(path.read_text(encoding="utf-8"), str(path), "exec")
            except (OSError, UnicodeDecodeError, SyntaxError) as exc:
                report.error("script-syntax", path, str(exc))
            continue
        elif path.suffix in {".sh", ".bash"}:
            command = ["bash", "-n", str(path)]
        else:
            continue
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        if result.returncode:
            report.error("script-syntax", path, (result.stderr or result.stdout).strip())


def output(report: Report, as_json: bool) -> int:
    ordered = sorted(report.findings, key=lambda item: (item.severity != "error", item.path, item.code))
    if as_json:
        payload = {
            "skill": str(report.root),
            "valid": not report.errors,
            "errors": len(report.errors),
            "warnings": len(ordered) - len(report.errors),
            "findings": [asdict(item) for item in ordered],
        }
        print(json.dumps(payload, indent=2))
    else:
        for item in ordered:
            print(f"{item.severity.upper()}: {item.path}: {item.code}: {item.message}")
        print(
            f"Validated {report.root.name}: {len(report.errors)} error(s), "
            f"{len(ordered) - len(report.errors)} warning(s)."
        )
    return 1 if report.errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="skill directory or SKILL.md")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument("--check-scripts", action="store_true", help="compile Python and syntax-check shell scripts")
    args = parser.parse_args()

    root = args.path.parent if args.path.name == "SKILL.md" else args.path
    root = root.resolve()
    report = Report(root)
    skill = check_structure(root, report)
    if skill is not None:
        check_manifest(skill, report)
        check_resources(root, report)
        if args.check_scripts:
            check_scripts(root, report)
    return output(report, args.json)


if __name__ == "__main__":
    raise SystemExit(main())
