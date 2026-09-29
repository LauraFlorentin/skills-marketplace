#!/usr/bin/env bash
# Detect repeated edits and ask for confirmation without changing Git state.

set -u

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$PWD}"
CONFIG="$PROJECT_DIR/.harness/config.json"
[ -f "$CONFIG" ] || exit 0

STATE_DIR="$PROJECT_DIR/.harness/state"
COUNT_FILE="$STATE_DIR/edit-counts.json"
CONFIG_THRESHOLDS=$(python3 - "$CONFIG" <<'PY'
import json
import sys

try:
    config = json.load(open(sys.argv[1], encoding="utf-8"))
except (OSError, ValueError):
    config = {}
settings = config.get("circuit_breaker", {})
print(settings.get("soft_threshold", 5))
print(settings.get("confirmation_threshold", settings.get("hard_threshold", 10)))
PY
)
CONFIG_SOFT=$(printf '%s\n' "$CONFIG_THRESHOLDS" | sed -n '1p')
CONFIG_HARD=$(printf '%s\n' "$CONFIG_THRESHOLDS" | sed -n '2p')
SOFT_THRESHOLD="${HARNESS_SOFT_THRESHOLD:-$CONFIG_SOFT}"
HARD_THRESHOLD="${HARNESS_HARD_THRESHOLD:-$CONFIG_HARD}"
case "$SOFT_THRESHOLD" in
  ''|*[!0-9]*) SOFT_THRESHOLD=5 ;;
esac
case "$HARD_THRESHOLD" in
  ''|*[!0-9]*) HARD_THRESHOLD=10 ;;
esac
[ "$SOFT_THRESHOLD" -ge 1 ] || SOFT_THRESHOLD=1
[ "$HARD_THRESHOLD" -gt "$SOFT_THRESHOLD" ] || HARD_THRESHOLD=$((SOFT_THRESHOLD + 1))
mkdir -p "$STATE_DIR"

INPUT=$(cat)
FILE_PATH=$(printf '%s' "$INPUT" | python3 -c '
import json
import sys

try:
    payload = json.load(sys.stdin)
except (TypeError, ValueError):
    print("")
    raise SystemExit(0)

tool_input = payload.get("tool_input", {})
print(tool_input.get("file_path") or tool_input.get("path") or "")
' 2>/dev/null)

[ -n "$FILE_PATH" ] || exit 0

COUNT=$(python3 - "$COUNT_FILE" "$FILE_PATH" <<'PY'
import json
import sys
from pathlib import Path

count_path = Path(sys.argv[1])
file_path = sys.argv[2]
try:
    counts = json.loads(count_path.read_text(encoding="utf-8"))
except (OSError, ValueError):
    counts = {}
counts[file_path] = int(counts.get(file_path, 0)) + 1
count_path.write_text(json.dumps(counts, indent=2) + "\n", encoding="utf-8")
print(counts[file_path])
PY
)

if [ "$COUNT" -ge "$HARD_THRESHOLD" ]; then
  python3 - "$FILE_PATH" "$COUNT" <<'PY'
import json
import sys

path, count = sys.argv[1], int(sys.argv[2])
json.dump(
    {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": (
                f"Harness checkpoint: {path} has been edited {count} times in this "
                "session. Confirm the next edit after reviewing the task, diff, and "
                "a different hypothesis. No files or Git state were changed by the hook."
            ),
            "additionalContext": (
                "Repeated edits are a heuristic, not proof of failure. Review the "
                "original requirement and current diff before continuing."
            ),
        }
    },
    sys.stdout,
)
PY
elif [ "$COUNT" -eq "$SOFT_THRESHOLD" ]; then
  python3 - "$FILE_PATH" "$COUNT" <<'PY'
import json
import sys

path, count = sys.argv[1], int(sys.argv[2])
json.dump(
    {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "additionalContext": (
                f"Harness checkpoint: {path} has been edited {count} times. "
                "Before another edit, compare the current diff with the original "
                "requirement and state the new hypothesis."
            ),
        }
    },
    sys.stdout,
)
PY
fi

exit 0
