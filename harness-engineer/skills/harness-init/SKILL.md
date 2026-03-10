---
name: harness-init
description: >
  Scaffold a complete harness for any new project or repo so AI coding agents can work
  effectively across multiple sessions. Use whenever starting a new project with Claude Code,
  Codex, or any AI agent, or when an existing project has no harness and agents keep losing
  context between sessions. Creates: AGENTS.md table-of-contents, docs/ knowledge base,
  features.json with all features pre-marked failing, init.sh dev server startup script,
  claude-progress.txt handoff file, current_tasks/ multi-agent lock directory,
  layers.json architectural dependency graph, and wires the circuit breaker hooks.
  Trigger on: "set up harness", "scaffold this project", "init harness", "new project",
  "agent keeps forgetting context", "set up for agent-first development".
---

# Harness Init

Scaffolds a production-ready harness for agent-first development. Run once per project.
Subsequent agent sessions use harness-onboard to orient themselves from the scaffold.

## What Gets Created

```
project-root/
├── AGENTS.md                    ← 100-line TOC pointing into docs/
├── docs/
│   ├── architecture.md          ← Domain map + package layering
│   ├── design/                  ← Feature design docs
│   ├── plans/                   ← Versioned execution plans (one per complex feature)
│   ├── history/                 ← Archived progress notes (GC moves old entries here)
│   ├── quality.md               ← Per-domain quality grades (updated each GC run)
│   └── beliefs.md               ← Core agent-first operating principles
├── features.json                ← All features, initially passes=false
├── claude-progress.txt          ← Handoff log between sessions
├── init.sh                      ← Start dev server + smoke test
├── current_tasks/               ← Multi-agent task locks
├── layers.json                  ← Architectural dependency constraints
└── .harness/
    ├── hooks/                   ← Circuit breaker scripts
    ├── config.json              ← Dev server port, thresholds
    └── state/                   ← Runtime state (gitignored)
```

## Workflow

### Step 1 — Gather Context

Before generating any files, ask the agent (or read from existing repo):

1. What is this project? (app type, stack, primary language)
2. What are the top 5–10 high-level features?
3. What port does the dev server run on? (or how to detect it)
4. Is this multi-agent (parallel Claude instances) or single-agent?
5. What architectural layers exist? (use defaults if unclear)
6. Which model will be used? (claude / codex / gemini — sets `.harness/config.json model`)
7. Is Puppeteer MCP available for browser automation? (recommended — set `browser_automation.enabled=true` if yes)

If run on an existing repo: run `find . -type f | head -50` and `cat package.json` (or equivalent) to infer stack answers automatically. Do not ask if you can infer.

### Step 2 — Generate AGENTS.md

Keep it under 100 lines. It is a MAP, not an encyclopedia.
Use the `templates/AGENTS.md.template` as the base. Key sections to fill in:

- **What This Project Is**: 1-paragraph description inferred from repo/prompt
- **Repository Map**: fill paths for docs/plans/ if non-standard
- **Two Agent Modes**: leave as-is — this is the initializer/coding-agent gate
- **Operating Principles**: keep defaults, add project-specific rules at the end
- **Verification Contract**: keep verbatim — this is the slop-prevention mechanism

The example in the template is the canonical form. Do not simplify it.

### Step 3 — Generate features.json

Expand the user's prompt into a comprehensive feature list. For a web app, aim for 50–200 features. Each feature must be testable end-to-end by a human executing the steps in a real browser — not by reading code.

Use the `templates/features.json.template` as the base. The `_verification_contract` field is mandatory and must not be removed — it is the slop-prevention mechanism.

Feature schema:
```json
{
  "id": "feat-001",
  "category": "functional",
  "priority": 1,
  "description": "User can open the app and see the home screen",
  "steps": [
    "Navigate to localhost:[port]",
    "Verify home screen loads without errors",
    "Check that primary navigation is visible"
  ],
  "passes": false,
  "in_progress": false,
  "circuit_broken": false,
  "break_reason": null
}
```

**Step-writing rules:**
- Each step must be executable by a person in a browser — "click", "navigate", "verify visible", "submit form"
- No step should say "check the code" or "review the implementation" — behavior only
- Include at least one negative/edge-case step per feature (e.g., "Submit empty form, verify error message appears")
- Steps are immutable once written — agents may NOT edit them

**Agent field permissions (embed in _instructions):**
- `passes`, `in_progress`, `circuit_broken`, `break_reason`: agent-writable
- All other fields: READ-ONLY — editing them is unacceptable

### Step 4 — Generate init.sh

