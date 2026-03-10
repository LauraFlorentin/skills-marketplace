---
name: harness-onboard
description: >
  Session startup ritual for AI coding agents — orients a fresh agent at the start of
  every Claude Code session in a harness-enabled project. Automatically fires via
  SessionStart hook. Reads progress files, git history, feature list, runs the dev
  server smoke test, picks the next feature, and primes the agent with the reasoning
  sandwich (xhigh planning → high implementation → xhigh verification). Eliminates
  the "new agent arrives with no context" problem described in Anthropic's long-running
  agent research. Also implements LangChain's LocalContextMiddleware pattern: maps
  directory structure, available tools, and injects environment context upfront.
  Trigger on: "start a new session", "orient the agent", "session startup", "onboard",
  auto-fires at SessionStart in harness-enabled projects.
---

# Harness Onboard

The session startup ritual. Every new agent session in a harness project starts here.
Based on Anthropic's shift-handoff pattern: each new agent reads the shift notes left
by the previous agent, verifies the environment, then picks up the next task.

## First: Am I the Initializer or a Coding Agent?

This distinction matters. Anthropic's research found that the first session requires
a fundamentally different prompt and task than all subsequent sessions.

```bash
# Check if this is the first session
if [ ! -f "claude-progress.txt" ] || ! grep -q "SESSION" claude-progress.txt; then
  echo "INITIALIZER MODE: No prior sessions detected"
else
  echo "CODING AGENT MODE: Prior sessions exist"
fi
```

### If INITIALIZER (first session, no prior progress):
Your job is **environment setup only** — not feature implementation.
Run `/harness-engineer:init` and follow the full scaffold workflow.
Do NOT start implementing features. Do NOT touch application code.
Your deliverables: AGENTS.md, features.json, init.sh, docs/, layers.json, claude-progress.txt.
End by writing an initial progress entry and committing everything.

### If CODING AGENT (subsequent sessions):
Follow the ritual below. Your job is incremental feature progress.

## The Ritual (run in this exact order)

### 1. Orient (30 seconds)

```bash
# Where am I?
pwd
ls -la

# What's the recent history?
git log --oneline -10

# What was the last session working on?
tail -50 claude-progress.txt

# What's the current feature state?
python3 -c "
import json
with open('features.json') as f:
    data = json.load(f)
features = data if isinstance(data, list) else data.get('features', [])
passing = [f for f in features if f.get('passes') == True]
failing = [f for f in features if f.get('passes') == False and not f.get('circuit_broken')]
broken = [f for f in features if f.get('circuit_broken') == True]
in_prog = [f for f in features if f.get('in_progress') == True]
print(f'✓ Passing: {len(passing)} | ✗ Failing: {len(failing)} | ⚡ Broken: {len(broken)} | ⏳ In Progress: {len(in_prog)}')
print()
print('Next up (top 3 failing by priority):')
todo = sorted([f for f in failing], key=lambda x: x.get('priority', 99))[:3]
for f in todo:
    print(f'  [{f[\"id\"]}] {f[\"description\"][:80]}')
"
```

### 2. Verify Environment

```bash
# Start the dev server (this is mandatory — never skip)
bash init.sh

# If init.sh doesn't exist, find and start the dev server manually:
# node: npm run dev / npm start
# python: python manage.py runserver / uvicorn main:app
# etc.
```

**If init.sh fails:** STOP. Do not write code. Fix init.sh first. The dev server being broken is a P0 harness issue — report it and fix it before anything else.

### 3. Map the Environment (LangChain LocalContextMiddleware pattern)

```bash
# Directory structure
find . -type f -not -path '*/node_modules/*' -not -path '*/.git/*' -not -path '*/.harness/state/*' | head -60

# Available tools (language-specific)
which node python3 python go rust cargo 2>/dev/null
node --version 2>/dev/null; python3 --version 2>/dev/null

# Package info
cat package.json 2>/dev/null | python3 -c "import json,sys; d=json.load(sys.stdin); print('Scripts:', list(d.get('scripts',{}).keys()))" 2>/dev/null
```

### 4. Pick the Next Feature

