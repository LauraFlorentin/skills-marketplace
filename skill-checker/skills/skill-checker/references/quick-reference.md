# Skill Checker — Quick Reference

Condensed rules from "The Complete Guide to Building Skills for Claude" by Anthropic.

---

## Naming Rules

| Rule | Correct | Wrong |
|---|---|---|
| Folder name | `my-cool-skill` | `My Cool Skill`, `my_cool_skill`, `MyCoolSkill` |
| Main file | `SKILL.md` | `skill.md`, `SKILL.MD`, `Skill.md` |
| Name field | `my-cool-skill` | `My Cool Skill` |
| No README.md inside skill folder | docs in SKILL.md or references/ | README.md at skill root |
| Reserved prefixes | anything else | `claude-*`, `anthropic-*` |

---

## YAML Frontmatter Template

```yaml
---
name: skill-name
description: What it does. Use when user says "phrase1", "phrase2", or mentions X. Do NOT use for Y.
license: MIT                        # optional
compatibility: Requires Python 3.8+ # optional, 1-500 chars
metadata:                           # optional
  author: Your Name
  version: 1.0.0
  mcp-server: server-name
---
```

**Forbidden in frontmatter:** XML angle brackets (< >), names containing "claude" or "anthropic"

---

## Description Formula

```
[WHAT it does] + [WHEN to use it / trigger phrases] + [Key capabilities] + [Negative triggers if needed]
```

Good: "Analyzes Figma design files and generates developer handoff documentation. Use when user uploads .fig files, asks for 'design specs', 'component documentation', or 'design-to-code handoff'."

Bad: "Helps with projects."

---

## Progressive Disclosure Levels

| Level | What | Size Target | When Loaded |
|---|---|---|---|
| 1. Frontmatter | name + description | ~100 words | Always (system prompt) |
| 2. SKILL.md body | Full instructions | <500 lines | When skill triggers |
| 3. Bundled files | references/, scripts/, assets/ | Unlimited | On demand |

---

## Folder Structure

```
skill-name/
├── SKILL.md           # Required
├── scripts/           # Optional — executable code
├── references/        # Optional — docs loaded as needed
└── assets/            # Optional — templates, fonts, icons
```

---

## Five Workflow Patterns

1. **Sequential Orchestration** — ordered steps with dependencies and validation gates
2. **Multi-MCP Coordination** — phased work across multiple services
3. **Iterative Refinement** — draft → validate → improve → repeat
4. **Context-Aware Tool Selection** — decision tree for choosing the right tool
5. **Domain-Specific Intelligence** — embedded expertise beyond tool access

---

## Three Skill Categories

1. **Document & Asset Creation** — consistent output generation
2. **Workflow Automation** — multi-step processes with methodology
3. **MCP Enhancement** — workflow guidance on top of MCP tool access

---

## Testing Checklist

**Triggering:**
- ✅ Triggers on obvious tasks
- ✅ Triggers on paraphrased requests
- ❌ Does NOT trigger on unrelated topics

**Functional:**
- Valid outputs generated
- API/MCP calls succeed
- Error handling works
- Edge cases covered

**Performance:**
- Fewer back-and-forth messages than without skill
- Fewer failed API calls
- Lower token consumption

---

## Common Fixes

| Problem | Fix |
|---|---|
| Skill doesn't trigger | Add more trigger phrases to description |
| Skill triggers too often | Add negative triggers, narrow scope |
| Instructions not followed | Move critical steps to top, use imperative form, explain WHY |
| Model "laziness" | Add "Take your time, quality over speed" (better in user prompt than SKILL.md) |
| Slow / degraded responses | Reduce SKILL.md size, use progressive disclosure, check enabled skill count |
| MCP calls fail | Verify connection, check auth, test MCP independently, verify tool names |
