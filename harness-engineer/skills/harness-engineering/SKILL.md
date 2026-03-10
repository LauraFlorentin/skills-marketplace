---
name: harness-engineering
description: >
  Expert guide for designing autonomous AI agent systems using harness engineering principles —
  the full environment of scaffolding, constraints, alignment, and evaluation that makes AI
  agents production-reliable. Use this skill whenever the user asks about: building AI agent
  systems or pipelines, designing context/prompt/scaffolding architecture, setting up evaluation
  frameworks or benchmarks for AI agents, aligning AI behavior with constitutional principles,
  measuring AI agent performance (accuracy, latency, cost, safety), debugging or improving agent
  reliability, or any request involving "agents", "harness", "evals", "scaffolding",
  "LangSmith", "CI/CD for AI", "agentic workflows", "multi-agent systems", or similar.
triggers:
  - harness engineering
  - context engineering
  - constitutional ai
  - evaluation framework
  - CLASS metrics
  - agent alignment
  - evals
  - scaffolding architecture
  - agent performance
  - CI/CD for AI
---

# Harness Engineering

Harness engineering is the discipline of designing the full environment surrounding an AI agent
— the scaffolding, constraints, feedback loops, and evaluation pipelines — that makes agentic
behavior reliable, observable, and aligned in production.

> The model provides the intelligence. The harness provides the control.

Read `references/context-engineering.md` for deep guidance on CLAUDE.md / AGENTS.md patterns.
Read `references/alignment.md` for Constitutional AI and value hierarchy implementation.
Read `references/evaluation-framework.md` for evaluation harness design and benchmarking.

---

## How This Skill Relates to the Plugin

This skill provides the **theory and research foundation** that informs the plugin's four operational skills:

| Operational Skill | Theory Connection |
|---|---|
| `harness-init` | Context Engineering — the doc hierarchy and CLAUDE.md patterns scaffold during init come from these principles |
| `harness-doctor` | Alignment & Anti-Patterns — doctor diagnoses failures that often stem from architectural drift and constraint violations described here |
| `harness-gc` | Entropy Management — gc implements the garbage collection agent pattern theorized in context engineering research |
| `harness-onboard` | Observability — onboard orients new sessions using the tracing and documentation principles from this skill |

**Use this skill when you need to understand _why_ the operational skills work the way they do, or when designing new harness patterns from scratch.**

---

## The Three Pillars of Harness Engineering

### 1. Context Engineering
Ensuring the agent has the *right information at the right time*.

**Core principle**: Anything inaccessible to the agent in-context does not exist. Repository = single source of truth.

**Layered documentation structure** (avoid monolithic instruction files):
```
CLAUDE.md / AGENTS.md    → Top-level map: project structure, entry points, core beliefs
design-docs/             → API contracts, state management patterns, UI standards
exec-plans/              → Feature steps, tech debt trackers, task-specific logic
.cursorrules             → Local constraints: naming conventions, linter configs
```

**When to use which file**:
- CLAUDE.md is the *map*, not the *manual*. Keep it under 200 lines — it should point, not repeat.
- Design docs are machine-readable architectural decisions, validated by CI.
- Exec plans are task-specific; load them only when relevant.

### 2. Architectural Constraints
Enforcing structural boundaries that prevent agentic drift and converge on correct solutions faster.

**Dependency layering** (enforce via pre-commit hooks + structural tests):
```
Types → Config → Repo → Service → Runtime → UI
```
Each domain imports only from layers to its left. This is enforced mechanically, not suggested.

**Entropy management**: Schedule "garbage collection" agents to:
- Detect documentation drift from codebase reality
- Resolve circular dependencies
- Verify naming convention compliance
- Flag and remove dead code

**LLM-based auditors**: Use a second agent (with no generation context) to review the primary agent's outputs for architectural violations before committing.

### 3. Evaluation Harness
Continuously measuring agent behavior across accuracy, cost, latency, safety, and consistency.

**Five-stage evaluation pipeline**:
1. **Task Definition** — dataset (prompts + ground truth), prompt template, scoring metric
2. **Model Interface** — standardized API connectors (OpenAI, Anthropic, local vLLM/HuggingFace)
3. **Inference Execution** — batching, token tracking, caching to avoid redundant calls
4. **Scoring & Aggregation** — exact match, F1, semantic similarity, `pass@k` for code
5. **Reporting** — leaderboards, dashboards, regression diffs across model versions

---

## Multi-Dimensional Performance Metrics

Never evaluate on accuracy alone. Use the **CLASS framework**:

