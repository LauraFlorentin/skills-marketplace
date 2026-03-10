---
name: harness-gc
description: >
  Garbage collect the harness: find and fix stale documentation, architectural layer
  violations, inconsistent feature states, dead context, and entropy accumulated from
  agent-generated code. Run periodically (weekly or after large sprints) to keep the
  harness healthy and agents oriented correctly. Produces a prioritized cleanup report
  and applies fixes — all written by the agent, never manually. Based on OpenAI's
  "garbage collection agents" pattern and the principle that documentation for agents
  must be maintained by agents. Trigger on: "gc the harness", "clean up harness",
  "docs are stale", "harness drift", "garbage collect", "harness maintenance",
  "agent keeps getting confused", "clean up features.json".
---

# Harness GC

Fights harness entropy. Agent-generated code and docs accumulate drift differently than
human-written code — this skill finds and fixes it systematically.

## What GC Checks

### 1. Documentation Staleness
- AGENTS.md references files that don't exist
- docs/ files reference code paths that have moved or been deleted
- Architecture diagram describes components that no longer exist
- beliefs.md has principles that contradict current code structure

### 2. Feature List Integrity
- Features marked `passes=true` that actually fail when tested
- Features with `in_progress=true` that haven't been touched in 2+ commits
- Features marked `circuit_broken=true` that are now resolved
- Feature descriptions that no longer match the implemented behavior
- Duplicate or conflicting features

### 3. Architectural Layer Violations
- Files importing from higher layers (e.g., `repo/` importing from `ui/`)
- Circular dependencies between packages
- New modules added without being assigned to a layer

### 4. Dead Context
- AGENTS.md operating principles that are now redundant (model improved)
- docs/design/ files for features that were abandoned or changed significantly
- docs/plans/ execution plans for features now marked passes=true (archive them)
- Execution plans with status "In Progress" but feature is marked passes=true (inconsistent)
- Execution plans missing Decision Log entries for non-obvious choices
- Execution plans in docs/plans/ with no corresponding features.json entry (orphaned)
- Tech debt tracker items that were silently resolved

### 5. Progress File Health
- claude-progress.txt entries older than 30 days (summarize and archive)
- Progress notes referencing branches or commits that no longer exist
- Contradictory entries (feature marked done in one entry, failing in another)

### 6. Lock Directory Cleanup
- current_tasks/ files older than 1 hour (stale agent locks)
- current_tasks/ files referencing features already marked passing

### 7. Harness Config Staleness
- SOFT_THRESHOLD / HARD_THRESHOLD may need recalibration (too aggressive or too loose)
- Dev server port changed and init.sh not updated
- `.claude/settings.json` hooks referencing scripts that moved

## Workflow

### Step 1 — Scan

```bash
# Documentation references
echo "=== Checking AGENTS.md references ==="
python3 .harness/scripts/check-doc-refs.py

# Feature integrity
echo "=== Feature list status ==="
python3 -c "
import json
with open('features.json') as f:
    data = json.load(f)
features = data if isinstance(data, list) else data.get('features', [])
issues = []
for f in features:
    if f.get('in_progress') and not f.get('passes'):
        issues.append(f'STUCK_IN_PROGRESS: {f[\"id\"]} - {f[\"description\"][:60]}')
    if f.get('circuit_broken') and f.get('passes'):
        issues.append(f'BROKEN_BUT_PASSING: {f[\"id\"]} - inconsistent state')
for i in issues:
    print(i)
print(f'Total issues: {len(issues)}')
"

# Layer violations
echo "=== Layer constraint check ==="
bash .harness/scripts/check-layers.sh 2>/dev/null || echo "Layer check script not found"

# Stale locks
echo "=== Stale locks ==="
find current_tasks/ -name "*.txt" -mmin +60 2>/dev/null | head -20

# Dead docs
echo "=== Docs referencing dead paths ==="
grep -r "src/" docs/ 2>/dev/null | while read line; do
    path=$(echo "$line" | grep -o 'src/[^"` ]*')
    [ -n "$path" ] && [ ! -e "$path" ] && echo "DEAD REF: $line"
done | head -20

# Quality grades — flag unassessed domains
echo "=== Quality grade coverage ==="
python3 -c "
import re, sys
try:
    with open('docs/quality.md') as f:
        content = f.read()
    unassessed = re.findall(r'\|\s*(\w+)\s*\|\s*—\s*\|', content)
    if unassessed:
        print(f'UNASSESSED DOMAINS ({len(unassessed)}): {', '.join(unassessed)}')
        print('Run harness-gc Step 5 to assign grades.')
    else:
        print('All domains have grades assigned.')
except FileNotFoundError:
    print('WARNING: docs/quality.md not found — run harness-init')