```python
import json

with open('features.json') as f:
    data = json.load(f)

features = data if isinstance(data, list) else data.get('features', [])

# Skip: passing, circuit_broken, in_progress (from other agents)
candidates = [
    f for f in features
    if not f.get('passes')
    and not f.get('circuit_broken')
    and not f.get('in_progress')
]

# Sort by priority (lower = higher priority)
candidates.sort(key=lambda x: x.get('priority', 99))

if candidates:
    next_feature = candidates[0]
    # Mark as in_progress to prevent other agents grabbing it
    next_feature['in_progress'] = True
    with open('features.json', 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Working on: [{next_feature['id']}] {next_feature['description']}")
    print(f"Steps: {next_feature.get('steps', [])}")
else:
    print("🎉 All features passing! Run harness-gc to clean up.")
```

Also acquire a task lock for multi-agent setups:
```bash
# Claim the task lock (Anthropic C compiler pattern)
echo "$(date): session-$$" > current_tasks/[feature-id].txt
```

**For complex features (3+ files, multiple sessions, or architectural decisions):**
Create an execution plan before writing any code:
```bash
# Copy the template and fill it in
cp .harness/../templates/execution-plan.md.template docs/plans/plan-[feature-id].md
# Fill in: feature spec, approach, files to change, layer analysis, risk assessment
# This becomes the working document for the feature — update it as you go
```
Add `docs/plans/` to AGENTS.md repository map if not already present.

### 5. Apply the Reasoning Sandwich (LangChain pattern)

Structure your work in three phases with appropriate reasoning depth:

**Phase 1 — Plan (xhigh reasoning):**
- Re-read the feature description and steps carefully
- Read relevant existing code before touching anything
- Write a brief plan: what files will change, what approach, what could go wrong
- Verify your plan doesn't violate layers.json constraints

**Phase 2 — Build (high reasoning):**
- Implement one step at a time
- Before writing code, re-read the feature `steps` array — these are your acceptance criteria
- Write code so a person executing those steps in a real browser will see the described behavior
- Write tests as you go, not after — but remember: unit tests passing ≠ steps passing
- Commit partial progress if you complete a logical sub-unit
- Treat the steps array like a CI test suite written by a QA engineer: do not work around it

**Phase 3 — Verify (xhigh reasoning):**
- Run the full test suite
- **Check browser automation availability first:**
  ```bash
  python3 -c "
  import json
  try:
      c = json.load(open('.harness/config.json'))
      ba = c.get('browser_automation', {})
      if ba.get('enabled'):
          print(f'BROWSER: {ba.get(\"mcp_server\",\"puppeteer\")} MCP available — USE IT for verification')
      else:
          print('BROWSER: disabled — verify manually by executing feature steps')
  except: print('BROWSER: config not found — verify manually')
  "
  ```
- **If browser automation enabled**: use the configured MCP tool (e.g. Puppeteer) to navigate and execute each feature step in a real browser. This is the gold standard — Anthropic research shows it prevents premature completion better than any other technique.
- **If browser automation disabled**: manually execute every step in the feature's `steps` array. Open the app, click through the flow. Do not read code to verify — observe behavior.
- Compare result against original feature steps, not against your own code
- Check browser console for errors (even if everything "looks right")
- Only mark `passes=true` after all steps pass and console is clean

### 6. Session End Protocol

Before ending the session:

```bash
# 1. Final commit with descriptive message
git add -A
git commit -m "feat([feature-id]): [what was implemented]"

# 2. Release task lock
rm -f current_tasks/[feature-id].txt

# 3. Update progress file
cat >> claude-progress.txt << EOF

=== SESSION $(date '+%Y-%m-%d %H:%M') ===
Completed: [feature-id] — [description]
State: [passing/partial/abandoned and why]
Next session should: [specific instruction for next agent]
Known issues: [anything that might trip up the next agent]
Commits: $(git log --oneline -3)
===========================================
EOF

# 4. Update feature status
# Mark passes=true if done, in_progress=false in either case
```

## Quick Reference Card

```
START:  pwd → git log → tail claude-progress.txt → python3 features.json summary
VERIFY: bash init.sh (MANDATORY — never skip)
MAP:    find . -type f (top 60) → check tools available
PICK:   features.json → sort by priority → mark in_progress=true → lock current_tasks/
BUILD:  Plan(xhigh) → Build(high) → Verify(xhigh)
TEST:   end-to-end as user, not just unit tests, check browser console
COMMIT: after every feature, descriptive message
END:    git commit → rm lock → update claude-progress.txt → update features.json
```

## If You're Confused

Read these in order:
1. `AGENTS.md` — the map
2. `claude-progress.txt` — what the last agent did
3. `git log --oneline -20` — what changed recently
4. `features.json` — what's left to do
5. `docs/architecture.md` — how the system is structured

If still confused: write a note in claude-progress.txt and start harness-doctor.
