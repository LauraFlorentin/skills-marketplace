#!/usr/bin/env bash
# Remind the agent about a long-lived dirty worktree without stashing or committing.

set -u

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$PWD}"
CONFIG="$PROJECT_DIR/.harness/config.json"
[ -f "$CONFIG" ] || exit 0
git -C "$PROJECT_DIR" rev-parse --git-dir >/dev/null 2>&1 || exit 0

STATE_DIR="$PROJECT_DIR/.harness/state"
DIRTY_SINCE="$STATE_DIR/dirty-since.txt"
LAST_BAND="$STATE_DIR/checkpoint-band.txt"
CONFIG_TIMEOUTS=$(python3 - "$CONFIG" <<'PY'
import json
import sys

try:
    config = json.load(open(sys.argv[1], encoding="utf-8"))
except (OSError, ValueError):
    config = {}
settings = config.get("checkpoint_reminder", config.get("dead_mans_switch", {}))
print(settings.get("warning_minutes", 30))
print(settings.get("critical_minutes", 60))
PY
)
CONFIG_WARNING=$(printf '%s\n' "$CONFIG_TIMEOUTS" | sed -n '1p')
CONFIG_CRITICAL=$(printf '%s\n' "$CONFIG_TIMEOUTS" | sed -n '2p')
WARNING_MINUTES="${HARNESS_COMMIT_TIMEOUT:-$CONFIG_WARNING}"
CRITICAL_MINUTES="${HARNESS_CRITICAL_TIMEOUT:-$CONFIG_CRITICAL}"
case "$WARNING_MINUTES" in
  ''|*[!0-9]*) WARNING_MINUTES=30 ;;
esac
case "$CRITICAL_MINUTES" in
  ''|*[!0-9]*) CRITICAL_MINUTES=60 ;;
esac
[ "$CRITICAL_MINUTES" -ge "$WARNING_MINUTES" ] || CRITICAL_MINUTES="$WARNING_MINUTES"
mkdir -p "$STATE_DIR"

DIRTY=$(git -C "$PROJECT_DIR" status --porcelain 2>/dev/null)
if [ -z "$DIRTY" ]; then
  rm -f "$DIRTY_SINCE" "$LAST_BAND"
  exit 0
fi

NOW=$(date +%s)
if [ ! -f "$DIRTY_SINCE" ]; then
  printf '%s\n' "$NOW" > "$DIRTY_SINCE"
  exit 0
fi

STARTED=$(cat "$DIRTY_SINCE" 2>/dev/null || printf '%s' "$NOW")
case "$STARTED" in
  ''|*[!0-9]*) STARTED="$NOW" ;;
esac
ELAPSED_MINUTES=$(( (NOW - STARTED) / 60 ))
BAND=""

if [ "$ELAPSED_MINUTES" -ge "$CRITICAL_MINUTES" ]; then
  BAND="critical"
elif [ "$ELAPSED_MINUTES" -ge "$WARNING_MINUTES" ]; then
  BAND="warning"
fi

[ -n "$BAND" ] || exit 0
[ "$(cat "$LAST_BAND" 2>/dev/null || true)" != "$BAND" ] || exit 0
printf '%s\n' "$BAND" > "$LAST_BAND"

CHANGED_FILES=$(printf '%s\n' "$DIRTY" | wc -l | tr -d ' ')
python3 - "$BAND" "$ELAPSED_MINUTES" "$CHANGED_FILES" <<'PY'
import json
import sys

band, minutes, files = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
if band == "critical":
    context = (
        f"Harness checkpoint: {files} file(s) have remained uncommitted for "
        f"{minutes} minutes. Pause to run relevant verification and ask the user "
        "before committing, stashing, reverting, or splitting the work. The hook "
        "did not change the worktree."
    )
else:
    context = (
        f"Harness checkpoint: {files} file(s) have been dirty for {minutes} "
        "minutes. Check whether a small verified checkpoint is appropriate; do "
        "not commit or stash without authorization."
    )
json.dump(
    {
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": context,
        }
    },
    sys.stdout,
)
PY

exit 0
