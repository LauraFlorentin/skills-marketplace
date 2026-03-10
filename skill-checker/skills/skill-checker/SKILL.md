---
name: skill-checker
description: Validate, review, and improve Claude skills against Anthropic's official best practices from "The Complete Guide to Building Skills for Claude." Use when a user says "check my skill", "review this skill", "validate my SKILL.md", "is my skill good", "skill audit", "skill review", "proof check my skill", "grade my skill", or uploads a skill folder or SKILL.md for feedback. Also trigger when the user mentions skill quality, skill triggering issues, skill debugging, or wants to ensure a skill follows Anthropic's official guidelines before publishing or sharing.
---

# Skill Checker

A comprehensive skill validation and review tool based on Anthropic's official "Complete Guide to Building Skills for Claude." This skill runs a multi-dimensional audit on any skill folder or SKILL.md and produces an actionable scorecard with specific fix recommendations.

## When to use

Run this skill whenever a user:
- Uploads or references a skill they want reviewed
- Asks "is this skill good?" or "check my skill"
- Wants to validate before publishing/distributing
- Is debugging triggering, execution, or quality issues
- Wants to improve an existing skill

## How it works

The review runs in three phases:
1. **Structural validation** — file naming, folder layout, YAML correctness
2. **Content quality audit** — description effectiveness, instruction clarity, progressive disclosure, patterns used
3. **Scorecard & recommendations** — graded rubric across all dimensions with prioritized fixes

---

## Phase 1: Structural Validation

Read the skill folder and check every item below. Report pass/fail for each.

### 1.1 File & Folder Naming

- [ ] Folder name uses kebab-case (e.g., `my-cool-skill`)
- [ ] No spaces in folder name
- [ ] No underscores in folder name
- [ ] No capital letters in folder name
- [ ] Folder name does NOT contain "claude" or "anthropic" (reserved)
- [ ] Main file is exactly `SKILL.md` (case-sensitive — not `skill.md`, `SKILL.MD`, etc.)
- [ ] No `README.md` inside the skill folder (all docs belong in SKILL.md or references/)

### 1.2 YAML Frontmatter

- [ ] Frontmatter is delimited by `---` on both the opening and closing lines
- [ ] `name` field is present
- [ ] `name` field uses kebab-case, no spaces, no capitals
- [ ] `name` field matches the folder name
- [ ] `description` field is present
- [ ] `description` is under 1024 characters
- [ ] No XML angle brackets (`<` or `>`) anywhere in frontmatter (security restriction)
- [ ] No unclosed quotes in YAML values
- [ ] Optional fields (if present) are valid:
  - `license`: recognized license identifier (e.g., MIT, Apache-2.0)
  - `compatibility`: 1–500 characters, describes environment requirements
  - `metadata`: valid key-value pairs (suggested: author, version, mcp-server)

### 1.3 Folder Structure

- [ ] Contains `SKILL.md` at root (required)
- [ ] Optional directories follow convention: `scripts/`, `references/`, `assets/`
- [ ] No unexpected top-level files that should be in subdirectories
- [ ] If `scripts/` exists, files are executable code (Python, Bash, etc.)
- [ ] If `references/` exists, files are documentation (.md, .txt, etc.)
- [ ] If `assets/` exists, files are templates, fonts, icons, etc.

---

## Phase 2: Content Quality Audit

### 2.1 Description Field (Critical — this is the primary triggering mechanism)

The description must answer two questions: **WHAT** the skill does and **WHEN** to use it.

**Check for:**
- [ ] Describes what the skill does (capability)
- [ ] Describes when to use it (trigger conditions / user phrases)
- [ ] Includes specific trigger phrases users would actually say
- [ ] Mentions relevant file types if applicable
- [ ] Is specific enough to avoid over-triggering on unrelated queries
- [ ] Is broad enough to trigger on paraphrased requests (not just one exact phrase)
- [ ] Includes negative triggers if there's risk of confusion with other skills (e.g., "Do NOT use for simple data exploration")

**Grade the description:**
- **Excellent**: Specific, actionable, includes 3+ trigger phrases, mentions file types, clear scope
- **Good**: Answers WHAT and WHEN, has trigger phrases, reasonable scope
- **Needs work**: Vague ("Helps with projects"), missing triggers, too generic, or too technical without user-facing language
- **Failing**: Missing entirely, one-word, or no trigger conditions

