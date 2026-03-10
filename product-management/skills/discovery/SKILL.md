---
name: discovery
description: User research, persona development, jobs-to-be-done mapping, and opportunity scoring for startup and enterprise PMs — guerrilla interviews, formal research plans, proto-personas, data-backed segmentation, JTBD frameworks, and Opportunity Solution Trees. Use when user asks to "run product discovery", "user research plan", "build personas", or mentions customer interviews, jobs-to-be-done, or opportunity scoring.
triggers:
  - user research
  - research plan
  - interview guide
  - persona
  - user persona
  - proto-persona
  - jobs to be done
  - JTBD
  - job stories
  - opportunity scoring
  - opportunity solution tree
  - customer discovery
  - user interviews
  - discovery
  - product discovery
  - customer research
  - affinity mapping
  - synthesis
---

# Product Discovery

## Disclaimer

Research outputs are hypotheses until validated with real users. Always test assumptions with actual customer behavior, not just stated preferences.

## User Research

User research is how you replace opinions with evidence. Every product decision -- what to build, who to build it for, how it should work -- is better when informed by direct contact with real users. The biggest risk in product development is not building the wrong thing; it is building the wrong thing confidently because nobody talked to a customer.

The depth of research should match your stage. A startup with 0 customers needs fast, scrappy signal. An enterprise team with 50,000 users needs rigorous, statistically defensible insights. Both approaches produce valid evidence if executed well.

### Startup Mode: Guerrilla Research

For early-stage products with limited budget and no dedicated research team, guerrilla research gives you actionable insights in days, not months. The goal is speed and directional accuracy -- you are not publishing a peer-reviewed paper; you are reducing the risk of building something nobody wants.

**Intercept Interviews:**

Go where your target users already are. Do not wait for them to come to you.

- **Coffee shops and co-working spaces:** Approach people who match your target profile. "I'm building a product for [role/situation] -- would you mind answering 3 quick questions? It will take under 5 minutes." Offer to buy their coffee. Success rate: roughly 1 in 3 people say yes.
- **Online communities:** Reddit, Slack groups, Discord servers, niche forums, LinkedIn groups. Post a genuine question about their workflow or pain point -- not a survey link. Engage in the thread. DM people who share relevant experiences. Be transparent that you are building a product.
- **Industry events and meetups:** Attend events your target users attend. The hallway conversations and after-parties are more valuable than the talks. Prepare 3-5 open-ended questions in advance.

**Unmoderated Surveys:**

Use Typeform, Google Forms, or Tally to collect structured data at scale. Keep surveys under 10 questions -- completion rates drop sharply after question 10. Rules for effective surveys:

1. Start with a screener question to filter out non-target respondents.
2. Use a mix of multiple-choice (for quantitative signal) and open-text (for qualitative depth).
3. Avoid leading questions. "How frustrated are you with X?" assumes they are frustrated. Instead: "How would you describe your experience with X?"
4. Include one "magic wand" question: "If you could change one thing about how you [task], what would it be?"
5. Distribute through channels where your target users are active. Response rates from cold email are typically 2-5%; from engaged communities, 15-30%.

**5-User Tests:**

Jakob Nielsen's research demonstrates that 5 users find approximately 85% of usability issues. You do not need 50 users for a usability test. Run a quick test with 5 people, fix the major issues, then test again with 5 more if needed.

- **Format:** 15-30 minute sessions. Give users a task ("Sign up and create your first project"). Observe silently. Ask them to think aloud.
- **Recording:** Use Loom for remote async tests (send users a link; they record their screen and voice). Use Hotjar or FullStory for session recording on live products (no scheduling required -- watch real users navigate your product).
- **Analysis:** After 5 sessions, you will see clear patterns. List every point where users hesitated, expressed confusion, or failed to complete the task. Prioritize fixes by severity: Can't complete task > Completes with difficulty > Minor friction.

**1-Week Research Sprint Protocol:**

Use this when you need to go from zero insight to actionable findings in 5 business days.

| Day | Activity | Output |
|---|---|---|
| **Monday** | Define research question. Write 5-7 interview questions. Identify 8-10 target participants (recruit more than you need -- expect 30-40% no-shows). | Research brief (1 page), interview guide, participant list |
| **Tuesday** | Conduct 3-4 intercept or scheduled interviews (30 min each). Record with consent. Take rough notes during, detailed notes immediately after. | Raw interview notes, recordings |
| **Wednesday** | Conduct 3-4 more interviews. Launch a short unmoderated survey (5-7 questions) to triangulate interview findings with broader data. | Raw interview notes, survey live |
| **Thursday** | Synthesize findings. Affinity-map key observations (see Synthesis Methods below). Write insight statements. Close survey and analyze responses. | Affinity map, 3-5 insight statements |
| **Friday** | Create a 1-page findings summary. Present to team (15-30 min). Decide on next actions. | Findings summary, decision log |

