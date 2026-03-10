---
name: harness-doctor
description: >
  Analyze agent failures and automatically generate harness fixes to prevent recurrence.
  Use whenever an agent session went wrong, produced broken output, got stuck in a loop,
  failed to complete features, or the codebase is in a bad state after an agent run.
  Reads git log, progress files, circuit breaker logs, and test output to diagnose the
  failure mode, then generates a targeted harness patch (AGENTS.md update, features.json
  fix, new hook, or architectural constraint) that prevents the same failure from happening
  again. Based on LangChain's Trace Analyzer and OpenAI's "failure = harness signal" principle.
  Trigger on: "agent failed", "session went wrong", "agent got stuck", "loop broke",
  "agent made a mess", "why did it fail", "harness doctor", "fix my harness".
---

# Harness Doctor

Diagnoses agent session failures and generates targeted harness patches.
The core principle (OpenAI): every agent failure is a harness gap. Don't just fix the code — fix the system so the agent never makes the same mistake again.

## Failure Mode Taxonomy

| Code | Name | Symptoms |
|---|---|---|
| `DOOM_LOOP` | Same file edited 5+ times | Circuit breaker log, high edit count |
| `PREMATURE_EXIT` | Agent declared done too early | Features marked passing that fail manually |
| `ONE_SHOT` | Tried to build everything at once | Single large commit, context exhaustion |
| `DIRTY_STASH` | Dead Man's Switch fired | Stash entry in git stash list |
| `BROKEN_FOUNDATION` | Built on broken dev server | Watchdog log showing server down |
| `LAYER_VIOLATION` | Imported across layer boundary | layers.json check failure |
| `CONTEXT_BLIND` | Agent didn't read progress/features | Missing reads in tool call history |
| `ENVIRONMENT_BLIND` | Agent didn't run init.sh | No smoke test in session log |

## Workflow

### Step 1 — Collect Evidence

Run these commands to gather diagnostic data:

```bash
# Git history of last session
git log --oneline -20

# Circuit breaker log
cat .harness/state/circuit-breaker.log 2>/dev/null || echo "No circuit breaker log"

# Dead man's switch log  
cat .harness/state/deadmans-switch.log 2>/dev/null || echo "No DMS log"

# Watchdog log
cat .harness/state/watchdog.log 2>/dev/null || echo "No watchdog log"

# Break audit trail
cat .harness/state/breaks.log 2>/dev/null || echo "No breaks logged"

# Stash list (Dead Man's Switch entries)
git stash list | grep harness || echo "No harness stashes"

# Progress file
cat claude-progress.txt 2>/dev/null | tail -30

# Feature status summary
python3 -c "
import json
with open('features.json') as f:
    data = json.load(f)
features = data if isinstance(data, list) else data.get('features', [])
total = len(features)
passing = sum(1 for f in features if f.get('passes') == True)
broken = sum(1 for f in features if f.get('circuit_broken') == True)
in_prog = sum(1 for f in features if f.get('in_progress') == True)
print(f'Features: {total} total, {passing} passing, {broken} circuit-broken, {in_prog} in-progress')
" 2>/dev/null

# Current dirty state
git status --short
```

### Step 2 — Classify Failure Mode

Based on evidence, identify the primary failure mode(s) from the taxonomy above.
Multiple modes can co-occur (e.g., DOOM_LOOP + DIRTY_STASH).

### Step 3 — Generate Harness Patch

For each identified failure mode, generate the appropriate fix:

#### DOOM_LOOP → Lower circuit breaker threshold or add approach-diversity prompt
```bash
# In .claude/settings.json harness section:
# Lower SOFT_THRESHOLD from 5 → 3 for this project
# Add to AGENTS.md operating principles:
echo "9. Before editing a file for the 3rd time, write down WHY this attempt will succeed where the previous ones failed." >> AGENTS.md
```

#### PREMATURE_EXIT → Strengthen PreCompletionChecklist
Add to AGENTS.md:
```
BEFORE marking any feature passes=true, you MUST:
1. Run init.sh fresh (kill and restart the dev server)
2. Navigate to the feature as a user would
3. Test at least 2 edge cases, not just the happy path
4. Check browser console for errors
Passing your own unit test is NOT sufficient.
```

#### ONE_SHOT → Add explicit single-feature constraint
Add to AGENTS.md:
```
HARD CONSTRAINT: You may work on exactly ONE feature per session.
After completing and committing one feature, start a new session.
Do not implement more than one features.json item before committing.
```

#### DIRTY_STASH → Add commit reminder to features workflow
Add to AGENTS.md:
```
COMMIT PROTOCOL: After completing ANY work unit (even partial):
  git add -A && git commit -m "wip: [description of what's done"
If you haven't committed in 15 minutes, something is wrong. Stop and assess.
```

#### BROKEN_FOUNDATION → Make init.sh mandatory
Add to AGENTS.md:
```
SESSION START IS NON-NEGOTIABLE:
  bash init.sh
If init.sh fails, STOP. Do not write a single line of code until it passes.
The app must be in a known working state before you touch it.
```

#### LAYER_VIOLATION → Add import linting hook
```bash
# Add to .claude/settings.json PostToolUse hooks:
# Run layer check after every Write
bash .harness/scripts/check-layers.sh
```

#### CONTEXT_BLIND → Add explicit reading to onboard ritual
Strengthen harness-onboard for this project (see harness-onboard skill).

#### ENVIRONMENT_BLIND → Wire init.sh to SessionStart hook
```json
{
  "SessionStart": [{
    "matcher": "*",
    "hooks": [{"type": "command", "command": "bash init.sh"}]
  }]
}
```

### Step 4 — Apply Patches

Apply all generated patches. Always apply by having Claude write the fix — never manually.

```bash
# After applying patches, commit them
git add AGENTS.md .claude/settings.json .harness/
git commit -m "harness-doctor: fix [FAILURE_MODE] — [one line description]"
```

### Step 5 — Write Doctor Report

Append to `claude-progress.txt`:

```
=== HARNESS DOCTOR REPORT [timestamp] ===
Failure modes detected: [list]
Root causes:
  - [cause 1]
  - [cause 2]
Patches applied:
  - [patch 1]: [what changed and why]
  - [patch 2]: [what changed and why]
Prevention: [what the harness now does differently]
Next session: [recommended starting point]
===========================================
```

### Step 6 — Recover Working State

If the repo is in a dirty state:
```bash
# Option A: stash exists with good work
git stash list  # find the relevant harness stash
git stash show -p stash@{0}  # inspect it
# Cherry-pick what's good, discard the rest

# Option B: everything is broken, start clean
git checkout -- .  # discard all uncommitted changes
# Find last known good commit
git log --oneline | head -20
# Reset if needed
git reset --hard [good-commit-sha]
```

## Output

Tell the user:
1. What failure mode(s) were detected
2. What harness patches were applied
3. Whether the repo needed recovery and what state it's in now
4. What to run next (`bash init.sh` to verify, then resume)
