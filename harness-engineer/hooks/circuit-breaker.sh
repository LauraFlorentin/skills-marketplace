#!/usr/bin/env bash
# =============================================================================
# HARNESS ENGINEER — Circuit Breaker Hook
# Layer 1: Hard loop detection with enforced git stash + revert + requeue
#
# Fires on: PostToolUse (Write, Edit, MultiEdit)
# Logic:
#   1. Track per-file edit counts in .harness/state/edit-counts.json
#   2. Soft nudge at SOFT_THRESHOLD edits to same file
#   3. Hard circuit break at HARD_THRESHOLD — stash, revert, requeue feature
# =============================================================================

SOFT_THRESHOLD=${HARNESS_SOFT_THRESHOLD:-5}
HARD_THRESHOLD=${HARNESS_HARD_THRESHOLD:-10}
STATE_DIR=".harness/state"
EDIT_COUNT_FILE="$STATE_DIR/edit-counts.json"
FEATURES_FILE="features.json"
LOG_FILE="$STATE_DIR/circuit-breaker.log"

mkdir -p "$STATE_DIR"

# ── Helpers ──────────────────────────────────────────────────────────────────

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# Get filepath from Claude Code hook env vars
# Claude Code passes: CLAUDE_TOOL_NAME, CLAUDE_FILE_PATH (or parse from input)
FILEPATH="${CLAUDE_FILE_PATH:-}"

# If no filepath in env, try to parse from CLAUDE_TOOL_INPUT
if [ -z "$FILEPATH" ] && [ -n "$CLAUDE_TOOL_INPUT" ]; then
  FILEPATH=$(echo "$CLAUDE_TOOL_INPUT" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    print(data.get('path', data.get('file_path', data.get('file', ''))))
except:
    print('')
" 2>/dev/null)
fi

# No filepath = not a file edit, skip
[ -z "$FILEPATH" ] && exit 0

log "Edit detected: $FILEPATH"

# ── Edit Count Tracking ───────────────────────────────────────────────────────

# Initialize or load edit counts
if [ ! -f "$EDIT_COUNT_FILE" ]; then
  echo '{}' > "$EDIT_COUNT_FILE"
fi

# Increment count for this file
COUNT=$(python3 -c "
import json, sys

filepath = sys.argv[1]
count_file = sys.argv[2]

with open(count_file, 'r') as f:
    counts = json.load(f)

counts[filepath] = counts.get(filepath, 0) + 1
new_count = counts[filepath]

with open(count_file, 'w') as f:
    json.dump(counts, f, indent=2)

print(new_count)
" "$FILEPATH" "$EDIT_COUNT_FILE" 2>/dev/null)

COUNT=${COUNT:-0}
log "Edit count for $FILEPATH: $COUNT"

# ── Soft Nudge ────────────────────────────────────────────────────────────────

if [ "$COUNT" -eq "$SOFT_THRESHOLD" ]; then
  log "SOFT NUDGE triggered for $FILEPATH (count=$COUNT)"
  cat << EOF

⚠️  HARNESS ENGINEER — LOOP WARNING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
You have edited '$FILEPATH' $COUNT times in this session.

This is a signal that you may be stuck. Before continuing:

1. STOP and re-read the original task spec in features.json
2. Ask: is my current approach fundamentally broken?
3. If yes → git stash, start fresh with a different approach
4. If no → explain to yourself WHY the next edit will be different

Do NOT make the same type of edit again without a clear new hypothesis.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF
  # Return message to Claude via stdout (Claude Code reads hook stdout)
  exit 0
fi

# ── Hard Circuit Break ────────────────────────────────────────────────────────

if [ "$COUNT" -ge "$HARD_THRESHOLD" ]; then
  log "HARD CIRCUIT BREAK triggered for $FILEPATH (count=$COUNT)"

  # 1. Identify which feature is currently being worked on
  CURRENT_FEATURE=""
  if [ -f "$FEATURES_FILE" ]; then
    CURRENT_FEATURE=$(python3 -c "
import json
with open('$FEATURES_FILE', 'r') as f:
    features = json.load(f)

# Find first in-progress feature (passes=false but has been touched)
# Heuristic: look for feature with 'in_progress': true flag
for feature in features if isinstance(features, list) else features.get('features', []):
    if feature.get('in_progress') or feature.get('passes') == 'in_progress':
        print(feature.get('description', feature.get('id', 'unknown')))
        break
" 2>/dev/null)
  fi

  # 2. Stash dirty working tree
  log "Stashing dirty working tree..."
  STASH_MSG="harness-circuit-break: $FILEPATH edit-count=$COUNT $(date '+%Y%m%d-%H%M%S')"
  git stash push -m "$STASH_MSG" 2>/dev/null
  STASH_EXIT=$?

  # 3. If stash succeeded, we're back to last clean commit
  # If nothing to stash, we're already clean (just reset file counts)

  # 4. Requeue the feature — mark it as failing again
  if [ -n "$CURRENT_FEATURE" ] && [ -f "$FEATURES_FILE" ]; then
    python3 -c "
import json
feature_desc = '''$CURRENT_FEATURE'''
with open('$FEATURES_FILE', 'r') as f:
    data = json.load(f)

features = data if isinstance(data, list) else data.get('features', [])
for feature in features:
    if feature.get('description') == feature_desc or feature.get('in_progress'):
        feature['passes'] = False
        feature['in_progress'] = False
        feature['circuit_broken'] = True
        feature['break_reason'] = f'Circuit breaker fired: {int($COUNT)} edits to $FILEPATH'
        break

out = data if isinstance(data, list) else data
with open('$FEATURES_FILE', 'w') as f:
    json.dump(out, f, indent=2)
print('Feature requeued.')
" 2>/dev/null
  fi

  # 5. Reset edit counts for this file
  python3 -c "
import json
with open('$EDIT_COUNT_FILE', 'r') as f:
    counts = json.load(f)
counts['$FILEPATH'] = 0
with open('$EDIT_COUNT_FILE', 'w') as f:
    json.dump(counts, f, indent=2)
" 2>/dev/null

  # 6. Log the break event
  BREAK_LOG="$STATE_DIR/breaks.log"
  echo "$(date '+%Y-%m-%d %H:%M:%S') | file=$FILEPATH | count=$COUNT | stash='$STASH_MSG' | feature='$CURRENT_FEATURE'" >> "$BREAK_LOG"

  # 7. Output hard stop message to Claude
  cat << EOF

🚨  HARNESS ENGINEER — CIRCUIT BREAKER FIRED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HARD STOP. You have edited '$FILEPATH' $COUNT times.

ACTION TAKEN AUTOMATICALLY:
  ✓ Dirty working tree stashed as: "$STASH_MSG"
  ✓ Repo restored to last clean commit
  ✓ Feature requeued as failing in features.json
  ✓ Edit counts reset for this file

WHAT YOU MUST DO NOW:
  1. Read features.json — pick the NEXT highest-priority failing feature
     (skip the one that just broke — it's been flagged as circuit_broken)
  2. Run init.sh to verify the app is in a working state
  3. Start fresh on a DIFFERENT feature
  4. Return to the broken feature only after 2+ other features are complete

The stash is preserved. A human engineer can inspect it with:
  git stash list
  git stash show -p stash@{0}

DO NOT attempt to pop the stash or return to this file this session.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF

  exit 2  # Exit code 2 = block the tool call (Claude Code respects this)
fi

exit 0
