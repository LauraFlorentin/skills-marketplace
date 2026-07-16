#!/usr/bin/env bash
# Create or verify optional project-local Harness Engineer state.
# Plugin hooks are discovered from hooks/hooks.json; this script does not edit
# Claude settings, Git state, or existing project files.

set -eu

MODE="${1:-configure}"
PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$PWD}"
HARNESS_DIR="$PROJECT_DIR/.harness"

if [ "$MODE" = "--verify" ]; then
  status=0
  if [ -f "$HARNESS_DIR/config.json" ]; then
    printf 'ok: %s\n' "$HARNESS_DIR/config.json"
    python3 -m json.tool "$HARNESS_DIR/config.json" >/dev/null || status=1
  else
    printf 'missing: %s\n' "$HARNESS_DIR/config.json"
    status=1
  fi
  [ -d "$HARNESS_DIR/state" ] && printf 'ok: %s\n' "$HARNESS_DIR/state" || printf 'optional: runtime state directory will be created by hooks\n'
  printf 'plugin hooks: packaged in hooks/hooks.json; no project settings entry is required\n'
  exit "$status"
fi

if [ "$MODE" != "configure" ] && [ "$MODE" != "--configure" ]; then
  printf 'Usage: bash install.sh [--configure|--verify]\n' >&2
  exit 2
fi

mkdir -p "$HARNESS_DIR/state"

if [ -e "$HARNESS_DIR/config.json" ]; then
  printf 'preserved existing %s\n' "$HARNESS_DIR/config.json"
else
  config=$(cat <<'EOF'
{
  "model": "unspecified",
  "circuit_breaker": {
    "soft_threshold": 5,
    "confirmation_threshold": 10
  },
  "checkpoint_reminder": {
    "warning_minutes": 30,
    "critical_minutes": 60
  },
  "watchdog": {
    "check_interval_tool_calls": 20,
    "lock_stale_minutes": 30
  },
  "browser_automation": {
    "enabled": false
  }
}
EOF
)
  printf '%s\n' "$config" > "$HARNESS_DIR/config.json"
  printf 'created %s\n' "$HARNESS_DIR/config.json"
fi

printf '%s\n' 'No Claude settings or Git state were changed.'
printf '%s\n' 'Review the generated configuration before committing it.'