**Tools on a budget:** Google Meet or Zoom for remote interviews (free tier), Google Forms or Tally for surveys (free), Loom for async recording (free for 25 videos), Miro or FigJam for affinity mapping (free tiers available), Notion or Google Docs for research repository (free).

### Enterprise Mode: Formal Research

For products with established user bases, dedicated budgets, and stakeholders who require methodological rigor, formal research provides the defensible evidence needed to drive organizational decision-making.

**Research Plan Template:**

Every formal research initiative should start with a research plan approved by stakeholders before fieldwork begins. This prevents scope creep, misaligned expectations, and wasted budget.

```
RESEARCH PLAN
==============
Project: _______________
Date: _______________
Researcher: _______________
Sponsor/Stakeholder: _______________

1. OBJECTIVE
   What specific question(s) are we trying to answer?
   - Primary:
   - Secondary:

2. BACKGROUND
   What do we already know? What triggered this research?
   [2-3 sentences of context]

3. METHODOLOGY
   [ ] Moderated 1:1 interviews (N = ___)
   [ ] Unmoderated usability testing (N = ___)
   [ ] Survey (N = ___)
   [ ] Diary study (N = ___, duration: ___ days)
   [ ] Contextual inquiry / field observation (N = ___)
   [ ] Card sort / tree test (N = ___)
   Justification for chosen method:

4. PARTICIPANT CRITERIA
   Target profile:
   Screener questions:
   Recruiting source:
   Incentive: $___

5. TIMELINE
   | Phase | Dates | Deliverable |
   |-------|-------|-------------|
   | Planning & recruiting | Week 1-2 | Screener, guide, participants confirmed |
   | Fieldwork | Week 3-4 | Raw data collected |
   | Analysis | Week 5 | Coded data, themes identified |
   | Readout | Week 6 | Findings deck, recommendations |

6. BUDGET
   | Item | Cost |
   |------|------|
   | Participant incentives (N x $___) | $___ |
   | Recruiting fees | $___ |
   | Tools / software | $___ |
   | Total | $___ |

7. DELIVERABLES
   - [ ] Executive summary (1 page)
   - [ ] Full findings report
   - [ ] Video highlight reel (5-10 min)
   - [ ] Recommendation matrix (prioritized actions)

8. RISKS AND LIMITATIONS
   - [e.g., "Recruiting may skew toward power users"]
   - [e.g., "Self-reported data may not reflect actual behavior"]
```

**Recruiting Criteria Template:**

Careful recruiting is the difference between useful research and misleading data. Recruit participants who represent your actual or target user base, not just people who are easy to find.

```
PARTICIPANT SCREENER
=====================
Study: _______________
Target N: ___ participants

DEMOGRAPHICS:
- Age range: ___
- Location: ___
- Job title / role: ___
- Company size: ___
- Industry: ___

BEHAVIORAL CRITERIA:
- Frequency of [relevant behavior]: ___
- Current tools used for [task]: ___
- Experience level with [domain]: ___
- Recency of [relevant experience]: ___

SCREENING QUESTIONS:
1. [Question to verify they match the target profile]
   PASS: [acceptable answers]
   FAIL: [disqualifying answers]
2. [Question to assess relevant experience]
   PASS:
   FAIL:
3. [Question to check for bias/conflict]
   PASS:
   FAIL:

EXCLUSION CRITERIA:
- Employees of competitors
- Participants in a study within the last [6 months]
- Professional research participants ("panelists")
- [Other relevant exclusions]

INCENTIVE: $___  |  Format: [gift card / bank transfer / donation]
```

**Moderated 1:1 Interview Protocol (60 Minutes):**

This is the gold standard for qualitative research. One researcher, one participant, a structured conversation that uncovers motivations, behaviors, and unmet needs.

| Phase | Duration | Purpose | Activities |
|---|---|---|---|
| **Introduction** | 5 min | Build rapport, set expectations, get consent | Introduce yourself and the purpose. Explain there are no wrong answers. Ask permission to record. Have them sign consent form if required. |
| **Context** | 10 min | Understand their world | Ask about their role, responsibilities, typical day. "Tell me about your role and what a typical week looks like." Establish the context before diving into specifics. |
| **Exploration** | 30 min | Discover behaviors, motivations, pain points | Use open-ended questions (see Interview Guide below). Follow the participant's lead. Probe interesting threads with "Tell me more about that" and "Why?" |
| **Deep Dive** | 10 min | Explore specific scenarios in detail | Ask them to walk through a specific recent experience step by step. "Can you show me how you did that?" Ask about workarounds, frustrations, and what they wish existed. |
| **Wrap-up** | 5 min | Close gracefully, capture final thoughts | "Is there anything I should have asked but didn't?" "What's the one thing you'd want us to know?" Thank them, explain next steps, provide incentive. |

