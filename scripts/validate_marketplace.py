#!/usr/bin/env python3
"""Validate this marketplace without third-party dependencies."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE_PATH = ROOT / ".claude-plugin" / "marketplace.json"
PACKAGE_PATH = ROOT / "package.json"
KEBAB_CASE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.plugins = 0
        self.skills = 0
        self.commands = 0
        self.agents = 0

    def error(self, path: Path | str, message: str) -> None:
        self.errors.append(f"{relative(path)}: {message}")

    def warn(self, path: Path | str, message: str) -> None:
        self.warnings.append(f"{relative(path)}: {message}")


def relative(path: Path | str) -> str:
    value = Path(path)
    try:
        return value.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def load_json(path: Path, report: Report) -> object | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        report.error(path, f"invalid JSON: {exc}")
        return None


def parse_frontmatter(path: Path, report: Report) -> tuple[dict[str, str], str] | None:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        report.error(path, f"cannot read UTF-8 text: {exc}")
        return None

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        report.error(path, "missing opening YAML frontmatter delimiter")
        return None

    try:
        closing = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        report.error(path, "missing closing YAML frontmatter delimiter")
        return None

    fields: dict[str, str] = {}
    folded_key: str | None = None
    for line in lines[1:closing]:
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$", line)
        if match:
            value = match.group(2).strip()
            folded_key = match.group(1) if value in {">", ">-", "|", "|-"} else None
            if folded_key:
                value = ""
            if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
                value = value[1:-1]
            fields[match.group(1)] = value
        elif folded_key and line.startswith((" ", "\t")) and line.strip():
            fields[folded_key] = f"{fields[folded_key]} {line.strip()}".strip()
    return fields, "\n".join(lines[closing + 1 :])


def validate_links(path: Path, report: Report) -> None:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return

    for raw_target in LINK.findall(text):
        target = raw_target.strip().strip("<>").split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        candidate = (path.parent / unquote(target)).resolve()
        if not candidate.exists():
            report.error(path, f"broken local link: {raw_target}")


def validate_skill(path: Path, report: Report) -> None:
    parsed = parse_frontmatter(path, report)
    if parsed is None:
        return
    fields, body = parsed
    folder_name = path.parent.name
    name = fields.get("name", "")
    description = fields.get("description", "")

    if not KEBAB_CASE.fullmatch(folder_name):
        report.error(path.parent, "skill directory must use lowercase kebab-case")
    if name != folder_name:
        report.error(path, f"frontmatter name '{name}' must match directory '{folder_name}'")
    if not description:
        report.error(path, "frontmatter description is required")
    elif len(description) > 1024:
        report.error(path, "description exceeds the cross-platform 1,024-character limit")
    elif not any(term in description.lower() for term in ("use when", "use this", "use for", "trigger", "invoke")):
        report.warn(path, "description should say when the skill is relevant")

    line_count = len(path.read_text(encoding="utf-8").splitlines())
    if line_count > 500:
        report.error(path, f"SKILL.md has {line_count} lines; move detail to references/ (max 500)")
    if re.search(r"^## When to (?:Use|use)\s*$", body, re.MULTILINE):
        report.warn(path, "move invocation criteria into the frontmatter description")
    validate_links(path, report)


def validate_agent(path: Path, report: Report) -> None:
    parsed = parse_frontmatter(path, report)
    if parsed is None:
        return
    fields, _ = parsed
    if not fields.get("name"):
        report.error(path, "agent frontmatter requires name")
    if not fields.get("description"):
        report.error(path, "agent frontmatter requires description")
    validate_links(path, report)


def validate_plugin(plugin_dir: Path, entry: dict[str, object], report: Report) -> None:
    manifest_path = plugin_dir / ".claude-plugin" / "plugin.json"
    manifest = load_json(manifest_path, report)
    if not isinstance(manifest, dict):
        return

    name = plugin_dir.name
    if manifest.get("name") != name:
        report.error(manifest_path, f"manifest name must be '{name}'")
    version = manifest.get("version")
    if version is not None and (not isinstance(version, str) or not SEMVER.fullmatch(version)):
        report.error(manifest_path, "version must use semantic versioning")
    entry_version = entry.get("version")
    if entry_version is not None and entry_version != version:
        report.error(manifest_path, f"version conflicts with marketplace entry '{entry_version}'")

    if entry.get("source") != f"./{name}":
        report.error(MARKETPLACE_PATH, f"source for '{name}' must be './{name}'")
    for field in ("displayName", "description", "author", "repository", "homepage", "license"):
        if not manifest.get(field):
            report.error(manifest_path, f"manifest requires '{field}' repository metadata")
    if manifest.get("$schema") != "https://json.schemastore.org/claude-code-plugin-manifest.json":
        report.warn(manifest_path, "use the Claude Code plugin manifest schema for editor validation")
    if not entry.get("description"):
        report.error(MARKETPLACE_PATH, f"catalog entry '{name}' requires a description")

    for skill_path in sorted((plugin_dir / "skills").glob("*/SKILL.md")):
        report.skills += 1
        validate_skill(skill_path, report)

    commands_dir = plugin_dir / "commands"
    if commands_dir.is_dir():
        for command_path in sorted(commands_dir.glob("*.md")):
            if command_path.name == "README.md":
                continue
            report.commands += 1
            parsed = parse_frontmatter(command_path, report)
            if parsed is not None and not parsed[0].get("description"):
                report.error(command_path, "command frontmatter requires description")
            validate_links(command_path, report)

    agents_dir = plugin_dir / "agents"
    if agents_dir.is_dir():
        for agent_path in sorted(agents_dir.glob("*.md")):
            if agent_path.name == "README.md":
                continue
            report.agents += 1
            validate_agent(agent_path, report)

    hooks_dir = plugin_dir / "hooks"
    hook_scripts = [] if not hooks_dir.is_dir() else [
        path for path in hooks_dir.iterdir() if path.suffix in {".py", ".sh", ".js"}
    ]
    if hook_scripts and not (hooks_dir / "hooks.json").is_file():
        report.error(hooks_dir, "hook scripts require a hooks/hooks.json configuration")
    if (hooks_dir / "settings.json").exists():
        report.error(hooks_dir / "settings.json", "plugin hooks must use hooks/hooks.json")

    for markdown in plugin_dir.rglob("*.md"):
        if ".git" not in markdown.parts:
            validate_links(markdown, report)
            if "references" in markdown.parts and len(markdown.read_text(encoding="utf-8").splitlines()) > 500:
                first_lines = "\n".join(markdown.read_text(encoding="utf-8").splitlines()[:120]).lower()
                if "table of contents" not in first_lines and "## contents" not in first_lines:
                    report.warn(markdown, "long reference should include a table of contents")

    for path in plugin_dir.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".py", ".sh", ".json"}:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for forbidden in ("/mnt/skills/", "/mnt/user-data/", "hooks/settings.json"):
            if forbidden in content:
                report.error(path, f"contains non-portable or obsolete path: {forbidden}")
        if path.parent == commands_dir and "../skills/" in content:
            report.error(path, "command must use ${CLAUDE_PLUGIN_ROOT} for bundled skill paths")

    mutation_patterns = re.compile(
        r"\bgit\s+(?:add|commit|stash|reset|checkout|clean)\b|"
        r"\bfind\b[^\n]*\s-delete\b"
    )
    safety_paths = list(hooks_dir.glob("*")) if hooks_dir.is_dir() else []
    installer = plugin_dir / "install.sh"
    if installer.exists():
        safety_paths.append(installer)
    for path in safety_paths:
        if not path.is_file() or path.suffix not in {".py", ".sh", ".js", ".json"}:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        if mutation_patterns.search(content):
            report.error(path, "hook or installer must not mutate Git state automatically")


def validate_repository_metadata(marketplace: dict[str, object], report: Report) -> None:
    package = load_json(PACKAGE_PATH, report)
    if not isinstance(package, dict):
        return
    metadata = marketplace.get("metadata")
    marketplace_version = metadata.get("version") if isinstance(metadata, dict) else None
    package_version = package.get("version")
    if not isinstance(marketplace_version, str) or not SEMVER.fullmatch(marketplace_version):
        report.error(MARKETPLACE_PATH, "metadata.version must use semantic versioning")
    if package_version != marketplace_version:
        report.error(PACKAGE_PATH, "version must match marketplace metadata.version")
    if package.get("private") is not True:
        report.warn(PACKAGE_PATH, "set private=true to prevent accidental npm publication")
    scripts = package.get("scripts")
    if not isinstance(scripts, dict) or scripts.get("validate") != "python3 scripts/validate_marketplace.py":
        report.warn(PACKAGE_PATH, "provide the standard repository validation script")


def tracked_artifacts(report: Report) -> None:
    try:
        result = subprocess.run(
            ["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True
        )
    except (OSError, subprocess.CalledProcessError):
        report.warn(ROOT, "could not inspect tracked files with git")
        return

    banned_names = {".DS_Store", "settings.local.json"}
    for raw in result.stdout.split(b"\0"):
        if not raw:
            continue
        path = Path(raw.decode("utf-8"))
        if path.name in banned_names or path.suffix.lower() in {".zip", ".tar", ".gz"}:
            report.error(path, "generated or local-only artifact must not be tracked")


def validate_python_syntax(report: Report) -> None:
    for path in ROOT.rglob("*.py"):
        if ".git" in path.parts:
            continue
        try:
            source = path.read_text(encoding="utf-8")
            compile(source, str(path), "exec")
        except (OSError, UnicodeDecodeError, SyntaxError) as exc:
            report.error(path, f"invalid Python syntax: {exc}")


def main() -> int:
    report = Report()
    marketplace = load_json(MARKETPLACE_PATH, report)
    if not isinstance(marketplace, dict):
        return finish(report)

    entries = marketplace.get("plugins")
    if not isinstance(entries, list):
        report.error(MARKETPLACE_PATH, "plugins must be an array")
        return finish(report)
    validate_repository_metadata(marketplace, report)

    entry_map: dict[str, dict[str, object]] = {}
    for entry in entries:
        if not isinstance(entry, dict) or not isinstance(entry.get("name"), str):
            report.error(MARKETPLACE_PATH, "every plugin entry requires a string name")
            continue
        name = entry["name"]
        if name in entry_map:
            report.error(MARKETPLACE_PATH, f"duplicate plugin entry: {name}")
        entry_map[name] = entry

    plugin_dirs = sorted(
        path for path in ROOT.iterdir()
        if path.is_dir() and (path / ".claude-plugin" / "plugin.json").is_file()
    )
    directory_names = {path.name for path in plugin_dirs}
    catalog_names = set(entry_map)
    for missing in sorted(directory_names - catalog_names):
        report.error(MARKETPLACE_PATH, f"plugin directory missing from catalog: {missing}")
    for missing in sorted(catalog_names - directory_names):
        report.error(MARKETPLACE_PATH, f"catalog source has no plugin directory: {missing}")

    for plugin_dir in plugin_dirs:
        report.plugins += 1
        validate_plugin(plugin_dir, entry_map.get(plugin_dir.name, {}), report)

    for json_path in ROOT.rglob("*.json"):
        if ".git" not in json_path.parts:
            load_json(json_path, report)
    validate_python_syntax(report)
    tracked_artifacts(report)
    return finish(report)


def finish(report: Report) -> int:
    for warning in sorted(set(report.warnings)):
        print(f"WARNING: {warning}")
    for error in sorted(set(report.errors)):
        print(f"ERROR: {error}", file=sys.stderr)

    print(
        f"Validated {report.plugins} plugins, {report.skills} skills, "
        f"{report.commands} commands, and {report.agents} agents: "
        f"{len(set(report.errors))} error(s), {len(set(report.warnings))} warning(s)."
    )
    return 1 if report.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
