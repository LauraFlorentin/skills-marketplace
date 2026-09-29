#!/usr/bin/env python3
"""Validate local Markdown links and optional features.json state."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd().resolve()
SKIP_DIRS = {".git", ".harness", "node_modules", "dist", "build", ".venv", "venv"}
LINK_RE = re.compile(r"!?\[[^]]*]\(([^)]+)\)")


def markdown_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        if not any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            files.append(path)
    return sorted(files)


def local_target(raw: str) -> str | None:
    target = raw.strip().split(maxsplit=1)[0].strip("<>")
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None
    target = unquote(target).split("#", 1)[0].split("?", 1)[0]
    return target or None


def check_links() -> list[str]:
    issues: list[str] = []
    for document in markdown_files():
        content = document.read_text(encoding="utf-8", errors="replace")
        for raw in LINK_RE.findall(content):
            target = local_target(raw)
            if target is None:
                continue
            candidate = (document.parent / target).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                issues.append(f"OUTSIDE_ROOT {document.relative_to(ROOT)} -> {target}")
                continue
            if not candidate.exists():
                issues.append(f"BROKEN_LINK {document.relative_to(ROOT)} -> {target}")
    return issues


def check_features() -> list[str]:
    path = ROOT / "features.json"
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return [f"INVALID_FEATURES_JSON {exc}"]
    features = data if isinstance(data, list) else data.get("features", [])
    if not isinstance(features, list):
        return ["INVALID_FEATURES features must be an array"]

    issues: list[str] = []
    seen: set[str] = set()
    for index, feature in enumerate(features):
        if not isinstance(feature, dict):
            issues.append(f"INVALID_FEATURE index {index} is not an object")
            continue
        feature_id = feature.get("id")
        if not feature_id:
            issues.append(f"MISSING_ID index {index}")
        elif feature_id in seen:
            issues.append(f"DUPLICATE_ID {feature_id}")
        else:
            seen.add(feature_id)
        if not feature.get("description"):
            issues.append(f"MISSING_DESCRIPTION {feature_id or index}")
        criteria = feature.get("acceptance_criteria", feature.get("steps"))
        if not isinstance(criteria, list) or not criteria:
            issues.append(f"MISSING_ACCEPTANCE_CRITERIA {feature_id or index}")
        status = feature.get("status")
        if status is not None and status not in {"planned", "in_progress", "blocked", "verified"}:
            issues.append(f"INVALID_STATUS {feature_id or index}: {status}")
        if feature.get("passes") and feature.get("in_progress"):
            issues.append(f"INCONSISTENT_STATE {feature_id or index}: passing and in progress")
        if feature.get("passes") and feature.get("circuit_broken"):
            issues.append(f"INCONSISTENT_STATE {feature_id or index}: passing and circuit broken")
    return issues


def main() -> int:
    issues = check_links() + check_features()
    if issues:
        print("Harness validation issues:")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Harness documentation and feature state are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