**Red flags:**
- "Helps with X" without specifying what the user would say
- Pure technical description with no user-facing trigger phrases
- Overloaded description trying to cover too many unrelated things

### 2.2 Progressive Disclosure

Skills should use a three-level loading system to minimize token usage:

- **Level 1 — YAML frontmatter** (~100 words): Always in context. Just enough for Claude to decide when to use it.
- **Level 2 — SKILL.md body** (<500 lines ideal): Loaded when the skill triggers. Contains full instructions.
- **Level 3 — Linked files** (references/, scripts/, assets/): Loaded only as needed.

**Check for:**
- [ ] SKILL.md body is under 500 lines (ideal) or has clear hierarchy with pointers if longer
- [ ] Detailed documentation is in `references/`, not inline in SKILL.md
- [ ] SKILL.md references external files clearly with guidance on WHEN to read them
- [ ] Large reference files (>300 lines) include a table of contents
- [ ] Domain-specific variants are organized into separate reference files (e.g., `references/aws.md`, `references/gcp.md`) rather than all inlined

**Grade:**
- **Excellent**: Clean separation across all three levels, SKILL.md is lean, references are well-organized
- **Good**: Reasonable separation, maybe a bit long but manageable
- **Needs work**: Everything crammed into SKILL.md, no use of references/
- **Failing**: SKILL.md is 1000+ lines with no external files, or instructions are buried and hard to find

### 2.3 Instruction Quality

**Check for clarity and actionability:**
- [ ] Instructions use imperative form ("Run X", "Check Y" — not "You might want to consider running X")
- [ ] Critical instructions appear at the top, not buried deep
- [ ] Steps are numbered and sequenced when order matters
- [ ] Specific commands/scripts are given, not vague ("validate the data" → "Run `python scripts/validate.py --input {filename}`")
- [ ] Error handling is included (what to do when things go wrong)
- [ ] Examples are provided for common scenarios
- [ ] Explains the **why** behind instructions, not just the **what** (this helps the model generalize)
- [ ] Avoids excessive ALWAYS/NEVER/MUST in all-caps (reframe as reasoning when possible)
- [ ] Output format is defined (template, structure, or example of expected result)

**Check for composability:**
- [ ] Skill works well alongside other skills (doesn't assume it's the only capability)
- [ ] No conflicts with common built-in Claude capabilities

**Check for portability:**
- [ ] Works across Claude.ai, Claude Code, and API without modification
- [ ] Any environment-specific dependencies are noted in `compatibility` field

### 2.4 Workflow Pattern Assessment

Identify which pattern(s) the skill uses and whether it applies them well:

**Pattern 1: Sequential Workflow Orchestration**
- Explicit step ordering with dependencies between steps
- Validation at each stage
- Rollback instructions for failures

**Pattern 2: Multi-MCP Coordination**
- Clear phase separation between different MCP services
- Data passing between MCPs is documented
- Validation before moving to next phase
- Centralized error handling

**Pattern 3: Iterative Refinement**
- Explicit quality criteria defined
- Validation scripts or checks between iterations
- Clear stopping criteria (when to stop iterating)

**Pattern 4: Context-Aware Tool Selection**
- Clear decision criteria for choosing between tools
- Fallback options documented
- Transparency about choices (tells user why a path was chosen)

**Pattern 5: Domain-Specific Intelligence**
- Domain expertise embedded in logic (not just tool access)
- Compliance/governance checks before action
- Comprehensive audit trail / documentation

**Grade the pattern usage:**
- **Excellent**: Pattern is clearly identified and well-executed, with validation gates and error handling
- **Good**: Pattern is present and functional, minor gaps
- **Needs work**: Pattern is implicit or incomplete
- **N/A**: Skill is simple enough that no formal pattern is needed

### 2.5 Use Case Definition

- [ ] 2–3 concrete use cases are identifiable from the skill
- [ ] Each use case has a clear trigger, steps, and expected result
- [ ] Edge cases are addressed
- [ ] Success criteria are defined (even if qualitative)

### 2.6 Category Classification

Classify the skill into one of the three standard categories:

1. **Document & Asset Creation** — consistent output (docs, presentations, code, designs)
2. **Workflow Automation** — multi-step processes with methodology
3. **MCP Enhancement** — workflow guidance on top of MCP tool access