**Research Repository Structure:**

As research accumulates, it must be organized, searchable, and accessible to the entire product team. A research repository prevents redundant studies and enables teams to build on past findings.

```
/research-repository
  /[year]
    /[project-name]
      /plan.md           -- Research plan
      /screener.md       -- Recruiting criteria
      /guide.md          -- Interview guide
      /raw-data/         -- Transcripts, recordings, survey exports
      /analysis/         -- Affinity maps, coded data
      /findings.md       -- Final report
      /highlight-reel/   -- Video clips (2-3 min each)
  /tags/                 -- Cross-project tag index
    onboarding.md        -- Links to all studies touching onboarding
    pricing.md           -- Links to all studies touching pricing
    enterprise.md        -- Links to all studies with enterprise users
  /insights-library.md   -- Running log of validated insight statements
```

**Tag taxonomy:** Create a shared set of tags (15-25 tags is usually sufficient) that span product areas, user types, and themes. Apply tags consistently across projects. Review and prune the taxonomy quarterly.

**Stakeholder Readout Format:**

Research findings must be communicated in a format that drives action. A 60-page report that no one reads is worse than no research at all.

```
RESEARCH READOUT
=================
Study: _______________
Date: _______________
Researcher: _______________
Audience: _______________

EXECUTIVE SUMMARY (1 page max):
[3-4 sentences: What we studied, what we found, what it means]

KEY FINDINGS (3-5 findings):
Finding 1: [Statement]
  Evidence: [What we observed / data points]
  Frequency: [How many participants / what % of survey]
  Confidence: [High / Medium / Low]

Finding 2: [Statement]
  Evidence:
  Frequency:
  Confidence:

[... repeat for each finding]

IMPLICATIONS:
| Finding | Implication for Product | Implication for Design | Implication for GTM |
|---------|------------------------|----------------------|---------------------|
|         |                        |                      |                     |

RECOMMENDED ACTIONS:
| Action | Priority (H/M/L) | Owner | Timeline |
|--------|-------------------|-------|----------|
|        |                   |       |          |

OPEN QUESTIONS:
- [Questions this research raised but did not answer]
- [Suggested follow-up studies]

APPENDIX:
- Methodology details
- Participant demographics
- Full data tables
```

### Interview Guide Template

A well-structured interview guide ensures consistency across sessions while leaving room for natural conversation. Never read questions verbatim -- use them as a compass, not a script.

**Opening (5 minutes):**

Build rapport, set expectations, and get consent.

- "Thanks for taking the time to talk with us today. I'm [name], and I work on [product/team]. We're trying to understand how people like you [broad problem area] so we can make better decisions about what to build."
- "There are no right or wrong answers -- we're here to learn from your experience. If I ask something that doesn't make sense, just say so."
- "Is it okay if I record this session? The recording is just for our team's notes -- it won't be shared publicly."

**Exploration (30 minutes):**

Use open-ended questions that invite stories, not yes/no answers.

**10 Sample Questions:**

1. "Tell me about the last time you [relevant task/activity]. Walk me through what happened from start to finish."
2. "What's the hardest part of [relevant workflow] for you right now?"
3. "How do you currently handle [problem]? Walk me through your process step by step."
4. "When you think about [problem area], what frustrates you the most?"
5. "Can you show me how you do [task] today? I'd love to see your actual setup."
6. "What would happen if you couldn't do [task] at all? What would break?"
7. "Tell me about a time when [relevant process] went really well. What made it work?"
8. "Tell me about a time when [relevant process] went badly. What went wrong?"
9. "If you had a magic wand and could change one thing about how you [task], what would it be?"
10. "Who else is involved in [process]? How do you collaborate with them on this?"

**Deep Dive (10 minutes):**

When a participant mentions something interesting, go deeper.

- "You mentioned [specific thing]. Tell me more about that."
- "Why is that important to you?"
- "Can you show me an example?"
- "What did you try before you found that approach?"
- "How often does that happen?"
- "What would it mean for you if that problem went away?"

**Closing (5 minutes):**

- "Is there anything I should have asked you about but didn't?"
- "What's the one thing you'd want someone building a product in this space to know?"
- "Would it be okay if we followed up with you later if we have additional questions?"
- Thank the participant. Provide incentive. Explain next steps.

### Synthesis Methods

Raw research data is not insight. Synthesis is the process of transforming observations into actionable understanding. Do not skip this step -- it is where the real value is created.

**Affinity Mapping:**

Affinity mapping is the most widely used synthesis method. It works for any qualitative data: interview notes, survey responses, support tickets, usability observations.

