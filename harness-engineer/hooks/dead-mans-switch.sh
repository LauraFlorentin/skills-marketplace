#!/usr/bin/env bash
# =============================================================================
# HARNESS ENGINEER — Dead Man's Switch Hook
# Layer 2: Detects dirty working tree held too long without a commit
#
# Fires on: PostToolUse (any tool)
# Logic:
#   - Track last commit timestamp
#   - If dirty tree exists AND no commit in TIMEOUT_MINUTES → inject checkpoint
#   - If CRITICAL_TIMEOUT exceeded → force stash + revert
# =============================================================================

TIMEOUT_MINUTES=${HARNESS_COMMIT_TIMEOUT:-15}
CRITICAL_TIMEOUT_MINUTES=${HARNESS_CRITICAL_TIMEOUT:-30}
STATE_DIR=".harness/state"
TIMESTAMP_FILE="$STATE_DIR/last-commit-time.txt"
LOG_FILE="$STATE_DIR/deadmans-switch.log"

mkdir -p "$STATE_DIR"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# ── Check if working tree is dirty ───────────────────────────────────────────

DIRTY=$(git status --porcelain 2>/dev/null)
[ -z "$DIRTY" ] && {
  # Clean tree — update last commit timestamp and exit
  git log -1 --format="%ct" > "$TIMESTAMP_FILE" 2>/dev/null
  exit 0
}

# ── Get time since last commit ────────────────────────────────────────────────

LAST_COMMIT_TIME=$(git log -1 --format="%ct" 2>/dev/null)
NOW=$(date +%s)

if [ -z "$LAST_COMMIT_TIME" ]; then
  # No commits yet — use session start time
  LAST_COMMIT_TIME=$NOW
fi

ELAPSED_SECONDS=$(( NOW - LAST_COMMIT_TIME ))
ELAPSED_MINUTES=$(( ELAPSED_SECONDS / 60 ))

log "Dirty tree detected. Time since last commit: ${ELAPSED_MINUTES}m"

# ── Critical timeout — force stash ───────────────────────────────────────────

if [ "$ELAPSED_MINUTES" -ge "$CRITICAL_TIMEOUT_MINUTES" ]; then
  log "CRITICAL TIMEOUT: ${ELAPSED_MINUTES}m without commit. Forcing stash."

  STASH_MSG="harness-deadmans-critical: ${ELAPSED_MINUTES}m no-commit $(date '+%Y%m%d-%H%M%S')"
  git stash push -m "$STASH_MSG" 2>/dev/null

  cat << EOF

🚨  HARNESS ENGINEER — DEAD MAN'S SWITCH (CRITICAL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
You have had an uncommitted working tree for ${ELAPSED_MINUTES} minutes.

ACTION TAKEN:
  ✓ All changes stashed as: "$STASH_MSG"
  ✓ Repo restored to last clean commit

This means one of three things happened:
  A) You're stuck on a feature that's too large — break it down smaller
  B) The dev environment broke mid-implementation — run init.sh first
  C) You forgot to commit after completing something — check git stash

NEXT STEPS:
  1. Run init.sh — verify the app still works from last clean state
  2. Check stash: git stash show -p stash@{0}
  3. If stash contains good work → cherry-pick what's done, commit it, discard the rest
  4. If stash is all broken → abandon it, restart the feature from scratch

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF
  exit 2
fi

# ── Warning timeout — inject checkpoint prompt ────────────────────────────────

if [ "$ELAPSED_MINUTES" -ge "$TIMEOUT_MINUTES" ]; then
  log "WARNING: ${ELAPSED_MINUTES}m without commit. Injecting checkpoint."

  # Count uncommitted files
  CHANGED_FILES=$(git status --porcelain | wc -l | tr -d ' ')

  cat << EOF

⏱️  HARNESS ENGINEER — COMMIT CHECKPOINT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
You have $CHANGED_FILES uncommitted file(s) and haven't committed in ${ELAPSED_MINUTES} minutes.

PAUSE before your next tool call and assess:

  ✅ If the current feature is WORKING:
     → Run tests, verify end-to-end, then git commit with a descriptive message
     → Update features.json: mark this feature passes=true
     → Update claude-progress.txt with what was completed

  ⚠️  If you're MID-IMPLEMENTATION and it's NOT working yet:
     → Is this taking longer than expected? Consider if the approach is right.
     → Can you commit a partial working state and continue?
     → If you've been on this for ${ELAPSED_MINUTES}m+, the circuit breaker may fire soon.

  🔴 If the dev server or tests are BROKEN:
     → Stop. Run init.sh FIRST.
     → Do not continue building on a broken foundation.

Time until critical timeout (auto-stash): $(( CRITICAL_TIMEOUT_MINUTES - ELAPSED_MINUTES ))m
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF
fi

exit 0
