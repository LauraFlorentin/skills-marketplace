---
description: Explore harness engineering theory — context engineering, Constitutional AI alignment, CLASS evaluation metrics, and anti-patterns. Optionally filter by topic.
argument-hint: "[context-engineering | alignment | evaluation | CLASS | anti-patterns]"
allowed-tools: Read, Glob, Grep
---

Use the harness-engineering skill to explore theory and research foundations.

Topic filter (if provided): $ARGUMENTS

Follow this workflow:

1. **Load the skill**: Read `skills/harness-engineering/SKILL.md` for the overview
2. **Route by topic** (if a topic filter was provided):
   - `context-engineering` → Read `skills/harness-engineering/references/context-engineering.md`
   - `alignment` → Read `skills/harness-engineering/references/alignment.md`
   - `evaluation` or `CLASS` → Read `skills/harness-engineering/references/evaluation-framework.md`
   - `anti-patterns` → Focus on the "Common Anti-Patterns to Avoid" section in SKILL.md
   - No filter → Summarize all three pillars with pointers to deep-dive references
3. **Connect to practice**: After presenting theory, explain which operational skill (`init`, `doctor`, `gc`, `onboard`) applies the concept and suggest running it if relevant
4. **Output**: Clear explanation with practical examples, linking theory to the user's specific context

If the user's question spans multiple topics, cover all relevant areas and show how they connect.
