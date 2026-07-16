#!/usr/bin/env bash
# Add concise project harness context at session start.

set -u

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$PWD}"
CONFIG="$PROJECT_DIR/.harness/config.json"
[ -f "$CONFIG" ] || exit 0

# Reset counters owned by this plugin at the beginning of each hook session.
rm -f "$PROJECT_DIR/.harness/state/edit-counts.json" \
  "$PROJECT_DIR/.harness/state/tool-call-count.txt" \
  "$PROJECT_DIR/.harness/state/checkpoint-band.txt"

python3 - "$CONFIG" "$PROJECT_DIR/features.json" <<'PY'
import json
import sys
from pathlib import Path

config_path = Path(sys.argv[1])
features_path = Path(sys.argv[2])
try:
    config = json.loads(config_path.read_text(encoding="utf-8"))
except (OSError, ValueError):
    config = {}

model = str(config.get("model", "unspecified"))
browser = bool(config.get("browser_automation", {}).get("enabled"))
summary = [
    f"[HARNESS] Active project harness; configured model profile: {model}.",
    "Read the project instructions and current task state before implementation.",
    "Verify behavior against explicit acceptance criteria before reporting completion.",
    "Treat commits, stashes, resets, deletions, and external writes as user-controlled actions.",
]
if features_path.exists():
    try:
        data = json.loads(features_path.read_text(encoding="utf-8"))
        features = data if isinstance(data, list) else data.get("features", [])
        if isinstance(features, list):
            passing = sum(
                1 for item in features
                if isinstance(item, dict) and item.get("passes") is True
            )
            summary.append(f"Feature status: {passing}/{len(features)} passing.")
    except (OSError, ValueError):
        summary.append("features.json exists but is not valid JSON.")
summary.append(
    "Browser verification is enabled."
    if browser
    else "Browser verification is not configured; use the safest available verification method."
)
print("\n".join(summary))
PY

exit 0