| Metric | What to Measure | Why It Matters |
|---|---|---|
| **C**ost | Token usage, API expense per query | Economic sustainability |
| **L**atency | P50 and P99 response times | User experience |
| **A**ccuracy | Exact match, semantic similarity, pass@k | Core utility |
| **S**tability | Paraphrase consistency, deterministic output | Behavioral reliability |
| **S**afety | Refusal rates, toxicity, jailbreak resistance | Compliance and risk |

A system is considered production-ready not because it succeeds once, but because it **behaves predictably across different inputs, environments, and conditions**.

### Code Evaluation: pass@k
For coding tasks, prefer `pass@k` over single-attempt accuracy:

$$pass@k = E\left[1 - \frac{\binom{n-c}{k}}{\binom{n}{k}}\right]$$

Where `n` = total samples, `c` = correct samples, `k` = attempts allowed.

---

## Alignment: Constitutional AI in Practice

For agents operating in regulated or high-stakes domains, implement a value priority hierarchy:

| Priority | Value | Practical Application |
|---|---|---|
| Tier 1 | Safety & Oversight | Human control preserved; no autonomous irreversible actions |
| Tier 2 | Ethical Behavior | Honest, harm-avoiding, transparent about reasoning |
| Tier 3 | Compliance | Follows org guidelines, legal constraints, domain regulations |
| Tier 4 | Helpfulness | Meets user goals effectively within above constraints |

**Self-alignment loop** (RLAIF pattern):
1. Agent generates initial response
2. Agent critiques response against a stated principle
3. Agent rewrites response
4. Repeat — internalized behavior without exhaustive human labeling

Constitutional AI produces a **Pareto improvement**: the agent becomes simultaneously more helpful *and* more harmless, rather than trading one for the other.

---

## Observability & CI/CD Integration

### Tracing
Use nested span tracing (e.g., LangSmith) to visualize the full trajectory of multi-turn agentic workflows:
- Every LLM call, tool execution, and vector DB retrieval is logged as a span
- Cost and latency are attributed to specific sub-actions
- Hallucinations and logic errors are debuggable at the exact deviation point

### Evaluation Lifecycle (CI/CD)
Treat AI updates with the same rigor as software releases:

| Mode | Context | Purpose |
|---|---|---|
| **Offline** | Pre-release / dev | Regression testing against golden sets |
| **Online** | Production | Real-time quality drift detection |
| **Simulation** | Historical data | Forecast on thousands of real tickets |

---

## Common Anti-Patterns to Avoid

- **Monolithic AGENTS.md**: One giant file consumes context and causes the agent to ignore specific rules. Use the map-and-docs pattern.
- **Evaluating on accuracy only**: A model that always refuses is 100% "safe" but useless. Always include helpfulness.
- **Using the same model for generation and evaluation**: Self-enhancement bias inflates scores.
- **Skipping dependency layer enforcement**: Without mechanical enforcement (pre-commit hooks, structural tests), architectural drift happens silently.
- **Static benchmarks only**: Models memorize benchmarks over time. Rotate in dynamic / held-out eval sets.
- **No tracing in production**: Without span-level observability, debugging agentic failures is nearly impossible.

---

## Practical Output Templates

### CLAUDE.md Starter Template
```markdown
# [Project Name]

## What this is
[One paragraph: purpose, stack, key constraints]

## Entry points
- Main: [path]
- Tests: [path]
- Config: [path]

## Core beliefs
- [Principle 1: e.g., "Service layer never calls UI layer"]
- [Principle 2: e.g., "All external calls are wrapped in retry logic"]

## Design docs
> See design-docs/ for API contracts and architecture decisions
> See exec-plans/ for current feature implementation steps
```

### Evaluation Harness Config (JSON)
```json
{
  "task_name": "customer-support-agent",
  "model": "claude-sonnet-4-20250514",
  "metrics": ["exact_match", "semantic_f1", "latency_p99", "refusal_rate"],
  "evaluation_modes": ["offline", "online"],
  "golden_set": "evals/golden-set-v2.jsonl",
  "judge_model": "claude-opus-4-20250514",
  "positional_swap": true,
  "verbosity_penalty": true
}
```

---

## Research Foundation

- **OpenAI** (Feb 13 2026): Context engineering, architectural constraints, garbage collection agents
- **Anthropic** (Nov 26 2025): Dual-agent architecture, progress files, JSON feature lists, git checkpoints
- **LangChain** (Feb 17 2026): LoopDetectionMiddleware, PreCompletionChecklist, reasoning sandwich, trace analysis

## Cross-References

- **Operational skills**: See `harness-init`, `harness-doctor`, `harness-gc`, `harness-onboard` for applying these principles
- **Orchestrator**: See `../../agents/orchestrator.md` for autonomous multi-skill workflows
