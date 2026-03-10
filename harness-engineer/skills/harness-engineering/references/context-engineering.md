# Context Engineering Reference

## The System of Record Principle
The repository must be the single source of truth. Any decision, constraint, or convention
that exists only in a Slack thread, Google Doc, or developer's head is invisible to the agent.

## Documentation Hierarchy

### CLAUDE.md / AGENTS.md (Top-Level Map)
**Purpose**: Entry point for the agent. A map, not a manual.
**Target length**: Under 200 lines
**What to include**:
- Project purpose and tech stack (2-3 sentences)
- File structure overview
- Entry points (main, tests, config)
- 3-7 core architectural beliefs (enforced, not suggested)
- Pointers to design-docs/ and exec-plans/

**What NOT to include**: Don't put full API contracts, long implementation guides, or naming
conventions here. Those belong in design-docs/ and .cursorrules respectively.

### design-docs/ Directory
**Purpose**: Machine-readable architectural decisions
**Contents**:
- `api-contracts.md` — endpoint schemas, request/response formats
- `state-management.md` — how state flows through the system
- `ui-standards.md` — component patterns, accessibility rules
- `data-models.md` — entity schemas, relationships
- `integration-patterns.md` — third-party service patterns

Each doc should include: decision rationale, constraints, and examples.
These are validated by CI — if code diverges from a documented contract, the pipeline flags it.

### exec-plans/ Directory
**Purpose**: Task-specific implementation logic
**Contents**:
- Feature implementation steps (loaded only when working on that feature)
- Technical debt tracker
- Migration plans
- Rollout checklists

**Key principle**: Exec plans are ephemeral and task-scoped. They're not permanent architecture
docs — they describe what to do *now*, not what the system *is*.

### .cursorrules / .windsurfrules
**Purpose**: Local development constraints
**Contents**:
- Naming conventions (e.g., "all hooks prefixed with `use`")
- Linter configurations
- Import path rules
- Framework-specific patterns

These override global instructions for the specific project context.

## CI Validation of Documentation
Cross-link your docs. A CI check should:
1. Parse CLAUDE.md for all `> See design-docs/X` references
2. Verify those files exist and were recently updated
3. Flag docs that reference deleted code or stale API paths
4. Block merge if the "map" doesn't match the "terrain"

## Context Window Management
When a context file exceeds ~150 lines, agents begin to "soft-ignore" specific rules and fall
back to pattern matching. Signs this is happening:
- Agent follows general patterns but misses specific constraints
- Agent re-introduces code that was explicitly removed
- Naming conventions are inconsistently applied

**Fix**: Split the file. Use a table of contents structure and lazy-load subdocs.

## Example: Well-Structured CLAUDE.md
```markdown
# PaymentsService

## Purpose
Handles payment processing, reconciliation, and fraud detection for the consumer app.
Stack: Node.js, PostgreSQL, Stripe API, Redis for idempotency keys.

## Entry Points
- `src/index.ts` — service bootstrap
- `src/routes/` — HTTP handlers
- `tests/` — Jest test suite
- `infra/` — Terraform configs

## Architecture Beliefs
1. All Stripe calls are idempotent (idempotency key required)
2. Service layer never calls routes directly
3. All monetary values stored as integers (cents), never floats
4. Database transactions wrap all multi-step payment operations
5. External API failures are retried with exponential backoff

## Design Docs
> See design-docs/api-contracts.md for endpoint schemas
> See design-docs/data-models.md for payment entity structure
> See design-docs/integration-patterns.md for Stripe integration patterns

## Current Exec Plan
> See exec-plans/stripe-v2-migration.md for current migration steps
```

---

**Cross-references**: This pattern is implemented by `harness-init` (scaffolding) and validated by `harness-gc` (drift detection).