"

# Execution plans — check for orphans and stale plans
echo "=== Execution plan integrity ==="
python3 -c "
import json, os, glob

try:
    with open('features.json') as f:
        data = json.load(f)
    features = data if isinstance(data, list) else data.get('features', [])
    feature_ids = {f['id'] for f in features}
    passing_ids = {f['id'] for f in features if f.get('passes')}
except:
    print('Could not read features.json')
    exit()

plans = glob.glob('docs/plans/plan-*.md')
for plan_path in plans:
    basename = os.path.basename(plan_path)
    feat_id = basename.replace('plan-', '').replace('.md', '')
    if feat_id not in feature_ids:
        print(f'ORPHANED_PLAN: {plan_path} — no matching feature id')
    elif feat_id in passing_ids:
        print(f'COMPLETED_PLAN: {plan_path} — feature passes=true, consider archiving to docs/history/')
print(f'Plans checked: {len(plans)}')
"
```

### Step 2 — Prioritize Issues

Classify by severity:

**P0 — Breaks agent orientation (fix immediately)**
- AGENTS.md references non-existent files
- init.sh broken or points to wrong port
- features.json has JSON syntax errors

**P1 — Causes agent confusion (fix this GC run)**
- Features stuck as in_progress for multiple commits
- Docs describing removed components
- Layer violations in core modules

**P2 — Accumulating entropy (fix this GC run if time)**
- circuit_broken features that are actually resolved
- Progress notes older than 30 days
- Dead design docs

**P3 — Nice to have (log in tech debt tracker)**
- Redundant operating principles
- Over-aggressive circuit breaker thresholds
- Verbose or outdated architecture descriptions

### Step 3 — Apply Fixes

Apply all P0 and P1 fixes. For each fix:

**Stale doc references:**
```bash
# Update the doc to reflect current paths
# Or remove the reference entirely if the component is gone
```

**Stuck in_progress features:**
```python
# Reset to in_progress=False so next agent can pick them up cleanly
feature['in_progress'] = False
feature['passes'] = False
```

**Resolved circuit_broken features:**
```python
# Clear the flag so agents will attempt them again
feature['circuit_broken'] = False
feature['break_reason'] = None
```

**Stale locks:**
```bash
find current_tasks/ -name "*.txt" -mmin +60 -delete
```

**Layer violations:**
```bash
# Move the offending import or restructure the module
# Add the violation to AGENTS.md as a specific prohibition:
echo "LAYER CONSTRAINT: [module] must NEVER import from [layer]. Use [interface] instead." >> AGENTS.md
```

**Archive old progress notes:**
```bash
# Summarize entries older than 30 days into docs/history/progress-archive.md
# Truncate claude-progress.txt to last 30 days
```

### Step 4 — Commit fixes

```bash
git add AGENTS.md features.json docs/ current_tasks/ .harness/ 2>/dev/null
git commit -m "harness-gc: apply P0/P1 fixes — $(date '+%Y-%m-%d')"
```

### Step 5 — Update quality.md

After fixing issues, update `docs/quality.md` grades for any domain touched this GC run.

```python
# Grade each domain based on current state:
# A: all features passing, no violations, clean
# B: minor issues, no critical failures
# C: some features failing or untested
# D: multiple failures, layer violations
# F: broken, blocks other work

# Read features.json, count pass/fail per domain
# Read check-layers.sh output for violations per domain
# Update the grade table in docs/quality.md with today's date
```

This is mandatory — quality.md without grades is an empty file, not a quality tracker.

### Step 6 — Generate GC Report

Create `docs/gc-report-[date].md`:

```markdown
# Harness GC Report — [date]

## Summary
- P0 issues found: [n] | Fixed: [n]
- P1 issues found: [n] | Fixed: [n]  
- P2 issues found: [n] | Fixed: [n]
- P3 issues logged: [n]

## Fixes Applied
[list each fix with before/after]

## Tech Debt Logged
[list P3 items added to tracker]

## Harness Health Score
[overall assessment: Healthy / Needs Attention / Degraded]

## Recommended Next Run
[date — suggest 1 week for active projects, 1 month for stable ones]
```

### Step 7 — Final commit (quality.md + GC report)

```bash
git add docs/quality.md docs/gc-report-*.md docs/history/ 2>/dev/null
git commit -m "harness-gc: update quality grades + GC report — $(date '+%Y-%m-%d')"
```

## Scheduling

For active agent-first projects, run GC:
- After every 50+ feature completions
- After any session where circuit breaker fired 3+ times
- Before starting a new major feature area
- Weekly on projects with daily agent activity

The goal is a harness that gets better over time, not one that slowly decays.