1. **Extract observations.** Go through each interview or data source. Write one observation per sticky note (physical or digital). Be specific and behavioral: "P3 spent 4 minutes looking for the export button" -- not "Users find export confusing."
2. **Cluster into groups.** Spread all sticky notes on a wall or Miro board. Silently (no discussion) move notes that seem related into clusters. Do not name the clusters yet.
3. **Name the clusters.** Once clusters stabilize, give each a descriptive label. The label should capture the theme, not just summarize the notes. "Users build workarounds because they don't trust the system's calculations" -- not "Workarounds."
4. **Identify hierarchy.** Some clusters are sub-themes of larger themes. Arrange them into a hierarchy: 3-5 top-level themes, each with 2-4 sub-themes.
5. **Prioritize.** Mark themes by frequency (how many participants mentioned it) and intensity (how strongly they felt about it). High frequency + high intensity = top priority finding.

**Thematic Coding:**

For rigorous, repeatable analysis -- especially when working with transcripts from 10+ interviews.

1. **Create a codebook.** Define 15-30 codes based on your research questions and initial review of the data. Example codes: "pain-point-manual-process," "workaround-spreadsheet," "desire-automation," "trust-issue."
2. **Code each transcript.** Read through each transcript and tag relevant passages with codes. One passage can have multiple codes. Use a tool like Dovetail, Notion, or even a spreadsheet.
3. **Merge and refine codes.** After coding 3-4 transcripts, review your codebook. Merge codes that overlap. Split codes that are too broad. Add new codes for unexpected themes.
4. **Analyze code frequency.** Count how many participants each code appears for (not total occurrences -- one participant mentioning something 10 times is still one data point). Codes mentioned by 60%+ of participants are strong themes.
5. **Write theme summaries.** For each major theme, write a 2-3 sentence summary with supporting evidence.

**Insight Statement Formula:**

Transform observations into actionable insight statements using this structure:

> "We observed **[behavior]** because **[motivation]**, which means **[implication]**."

**Worked Example:**

Observations from 8 interviews with mid-market product managers:

- P1, P3, P5, P7 all maintain a separate spreadsheet to track feature requests alongside their project management tool.
- P2 and P6 copy-paste customer quotes from Slack into a Google Doc weekly.
- P4 and P8 have asked their engineering team to build internal dashboards to aggregate feedback.

Cluster: "Users build parallel tracking systems outside the product."

Insight statement:

> "We observed that **6 out of 8 product managers maintain a separate system (spreadsheets, docs, or internal tools) to track customer feedback**, because **their primary PM tool doesn't connect feedback to roadmap items in a way they trust for prioritization decisions**, which means **there is a significant opportunity to build integrated feedback-to-roadmap workflows that eliminate the need for manual aggregation**."

This insight is specific (6 of 8), explains the motivation (trust gap), and points to a clear product opportunity (integrated workflows).

### Research Anti-Patterns

These are the most common ways research goes wrong. Watch for them in your own work and when reviewing others' research.

- **Leading questions.** "Don't you think the dashboard is confusing?" leads the participant to agree. Instead: "Tell me about your experience using the dashboard." Let them tell you whether it is confusing without planting the idea. A leading question invalidates the response.
- **Confirmation bias.** You have a hypothesis and unconsciously steer the conversation to confirm it. You over-weight evidence that supports your belief and dismiss evidence that contradicts it. Counter this by actively looking for disconfirming evidence. Ask a colleague to review your analysis independently. Present findings to someone who holds the opposite hypothesis and see if your evidence convinces them.
- **Small sample rationalization.** "All 3 users we talked to said they want this feature" is not statistically meaningful. 3 users can reveal patterns worth investigating, but they cannot validate demand. Be honest about confidence levels. Say "early signal from 3 conversations" -- not "users want this."
- **Not recording.** If you rely on notes alone, you will miss nuance, misremember details, and project your own interpretation onto what was said. Record every session (with consent). Even if you never re-watch the full recording, having it available resolves disputes about what a participant actually said.
- **Analyzing during interviews.** Do not form conclusions while you are still collecting data. It biases your remaining interviews. During the interview, focus on listening and following threads. Write down hypotheses after each session, but wait until all sessions are complete before synthesizing themes. Your interpretation after interview 3 will often be contradicted by interview 7.
- **Asking about future behavior.** "Would you use a feature that does X?" is unreliable. People are poor predictors of their own future behavior. Instead, ask about past behavior: "Tell me about the last time you tried to [task]. What did you do?" Past behavior is the best predictor of future behavior.
- **Treating research as validation.** Research should inform decisions, not rubber-stamp them. If you only conduct research to confirm what you have already decided to build, you are wasting time and creating false confidence. Be willing to let research change your mind.

---

---

## References

For detailed templates, frameworks, and field-level guidance, read:

- [`references/discovery-reference.md`](references/discovery-reference.md) — Complete framework details, templates, and examples

Read this file when the task requires:
- Personas
- Jobs-to-Be-Done
- Opportunity Scoring
- Output Formats

