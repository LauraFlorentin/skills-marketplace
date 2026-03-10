#!/usr/bin/env bash
# =============================================================================
# HARNESS ENGINEER — Environment Health Watchdog
# Layer 3: Periodic check of dev server, structural integrity, stale task locks
#
# Fires on: PostToolUse (every N tool calls, configurable)
# Checks:
#   1. Dev server alive (if applicable)
#   2. Structural layer tests passing
#   3. Stale current_tasks/ locks (dead agent cleanup)
#   4. features.json integrity
# =============================================================================

CHECK_INTERVAL=${HARNESS_HEALTH_CHECK_INTERVAL:-10}  # Every N tool calls
STATE_DIR=".harness/state"
TOOL_COUNT_FILE="$STATE_DIR/tool-call-count.txt"
LOCK_DIR="current_tasks"
LOCK_STALE_MINUTES=${HARNESS_LOCK_STALE_MINUTES:-20}
LOG_FILE="$STATE_DIR/watchdog.log"
HEALTH_FILE="$STATE_DIR/health-status.json"

mkdir -p "$STATE_DIR"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# ── Throttle: only run every N tool calls ─────────────────────────────────────

COUNT=0
[ -f "$TOOL_COUNT_FILE" ] && COUNT=$(cat "$TOOL_COUNT_FILE" 2>/dev/null || echo 0)
COUNT=$(( COUNT + 1 ))
echo "$COUNT" > "$TOOL_COUNT_FILE"

if [ $(( COUNT % CHECK_INTERVAL )) -ne 0 ]; then
  exit 0
fi

log "Running health check (tool call #$COUNT)"

ISSUES=()
WARNINGS=()

# ── Check 1: Dev Server Health ────────────────────────────────────────────────