```bash
#!/usr/bin/env bash
# Harness init script — run at the start of every agent session
set -e

echo "=== HARNESS: Starting dev environment ==="

# 1. Install dependencies if needed
[[ -f package.json ]] && npm install --silent
[[ -f requirements.txt ]] && pip install -r requirements.txt -q

# 2. Start dev server in background (customize per stack)
npm run dev &> .harness/state/dev-server.log &
DEV_PID=$!
echo $DEV_PID > .harness/state/dev-server.pid

# 3. Wait for server to be ready
echo "Waiting for server on port [PORT]..."
for i in {1..30}; do
  curl -s http://localhost:[PORT] > /dev/null 2>&1 && break
  sleep 1
done

# 4. Smoke test — verify baseline still works
echo "Running smoke test..."
curl -sf http://localhost:[PORT] > /dev/null || { echo "ERROR: App not responding"; exit 1; }

echo "=== HARNESS: Environment ready ==="
echo "Dev server: http://localhost:[PORT] (PID: $DEV_PID)"
```

Customize PORT and start command from the detected stack.

### Step 5 — Generate layers.json

Default web app layer structure (customize as needed):

```json
{
  "layers": [
    { "name": "types", "order": 1, "description": "Type definitions, interfaces, constants" },
    { "name": "config", "order": 2, "description": "Configuration, environment variables" },
    { "name": "repo", "order": 3, "description": "Data access, database queries" },
    { "name": "service", "order": 4, "description": "Business logic, domain operations" },
    { "name": "runtime", "order": 5, "description": "API routes, controllers, middleware" },
    { "name": "ui", "order": 6, "description": "Frontend components, pages" }
  ],
  "rule": "Each layer may only import from layers with lower order numbers",
  "enforcement": ".harness/scripts/check-layers.sh"
}
```

### Step 6 — Initialise docs/ structure

Create these files at scaffold time:

**`docs/plans/README.md`** — explains the plans directory:
```markdown
# Execution Plans

Versioned work artifacts for complex features. One plan per feature that requires
more than one agent session or has non-obvious architectural decisions.

**When to create a plan:** Any feature that touches 3+ files, requires a decision
between competing approaches, or is likely to span multiple sessions.

**Template:** See `.harness/../templates/execution-plan.md.template`
**Naming:** `plan-[feature-id].md` (e.g., `plan-feat-042.md`)

Plans are the memory of WHY decisions were made. Future agents read them.
Any decision made in your head that isn't here doesn't exist.
```

**`docs/quality.md`** — structured grading template (see Step 8 below)

**`docs/beliefs.md`** — core operating principles for this specific project:
```markdown
# Agent Operating Beliefs

These are the core principles that govern how agents work on this project.
Updated as the project evolves — add new beliefs when patterns emerge.

1. **Repo is the world.** Nothing outside this repository exists for agents.
2. **One feature, one commit.** Atomicity prevents cascading failures.
3. **Test behavior, not code.** The steps array is the spec. Execute it.
4. **Failure = signal.** Every agent mistake points to a missing harness component.
5. **Clean state is non-negotiable.** Never leave the codebase in a state you wouldn't merge.
```

### Step 7 — Generate quality.md

```markdown
# Quality Grades

Updated by harness-gc on each run. Tracks health per domain and layer.
Scale: A (excellent) → B (good) → C (needs work) → D (broken) → F (critical)

| Domain/Layer | Grade | Last Updated | Notes |
|---|---|---|---|
| types | — | [date] | Not yet assessed |
| config | — | [date] | Not yet assessed |
| repo | — | [date] | Not yet assessed |
| service | — | [date] | Not yet assessed |
| runtime | — | [date] | Not yet assessed |
| ui | — | [date] | Not yet assessed |

## Assessment Criteria
- **A**: All features in domain passing, no layer violations, clean test coverage
- **B**: Minor issues, no critical failures, 1–2 tech debt items
- **C**: Some features failing or untested, architectural concerns present
- **D**: Multiple failures, layer violations, agent struggles to work in this area
- **F**: Domain is broken, blocks other work, requires human intervention

## Open Issues by Domain
[Updated by harness-gc — leave empty until first GC run]
```

### Step 8 — Wire Circuit Breaker Hooks

Copy hooks from the plugin and run install.sh to wire `.claude/settings.json`.
See `../../hooks/` and `../../install.sh`.

### Step 9 — Initial Git Commit

```bash
git add AGENTS.md features.json init.sh claude-progress.txt layers.json docs/ current_tasks/ .harness/
git commit -m "harness: initial scaffold via harness-engineer plugin"
```

## Output Summary

After init, tell the user:
- How many features were generated in features.json
- What port the dev server is configured for
- That circuit breaker hooks are active
- The model configured in `.harness/config.json`

**Then stop.** Your role as initializer is complete.

The next agent session is a coding agent — it will pick up features via harness-onboard.
Do NOT begin implementing features in this session.
Do NOT write application code.
Commit the scaffold and hand off.

First command for the user to run next: `bash init.sh` to verify the environment is wired correctly.