Note: Skills can span categories. Identify the primary and any secondary categories.

---

## Phase 3: Scorecard & Recommendations

### Scoring Rubric

Score each dimension 1–5:

| Dimension | 1 (Failing) | 3 (Adequate) | 5 (Excellent) |
|---|---|---|---|
| **Structure** | Missing SKILL.md or broken YAML | Valid structure, minor issues | Perfect folder layout, all conventions followed |
| **Description** | Missing or vague | Answers WHAT and WHEN | Specific triggers, file types, negative triggers, pushiness |
| **Progressive Disclosure** | Everything in one giant file | Some separation | Clean 3-level hierarchy, lean SKILL.md |
| **Instruction Clarity** | Vague, no examples | Clear steps, some examples | Imperative, examples, error handling, explains WHY |
| **Error Handling** | None | Basic error messages | Comprehensive troubleshooting, rollback, common issues |
| **Composability** | Conflicts with other skills | Works in isolation | Explicitly designed for multi-skill environments |
| **Testing Readiness** | No testable outputs | Some verifiable outputs | Clear success criteria, assertions possible |

### Output Format

Present the results as:

```
# Skill Review: [skill-name]

## Overall Score: X/35 ([rating])

### Structural Validation
✅ / ❌ [each check with pass/fail]

### Content Quality
| Dimension | Score | Notes |
|---|---|---|
| Description | X/5 | [specific feedback] |
| Progressive Disclosure | X/5 | [specific feedback] |
| Instruction Clarity | X/5 | [specific feedback] |
| Error Handling | X/5 | [specific feedback] |
| Composability | X/5 | [specific feedback] |
| Testing Readiness | X/5 | [specific feedback] |

### Pattern Analysis
Primary pattern: [pattern name]
Pattern execution: [grade]

### Category
Primary: [category]
Secondary: [category, if applicable]

### Top 3 Fixes (Prioritized)
1. **[Priority: High/Medium/Low]** — [specific, actionable fix]
2. **[Priority: High/Medium/Low]** — [specific, actionable fix]
3. **[Priority: High/Medium/Low]** — [specific, actionable fix]

### Description Rewrite (if score < 4)
Suggested improved description:
[rewritten description]
```

### Rating Scale
- **30–35**: Production-ready. Minor polish only.
- **22–29**: Good foundation. Address the top fixes and it's ready.
- **15–21**: Needs significant work. Focus on structural and description issues first.
- **Below 15**: Fundamental rework needed. Start with the Fundamentals chapter of the guide.

---

## Quick-Check Mode

If the user just wants a fast pass (e.g., "quick check my skill"), skip the full audit and run only:

1. YAML frontmatter validation (all required fields, no forbidden content)
2. Description quality check (WHAT + WHEN + trigger phrases)
3. Top 3 issues with fixes

This should take under 2 minutes and give the user enough to act on immediately.

---

## Validation Script

If the skill folder is available on the filesystem, run the automated structural checks:

```bash
python scripts/validate_skill.py <path-to-skill-folder>
```

This script checks file naming, YAML parsing, folder structure, description length, and forbidden content. It outputs a JSON report that feeds into the scorecard.

---

## Troubleshooting Common Issues (Reference for Reviewer)

### Skill won't upload
- File not named exactly `SKILL.md`
- YAML missing `---` delimiters
- Unclosed quotes in YAML
- Name has spaces or capitals

### Skill doesn't trigger
- Description too generic ("Helps with projects")
- Missing trigger phrases
- Missing relevant file type mentions
- Test: Ask Claude "When would you use the [skill name] skill?" — if Claude can't answer clearly, the description needs work

### Skill triggers too often
- Add negative triggers ("Do NOT use for...")
- Be more specific about scope
- Clarify what adjacent skills handle instead

### Instructions not followed
- Instructions too verbose (keep SKILL.md lean)
- Critical instructions buried deep (move them up)
- Ambiguous language ("process appropriately" → give explicit steps)
- Missing explanation of WHY (model can't generalize without reasoning)
- Consider bundling validation scripts for critical checks (code is deterministic; language isn't)

### Performance/context issues
- SKILL.md over 500 lines without progressive disclosure
- Too many skills enabled simultaneously (>20–50)
- All content loaded inline instead of referenced