check_dev_server() {
  # Look for common dev server ports or a harness config
  local config=".harness/config.json"
  local port=""

  if [ -f "$config" ]; then
    port=$(python3 -c "
import json
with open('$config') as f:
    c = json.load(f)
print(c.get('dev_server_port', ''))
" 2>/dev/null)
  fi

  # Auto-detect common ports if not configured
  if [ -z "$port" ]; then
    for p in 3000 3001 5173 8000 8080 4000; do
      if lsof -i ":$p" -sTCP:LISTEN -t >/dev/null 2>&1; then
        port=$p
        break
      fi
    done
  fi

  if [ -n "$port" ]; then
    # Try a health check
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" --max-time 3 "http://localhost:$port" 2>/dev/null)
    if [ "$STATUS" = "000" ] || [ -z "$STATUS" ]; then
      ISSUES+=("DEV_SERVER_DOWN: Port $port is not responding")
      log "FAIL: Dev server on port $port not responding"
    else
      log "OK: Dev server on port $port (HTTP $STATUS)"
    fi
  else
    log "SKIP: No dev server port detected"
  fi
}

# ── Check 2: Structural Layer Tests ──────────────────────────────────────────

check_structural_tests() {
  # Look for layer validation scripts the harness-init created
  local layer_test=".harness/scripts/check-layers.sh"
  local package_json="package.json"

  if [ -f "$layer_test" ]; then
    OUTPUT=$(bash "$layer_test" 2>&1)
    EXIT=$?
    if [ $EXIT -ne 0 ]; then
      ISSUES+=("LAYER_VIOLATION: Architectural layer constraint violated")
      log "FAIL: Layer check failed: $OUTPUT"
    else
      log "OK: Layer constraints pass"
    fi
  elif [ -f "$package_json" ]; then
    # Try a quick typecheck if available
    if grep -q '"typecheck"' "$package_json" 2>/dev/null; then
      OUTPUT=$(npm run typecheck --silent 2>&1 | tail -5)
      EXIT=$?
      if [ $EXIT -ne 0 ]; then
        WARNINGS+=("TYPE_ERRORS: TypeScript errors detected (run: npm run typecheck)")
        log "WARN: Type errors detected"
      else
        log "OK: TypeScript clean"
      fi
    fi
  fi
}

# ── Check 3: Stale Task Locks ─────────────────────────────────────────────────

check_stale_locks() {
  if [ ! -d "$LOCK_DIR" ]; then
    return
  fi

  NOW=$(date +%s)
  STALE_THRESHOLD=$(( LOCK_STALE_MINUTES * 60 ))

  while IFS= read -r -d '' lockfile; do
    if [ -f "$lockfile" ]; then
      MODIFIED=$(stat -f "%m" "$lockfile" 2>/dev/null || stat -c "%Y" "$lockfile" 2>/dev/null)
      AGE=$(( NOW - MODIFIED ))
      AGE_MINUTES=$(( AGE / 60 ))

      if [ "$AGE" -gt "$STALE_THRESHOLD" ]; then
        TASK_NAME=$(basename "$lockfile" .txt)
        log "STALE LOCK: $lockfile (${AGE_MINUTES}m old)"
        WARNINGS+=("STALE_LOCK: $TASK_NAME has been locked for ${AGE_MINUTES}m — possible dead agent. Auto-removing.")
        rm -f "$lockfile"
      fi
    fi
  done < <(find "$LOCK_DIR" -name "*.txt" -print0 2>/dev/null)
}

# ── Check 4: features.json Integrity ─────────────────────────────────────────

check_features_integrity() {
  local features_file="features.json"

  if [ ! -f "$features_file" ]; then
    return
  fi

  RESULT=$(python3 -c "
import json, sys

with open('$features_file') as f:
    data = json.load(f)

features = data if isinstance(data, list) else data.get('features', [])
total = len(features)
passing = sum(1 for f in features if f.get('passes') == True)
failing = sum(1 for f in features if f.get('passes') == False)
broken = sum(1 for f in features if f.get('circuit_broken') == True)
in_progress = sum(1 for f in features if f.get('in_progress') == True)

print(f'{total},{passing},{failing},{broken},{in_progress}')
" 2>/dev/null)

  if [ -n "$RESULT" ]; then
    IFS=',' read -r TOTAL PASSING FAILING BROKEN IN_PROGRESS <<< "$RESULT"
    log "Features: total=$TOTAL passing=$PASSING failing=$FAILING broken=$BROKEN in_progress=$IN_PROGRESS"

    if [ "${IN_PROGRESS:-0}" -gt 2 ]; then
      WARNINGS+=("MULTIPLE_IN_PROGRESS: $IN_PROGRESS features marked in_progress simultaneously — possible agent confusion")
    fi

    if [ "${BROKEN:-0}" -gt 0 ]; then
      WARNINGS+=("CIRCUIT_BROKEN_FEATURES: $BROKEN feature(s) were circuit-broken — do not revisit this session")
    fi
  fi
}

# ── Run All Checks ────────────────────────────────────────────────────────────

check_dev_server
check_structural_tests
check_stale_locks
check_features_integrity

# ── Write Health Status ───────────────────────────────────────────────────────

python3 -c "
import json
from datetime import datetime

issues = $(python3 -c "import json; print(json.dumps(${ISSUES[@]+"${ISSUES[*]}"}))" 2>/dev/null || echo '[]')
warnings = $(python3 -c "import json; print(json.dumps(${WARNINGS[@]+"${WARNINGS[*]}"}))" 2>/dev/null || echo '[]')

status = {
    'last_check': datetime.now().isoformat(),
    'tool_call': $COUNT,
    'healthy': len(issues) == 0,
    'issues': issues,
    'warnings': warnings
}

with open('$HEALTH_FILE', 'w') as f:
    json.dump(status, f, indent=2)
" 2>/dev/null

# ── Output Results ────────────────────────────────────────────────────────────

if [ ${#ISSUES[@]} -gt 0 ]; then
  echo ""
  echo "🔴  HARNESS ENGINEER — ENVIRONMENT HEALTH FAILURE"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "Critical issues detected. STOP and fix before continuing:"
  echo ""
  for issue in "${ISSUES[@]}"; do
    echo "  ✗ $issue"
  done
  echo ""
  echo "You are building on a broken foundation."
  echo "Fix these issues FIRST, then resume your current feature."
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  exit 2  # Block the next tool call
fi

if [ ${#WARNINGS[@]} -gt 0 ]; then
  echo ""
  echo "🟡  HARNESS ENGINEER — HEALTH WARNINGS"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  for warning in "${WARNINGS[@]}"; do
    echo "  ⚠ $warning"
  done
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
fi

exit 0
