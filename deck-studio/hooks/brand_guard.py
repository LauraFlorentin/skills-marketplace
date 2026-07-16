#!/usr/bin/env python3
"""Inject configured brand guidance before branded asset operations."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

# File types that should trigger brand enforcement
BRANDED_EXTENSIONS = {".pptx", ".docx", ".html", ".svg", ".png", ".pdf", ".htm"}
SAFE_LABELS = (
    "Brand Name",
    "Tagline",
    "Personality",
    "Primary",
    "Secondary",
    "Accent",
    "Background",
    "Text/Dark",
    "Heading Font",
    "Body Font",
    "Accent Font",
    "Logo description",
    "Logo placement",
    "Tone",
    "Key phrases/themes",
    "Avoid",
)


def find_config() -> Path | None:
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR")
    plugin_data = os.environ.get("CLAUDE_PLUGIN_DATA")
    candidates = []
    if project_dir:
        candidates.append(Path(project_dir) / ".brand-studio" / "brand-config.md")
    if plugin_data:
        candidates.append(Path(plugin_data) / "brand-config.md")
    return next((path for path in candidates if path.is_file()), None)


def safe_brand_summary(config_content: str) -> tuple[str, str]:
    values: dict[str, str] = {}
    for line in config_content.splitlines():
        if not line.startswith("- **") or ":**" not in line:
            continue
        label, value = line[4:].split(":**", 1)
        if label in SAFE_LABELS:
            values[label] = value.strip()[:160]
    brand_name = values.get("Brand Name") or "your brand"
    summary = "\n".join(f"- {label}: {values[label]}" for label in SAFE_LABELS if values.get(label))
    return brand_name, summary


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (TypeError, ValueError):
        return 0

    tool_params = json.dumps(payload.get("tool_input", {}), sort_keys=True).lower()
    has_branded_file = any(ext in tool_params.lower() for ext in BRANDED_EXTENSIONS)
    if not has_branded_file:
        return 0

    config_path = find_config()
    if config_path is None:
        return 0
    try:
        config_content = config_path.read_text(encoding="utf-8")
    except OSError:
        return 0

    if "STATUS: Not configured" in config_content:
        return 0

    brand_name, config_preview = safe_brand_summary(config_content)
    if not config_preview:
        return 0
    context = (
        f"[Brand Guard] Apply the configured {brand_name} identity to this branded asset.\n"
        f"Relevant brand settings:\n{config_preview}\n"
        "Match the configured colors, fonts, logo rules, and tone."
    )
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "additionalContext": context,
            }
        },
        sys.stdout,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
