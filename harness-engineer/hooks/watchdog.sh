#!/usr/bin/env bash
# Periodically report harness-state inconsistencies without modifying project files.

set -u

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$PWD}"
CONFIG="$PROJECT_DIR/.harness/config.json"
[ -f "$CONFIG" ] || exit 0

STATE_DIR="$PROJECT_DIR/.harness/state"
COUNT_FILE="$STATE_DIR/tool-call-count.txt"
CONFIG_WATCHDOG=$(python3 - "$CONFIG" <<'PY'
import json
import sys

try:
    config = json.load(open(sys.argv[1], encoding="utf-8"))
except (OSError, ValueError):
    config = {}
settings = config.get("watchdog", {})
print(settings.get("check_interval_tool_calls", 20))
print(settings.get("lock_stale_minutes", 30))
PY
)
CONFIG_INTERVAL=$(printf '%s\n' "$CONFIG_WATCHDOG" | sed -n '1p')
CONFIG_STALE=$(printf '%s\n' "$CONFIG_WATCHDOG" | sed -n '2p')
INTERVAL="${HARNESS_HEALTH_CHECK_INTERVAL:-$CONFIG_INTERVAL}"
LOCK_STALE_MINUTES="${HARNESS_LOCK_STALE_MINUTES:-$CONFIG_STALE}"
case "$INTERVAL" in
  ''|*[!0-9]*) INTERVAL=20 ;;
esac
case "$LOCK_STALE_MINUTES" in
  ''|*[!0-9]*) LOCK_STALE_MINUTES=30 ;;
esac
[ "$INTERVAL" -ge 1 ] || INTERVAL=1
mkdir -p "$STATE_DIR"

COUNT=$(cat "$COUNT_FILE" 2>/dev/null || printf '0')
case "$COUNT" in
  ''|*[!0-9]*) COUNT=0 ;;
esac
COUNT=$((COUNT + 1))
printf '%s\n' "$COUNT" > "$COUNT_FILE"
[ $((COUNT % INTERVAL)) -eq 0 ] || exit 0

python3 - "$PROJECT_DIR" "$LOCK_STALE_MINUTES" <<'PY'
import json
import sys
import time
from pathlib import Path

root = Path(sys.argv[1])
stale_seconds = int(sys.argv[2]) * 60
issues = []
features_path = root / "features.json"

if features_path.exists():
    try:
        data = json.loads(features_path.read_text(encoding="utf-8"))
        features = data if isinstance(data, list) else data.get("features", [])
        if not isinstance(features, list):
            raise TypeError("features must be an array")
        active = [item for item in features if isinstance(item, dict) and item.get("in_progress")]
        if len(active) > 1:
            issues.append(f"{len(active)} features are marked in progress")
    except (OSError, ValueError, TypeError) as exc:
        issues.append(f"features.json is invalid: {exc}")

locks = root / "current_tasks"
if locks.is_dir():
    now = time.time()
    stale = [
        path.name
        for path in locks.glob("*.txt")
        if path.is_file() and now - path.stat().st_mtime > stale_seconds
    ]
    if stale:
        issues.append(
            "stale task locks need human review: " + ", ".join(sorted(stale))
        )

if issues:
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": (
                    "Harness health warning: "
                    + "; ".join(issues)
                    + ". The watchdog did not edit or delete any files."
                ),
            }
        },
        sys.stdout,
    )
PY

exit 0
