# Discovery — Detailed Reference

Detailed frameworks, templates, and field-level guidance. Read when SKILL.md directs you here.

---

## Personas

Personas are fictional characters based on real data that represent distinct segments of your user base. They exist to create shared understanding across a team about who you are building for. A good persona makes design and prioritization decisions easier because you can ask: "Would [persona name] need this? Would they understand this?"

Personas become dangerous when they are treated as truth rather than hypotheses, when they are created once and never updated, or when they become stereotypes rather than research-based archetypes.

### Startup Mode: Proto-Personas

For early-stage products with fewer than 50 users, formal data-backed personas are premature. You do not have enough data. Instead, build proto-personas: lightweight, hypothesis-driven profiles based on founder intuition and early conversations. The key difference is that proto-personas are explicitly labeled as assumptions to be validated.

**Proto-Persona Template:**

```
PROTO-PERSONA
==============
Status: HYPOTHESIS -- validate by [date, within 30 days]

Name: _______________
Photo: [placeholder image or avatar]
Role / Title: _______________

DEMOGRAPHICS:
- Age range: ___
- Location: ___
- Tech savviness: [Low / Medium / High]
- Company size: ___

GOALS (top 3):
1.
2.
3.

FRUSTRATIONS (top 3):
1.
2.
3.

TOOLS THEY USE TODAY:
- [Tool 1] for [purpose]
- [Tool 2] for [purpose]
- [Tool 3] for [purpose]

REPRESENTATIVE QUOTE:
"[One sentence that captures how they describe their problem or need]"

HOW THEY'D DESCRIBE THE PROBLEM:
[2-3 sentences in their own language -- not product jargon]

VALIDATION STATUS:
- [ ] Based on at least 5 conversations with real people
- [ ] Goals confirmed through behavioral evidence (not just stated)
- [ ] Frustrations observed directly (not assumed)
- [ ] Reviewed and updated within 30 days of creation
```

**How to build proto-personas:**

1. Start with founder intuition. Write down who you think your users are. Be specific.
2. Conduct 5-10 conversations with people who match the profile. Adjust the persona based on what you learn.
3. Create 2-3 proto-personas maximum. If you have more than 3 at the early stage, you have not narrowed your focus enough.
4. Label them clearly as hypotheses. Print "HYPOTHESIS" at the top in bold. Set a 30-day validation deadline.
5. Validate or kill within 30 days. After 30 days, either upgrade the persona with real data or retire it if the segment does not exist as you imagined.

**Worked Example:**

```
PROTO-PERSONA
==============
Status: HYPOTHESIS -- validate by April 15, 2026

Name: Startup Sara
Photo: [avatar]
Role / Title: Head of Product at a Series A B2B SaaS startup

DEMOGRAPHICS:
- Age range: 28-35
- Location: US, remote-first
- Tech savviness: High
- Company size: 15-40 employees

GOALS (top 3):
1. Decide which features to build next based on data, not gut feeling
2. Keep engineering focused on the highest-impact work
3. Demonstrate to the CEO and board that product decisions are evidence-based

FRUSTRATIONS (top 3):
1. Spends 6+ hours/week manually reviewing sales call notes and
   support tickets to identify patterns
2. Engineering pushes back on priorities because the rationale
   feels subjective
3. Has tried 3 PM tools but none connect customer feedback
   directly to roadmap decisions

TOOLS THEY USE TODAY:
- Linear for issue tracking
- Notion for roadmap and specs
- Slack for internal communication (and ad-hoc customer feedback)
- Google Sheets for manual feedback tracking

REPRESENTATIVE QUOTE:
"I know our customers are telling us what to build -- I just can't
find it fast enough across all the places they tell us."

HOW THEY'D DESCRIBE THE PROBLEM:
"I'm drowning in qualitative data. Every sales call, every support
ticket, every Slack message has signal, but I don't have a way to
aggregate and prioritize it. So I end up going with my gut and then
second-guessing myself."

VALIDATION STATUS:
- [x] Based on at least 5 conversations with real people
- [x] Goals confirmed through behavioral evidence
- [ ] Frustrations observed directly -- need 2 more data points
- [ ] Reviewed and updated within 30 days of creation
```

### Enterprise Mode: Data-Backed Personas

For products with established user bases (500+ users), personas should be grounded in quantitative data and validated through ongoing measurement. These personas are living documents that evolve as your user base changes.

**Demographic Data Sources:**

| Source | What It Reveals | How to Access |
|---|---|---|
| CRM (Salesforce, HubSpot) | Job titles, company size, industry, deal size, engagement history | Export and analyze customer fields |
| Product analytics (Amplitude, Mixpanel) | Feature usage patterns, session frequency, workflow paths | Behavioral cohort analysis |
| Support tickets (Zendesk, Intercom) | Common problems by segment, satisfaction by segment | Tag analysis and sentiment scoring |
| Surveys (annual, NPS, onboarding) | Self-reported needs, satisfaction, demographics | Cross-tabulate responses by segment |
| Sales call recordings (Gong, Chorus) | Buying motivations, objections, competitive mentions | Theme analysis across calls |

**Behavioral Segmentation Methodology:**

Segment users by what they do, not who they are. Demographics (job title, company size) are proxies for behavior, but they are often inaccurate proxies. Two "Product Managers at mid-market SaaS companies" may use your product in completely different ways.

1. **Identify key behavioral dimensions.** Examples: frequency of use (daily vs. weekly), primary workflow (analytics vs. planning vs. collaboration), breadth of feature adoption (power user vs. single-feature user), team size (solo vs. team of 10+).
2. **Pull behavioral data.** Export usage data from your analytics platform. Include: login frequency, features used, session duration, collaboration patterns, time since first use.
3. **Cluster analysis.** Use k-means clustering or manual segmentation to group users by behavioral similarity. Start with 3-5 clusters. Test whether adding more clusters reveals meaningful distinctions.
4. **Profile each cluster.** For each behavioral cluster, pull demographic overlays (job title, company size, industry). Name the cluster based on its dominant behavior pattern, not demographics.
5. **Validate with qualitative research.** Interview 5-8 users from each cluster. Do they recognize themselves in the persona? Does the persona accurately describe their goals and frustrations?

**Data-Backed Persona Template:**

```
DATA-BACKED PERSONA
=====================
Name: _______________
Last updated: _______________
Next review: _______________ (quarterly)

SEGMENT SIZE:
- % of total user base: ___%
- Approximate user count: ___
- Revenue contribution: ___%

DEMOGRAPHIC PROFILE:
- Most common job titles: ___
- Company size range: ___
- Industry verticals: ___
- Geography: ___

BEHAVIORAL PROFILE:
- Login frequency: ___
- Primary workflow: ___
- Features used most: ___
- Features never used: ___
- Average session duration: ___
- Collaboration pattern: [solo / small team / cross-functional]

GOALS (ranked by frequency in research):
1. [Goal] -- mentioned by __% of segment
2. [Goal] -- mentioned by __% of segment
3. [Goal] -- mentioned by __% of segment

FRUSTRATIONS (ranked by intensity):
1. [Frustration] -- severity: [High/Med/Low]
2. [Frustration] -- severity: [High/Med/Low]
3. [Frustration] -- severity: [High/Med/Low]

CORE JOBS TO BE DONE:
- [Job statement 1 -- see JTBD section]
- [Job statement 2]
- [Job statement 3]

KEY METRICS FOR THIS PERSONA:
- NPS: ___
- Retention rate (12-month): ___%
- Feature adoption score: ___/10
- Support ticket frequency: ___ per month
- Expansion revenue rate: ___%

REPRESENTATIVE QUOTES (from research):
- "[Quote 1]" -- [Source: interview/survey/support ticket]
- "[Quote 2]" -- [Source]
- "[Quote 3]" -- [Source]

JOURNEY MAP SUMMARY:
- Awareness: [How they find us]
- Evaluation: [What they compare us against]
- Adoption: [First value moment]
- Retention: [What keeps them]
- Expansion: [What triggers upgrades]
- Churn risk: [Warning signals]

VALIDATION STATUS:
- Data sources: [list]
- Last qualitative validation: [date]
- Confidence level: [High / Medium / Low]
```

**Persona Validation Metrics:**

Personas are only useful if they accurately represent real users. Measure persona quality with these metrics and review quarterly:

| Metric | What It Tells You | Target |
|---|---|---|
| % of user base represented | Do your personas cover most of your users? | 80%+ of users should map to a persona |
| NPS by persona | Are different personas having different experiences? | Variance across personas reveals segment-specific issues |
| Feature usage by persona | Are personas using the product differently? | Distinct usage patterns confirm personas are real segments |
| Retention by persona | Which personas stay and which churn? | Identifies which segments you serve well and which you don't |
| Revenue per persona | Which personas drive the most revenue? | Informs prioritization of which persona to optimize for |

**Review Cadence:**

- **Quarterly:** Refresh behavioral data. Update segment sizes and metrics. Check if behavioral clusters have shifted.
- **Annually:** Full persona rebuild. Re-run clustering analysis. Conduct fresh qualitative interviews. Retire personas that no longer represent significant segments. Create new personas for emerging segments.

### Persona Quality Checklist

Before sharing a persona with the team, validate it against these criteria:

- [ ] **Based on real data?** Proto-personas require at least 5 conversations. Data-backed personas require quantitative behavioral data + qualitative validation. If a persona is based purely on assumptions, label it as a hypothesis.
- [ ] **Actionable for design decisions?** Can a designer or engineer read this persona and make a better product decision? If the persona does not change any decision, it is too generic.
- [ ] **Distinct from each other?** If two personas would make the same product choices, merge them. Each persona should lead to at least one different design decision.
- [ ] **Named and referenced in team conversations?** A persona that exists only in a document is useless. The team should use persona names in meetings: "How would Sara handle this?" If nobody references the persona, it is not earning its place.

### When NOT to Use Personas

Personas are a tool, not a religion. There are situations where they do more harm than good.

- **When you have fewer than 20 users.** You do not need a fictional representation of your users -- you can talk to the actual humans. Maintain a list of your users, talk to them directly, and build relationships. Personas are a necessary abstraction for scale; at 15 users, the abstraction adds complexity without value.
- **When personas become stereotypes.** "Marketing Mary is 35, drinks oat milk lattes, and loves Instagram" is a stereotype, not a persona. If the demographic details do not drive different product decisions, remove them. A persona should describe behaviors, goals, and pain points -- not lifestyle choices.
- **When they are created but never referenced.** If your team created personas 6 months ago and nobody has mentioned them since, they failed. Either the personas are too generic to be useful, they don't reflect reality, or the team doesn't believe in them. Diagnose the root cause before creating new personas.
- **When they prevent direct user contact.** Personas should supplement user research, not replace it. If a PM says "I don't need to talk to users because I have personas," the personas are being misused. Personas summarize what you have learned; they do not eliminate the need to keep learning.

---

## Jobs-to-Be-Done

Jobs-to-be-Done (JTBD) is a framework that shifts focus from who the user is to what the user is trying to accomplish. People don't buy products -- they "hire" products to do a job. Understanding the job is more stable and actionable than understanding demographics, because jobs persist even as technology, market conditions, and user profiles change.

The classic example: People don't buy a quarter-inch drill because they want a drill. They buy it because they want a quarter-inch hole. And they don't want a hole -- they want to hang a shelf. And they don't want a shelf -- they want their books organized and accessible. The deeper you understand the job, the better your product can serve it.

### Job Statement Format

Every job should be expressed as a structured statement that captures context, motivation, and desired outcome:

> "When I **[situation/context]**, I want to **[motivation/action]**, so I can **[expected outcome/benefit]**."

**Examples:**

- "When I **receive a new feature request from a customer**, I want to **quickly assess whether it aligns with our roadmap priorities**, so I can **give the sales team a definitive answer within 24 hours**."
- "When I **prepare for a quarterly board meeting**, I want to **show which product investments drove measurable business outcomes**, so I can **maintain the board's confidence in our product strategy**."
- "When I **onboard a new team member**, I want to **get them productive on our tools within their first week**, so I can **minimize the productivity dip that comes with new hires**."

### Job Types

Every job has three dimensions. Most products focus only on functional jobs, but emotional and social jobs often drive purchasing decisions more powerfully.

**Functional Jobs:** The practical task the user is trying to accomplish. This is the most visible and easiest to identify. "Organize my customer feedback," "Generate a monthly report," "Schedule a meeting across time zones."

**Emotional Jobs:** How the user wants to feel during and after doing the job. "Feel confident that I'm making the right prioritization decision," "Feel in control of a complex project," "Reduce anxiety about missing critical customer signals." Emotional jobs explain why users pay premium prices for products that are functionally equivalent to cheaper alternatives.

**Social Jobs:** How the user wants to be perceived by others. "Be seen as a data-driven decision maker by my leadership team," "Demonstrate to my team that I've considered their input," "Look prepared and credible in board presentations." Social jobs explain why enterprise buyers care about brand names, certifications, and analyst endorsements.

### Job Map (8 Stages)

A job map breaks any core job into 8 universal stages. For each stage, identify what the user is trying to do, where they struggle, and where opportunities exist.

| Stage | What the User Does | Pain Points to Identify | Opportunity Questions |
|---|---|---|---|
| **1. Define** | Determine what needs to be done; clarify objectives | Ambiguity about goals, conflicting priorities, unclear scope | How might we help users clarify what they need to accomplish? |
| **2. Locate** | Gather inputs, data, tools, and resources needed | Can't find information, data scattered across tools, missing inputs | How might we bring needed inputs together in one place? |
| **3. Prepare** | Set up the environment, organize inputs, plan the approach | Setup is time-consuming, complex configuration, steep learning curve | How might we reduce setup time and complexity? |
| **4. Confirm** | Verify readiness before executing -- right inputs, right conditions | Uncertainty about whether setup is correct, fear of wasted effort | How might we give users confidence that they're ready? |
| **5. Execute** | Perform the core task | Errors, inefficiency, manual steps that could be automated, context switching | How might we make execution faster, easier, or more reliable? |
| **6. Monitor** | Track progress and results during execution | Lack of visibility into status, no alerts for problems, delayed feedback | How might we provide real-time visibility into progress? |
| **7. Modify** | Make adjustments based on monitoring | Difficult to change course, rigid workflows, cascading changes | How might we make it easy to adjust without starting over? |
| **8. Conclude** | Finish up, deliver results, clean up, archive | No clear endpoint, results hard to share, no audit trail | How might we make it easy to wrap up and share results? |

**How to use the job map:** Pick a core job your product addresses. Walk through all 8 stages from the user's perspective. For each stage, document: (1) what the user does today, (2) what tools they use, (3) what pain points they experience, (4) what the ideal experience looks like. The biggest gaps between current and ideal are your product opportunities.

### Startup Mode: Quick Job Stories

For early-stage products, a full JTBD analysis is overkill. Instead, identify 3-5 core functional jobs through 5-10 customer conversations and write them as job stories.

**Process:**

1. **Conduct 5-10 conversations** (15-20 minutes each) focused on understanding how people currently handle the problem your product addresses.
2. **Listen for jobs.** Pay attention to verbs: "I need to...", "I'm trying to...", "Every week I have to..." Each of these is a job.
3. **Write 3-5 job stories** using the standard format.
4. **Prioritize by frequency and intensity.** For each job, rate:
   - **Frequency:** How often does the user perform this job? (Daily / Weekly / Monthly / Quarterly)
   - **Intensity of pain:** How painful is the current approach? (1 = minor annoyance, 5 = significant time/money/emotional cost)
   - **Priority score:** Frequency rank * Intensity. Highest scores = best opportunities.

**Job Story Template:**

```
JOB STORY
==========
Job #: ___

Job Statement:
When I [situation/context],
I want to [motivation/action],
so I can [expected outcome/benefit].

Job Type: [Functional / Emotional / Social]

Frequency: [Daily / Weekly / Monthly / Quarterly]
Intensity of pain (1-5): ___
Priority score: ___

Current approach:
[How the user handles this job today, step by step]

Biggest pain point in current approach:
[The single most frustrating or time-consuming part]

Evidence:
- [P1: "direct quote about this job"]
- [P3: "direct quote about this job"]
- [Mentioned by ___ of ___ participants]
```

### Enterprise Mode: Full JTBD Framework

For mature products, use Tony Ulwick's Outcome-Driven Innovation (ODI) methodology to systematically identify under-served outcomes and prioritize product investment.

**Step 1: Define the core job.** Work with customers to define the core functional job at the right level of abstraction. Too broad: "Manage my business." Too narrow: "Export a CSV report." Right level: "Evaluate whether a feature request should be added to the roadmap."

**Step 2: List desired outcomes.** For the core job, list 50-100 desired outcomes. Desired outcomes are the metrics customers use (implicitly or explicitly) to judge how well a solution performs the job. Format: **[Direction of improvement] + [metric] + [context].**

Examples:
- Minimize the time it takes to assess the business impact of a feature request.
- Minimize the likelihood of prioritizing a feature that customers won't actually adopt.
- Increase the accuracy of effort estimates for proposed features.
- Minimize the number of data sources that must be consulted to make a prioritization decision.

**Step 3: Survey customers.** For each desired outcome, ask customers to rate:
- **Importance (1-5):** How important is this outcome to you when performing the job?
- **Satisfaction (1-5):** How satisfied are you with your current ability to achieve this outcome?

Survey 100+ customers for statistically meaningful results. Segment responses by persona if applicable.

**Step 4: Calculate opportunity score.**

> **Opportunity Score = Importance + max(Importance - Satisfaction, 0)**

This formula identifies outcomes that are highly important but poorly satisfied. The max function ensures that over-satisfied outcomes do not get negative scores.

| Outcome | Importance | Satisfaction | Opportunity Score |
|---|---|---|---|
| Minimize time to assess business impact of a feature request | 4.5 | 2.0 | 4.5 + max(4.5 - 2.0, 0) = **7.0** |
| Minimize likelihood of prioritizing low-adoption features | 4.8 | 1.5 | 4.8 + max(4.8 - 1.5, 0) = **8.1** |
| Increase accuracy of effort estimates | 3.5 | 3.0 | 3.5 + max(3.5 - 3.0, 0) = **4.0** |
| Minimize number of data sources consulted | 3.0 | 4.0 | 3.0 + max(3.0 - 4.0, 0) = **3.0** |

**Step 5: Classify outcomes.**

| Category | Criteria | Interpretation |
|---|---|---|
| **Under-served** | High importance, low satisfaction (Opportunity Score > 6) | Build here. Customers care deeply and current solutions fail them. |
| **Over-served** | Low importance, high satisfaction (Opportunity Score < 4) | Do not invest further. Current solutions exceed expectations. Consider cost reduction. |
| **Appropriately-served** | Importance roughly equals satisfaction (Opportunity Score 4-6) | Maintain current performance. Not a differentiator. |

**Step 6: Plot on importance vs. satisfaction matrix.**

```
         High Importance
              |
              |  UNDER-SERVED         (Build here)
              |  High importance,
              |  Low satisfaction
              |
              |
  Low    -----+------------------------  High
  Satisfaction|                         Satisfaction
              |
              |  TABLE STAKES           OVER-SERVED
              |  Low importance,        Low importance,
              |  Low satisfaction       High satisfaction
              |                         (Stop investing)
              |
         Low Importance
```

Target the upper-left quadrant: under-served outcomes where customers care intensely but existing solutions fall short. This is where new product investment generates the most value.

### Switch Interviews

Switch interviews reveal what triggers customers to change from one solution to another. This is critical for understanding adoption drivers and competitive dynamics.

**The Four Forces of Progress:**

Every switch decision is influenced by four competing forces. Two push toward switching; two resist it.

```
FORCES PUSHING TOWARD SWITCH:
  [1] Push: Pain with current solution  ──────────>
  [2] Pull: Appeal of new solution      ──────────>

FORCES RESISTING SWITCH:
  <──────────  [3] Anxiety: Fear of the new
  <──────────  [4] Habit: Comfort with the old
```

For a switch to happen, Push + Pull must exceed Anxiety + Habit. Your product strategy should strengthen Pull and reduce Anxiety -- you cannot control Push (that is your competitor's problem) or Habit (the customer must overcome that themselves).

**Interview Questions by Force:**

**Push (current pain):**
- "What first made you start looking for a new solution?"
- "What was the specific moment or event that made you say 'I need to do something different'?"
- "How long had you been unhappy before you started looking?"
- "What workarounds were you using to cope with the limitations?"

**Pull (new solution appeal):**
- "What caught your attention about [new solution] initially?"
- "What did you imagine your life would look like after switching?"
- "What specific capability or feature made you think this could work?"
- "Did someone recommend it? What did they say?"

**Anxiety (fear of new):**
- "What concerns did you have about switching?"
- "What almost stopped you from making the change?"
- "What questions did you need answered before committing?"
- "Did you try it before fully committing? What happened during the trial?"

**Habit (comfort with old):**
- "What did you like about your old solution despite its problems?"
- "What was hard to give up when you switched?"
- "Did you keep using the old solution alongside the new one for a while? Why?"
- "Were there things the old solution did that the new one still doesn't?"

---

## Opportunity Scoring

Once you have identified user needs through research, personas, and JTBD analysis, you need a systematic way to decide which opportunities to pursue first. Opportunity scoring transforms qualitative insight into quantifiable priorities, reducing the influence of opinion and organizational politics on product decisions.

### Opportunity Solution Trees (Teresa Torres)

The Opportunity Solution Tree (OST) is a visual framework that connects desired business outcomes to customer opportunities to solutions to experiments. It prevents the common failure mode of jumping from a business goal directly to a feature without understanding the underlying user need.

**Structure:**

```
                    [Desired Outcome]
                    (Business metric you
                     want to improve)
                          |
            +-------------+-------------+
            |             |             |
       [Opportunity 1] [Opportunity 2] [Opportunity 3]
       (Unmet need)    (Pain point)    (User desire)
            |             |             |
        +---+---+     +---+---+     +---+---+
        |       |     |       |     |       |
     [Sol A] [Sol B] [Sol C] [Sol D] [Sol E] [Sol F]
        |       |     |       |     |       |
     [Exp 1] [Exp 2] [Exp 3] [Exp 4] [Exp 5] [Exp 6]
```

**Rules:**

1. **Opportunities come from research, not brainstorming.** Every opportunity node must trace back to evidence from user research (interviews, surveys, behavioral data, support tickets). If you cannot cite the evidence, it is not a validated opportunity -- it is a guess.
2. **Multiple solutions per opportunity.** For each opportunity, brainstorm at least 3 possible solutions before committing to one. This prevents anchoring on the first idea. The best solution is rarely the first one you think of.
3. **Test before building.** Each solution should have at least one experiment to validate the approach before investing engineering resources. Experiments include: prototype tests, fake-door tests, Wizard of Oz MVPs, concierge tests, landing page tests, or data analysis.
4. **One tree per desired outcome.** Do not try to map your entire product onto one tree. Create a separate tree for each business metric you are trying to improve (e.g., one tree for activation, one for retention).

**Worked Example:**

```
Desired Outcome: Increase Day-7 activation rate from 22% to 40%
    |
    +-- Opportunity: New users can't find the feature that
    |   delivers core value (evidence: 5/8 users in onboarding
    |   study never reached the feedback dashboard)
    |     |
    |     +-- Solution A: Guided onboarding tour highlighting
    |     |   the feedback dashboard
    |     |     +-- Experiment: A/B test onboarding tour vs.
    |     |         current experience with 200 new signups
    |     |
    |     +-- Solution B: Make feedback dashboard the default
    |     |   landing page after signup
    |     |     +-- Experiment: Prototype test with 5 users --
    |     |         do they reach activation faster?
    |     |
    |     +-- Solution C: Send an email on Day 2 with a direct
    |         link to the dashboard and a 2-minute video
    |           +-- Experiment: Send to 100 users, measure
    |               click-through and activation rate
    |
    +-- Opportunity: Users who import data activate at 3x the
    |   rate, but only 30% import data in the first session
    |   (evidence: analytics cohort analysis)
    |     |
    |     +-- Solution A: CSV import wizard on signup flow
    |     +-- Solution B: Pre-populated sample data so users
    |     |   can experience value before importing their own
    |     +-- Solution C: Integrations with common tools
    |         (Slack, Jira) for automatic data sync
    |
    +-- Opportunity: Users who invite a teammate activate at
        2x the rate but only 15% invite anyone in week 1
        (evidence: cohort analysis + 3 interview mentions)
          |
          +-- Solution A: Prompt to invite a teammate after
          |   first key action
          +-- Solution B: Collaborative features that require
              a teammate to experience
```

### Scoring Criteria

Use four dimensions to score each opportunity. These dimensions are sometimes called RICE (Reach, Impact, Confidence, Effort), though the framework predates the acronym.

| Criterion | What It Measures | How to Estimate |
|---|---|---|
| **Reach** | How many users or customers will this affect in a given time period? | Use analytics data, segment sizes, or funnel data. Express as a number (e.g., "500 users/quarter"). |
| **Impact** | How much will this change behavior or move the target metric for each person reached? | Use a scale: 3 = massive (changes core workflow), 2 = high (significant improvement), 1 = medium (noticeable improvement), 0.5 = low (minor improvement). |
| **Confidence** | How sure are we about the reach and impact estimates? | 100% = strong evidence (A/B test data, validated prototype). 80% = good evidence (user research, analytics). 50% = moderate evidence (survey data, analogous products). 20% = speculation (gut feel, no data). |
| **Effort** | How many person-weeks of work will this take? | Estimate total person-weeks across engineering, design, and any other resources. Higher effort = lower priority, all else being equal. |

### Startup Mode: Simple Scoring Spreadsheet

For early-stage teams, a simple scoring spreadsheet is sufficient. Do not over-engineer the process -- the goal is to make prioritization decisions transparent and debatable, not to achieve false precision.

**Simple Scoring Template:**

| # | Opportunity | Reach (1-10) | Impact (1-10) | Confidence (1-10) | Effort (1-10) | Score (R*I*C)/E | Rank |
|---|---|---|---|---|---|---|---|
| 1 | _______________ | ___ | ___ | ___ | ___ | ___ | ___ |
| 2 | _______________ | ___ | ___ | ___ | ___ | ___ | ___ |
| 3 | _______________ | ___ | ___ | ___ | ___ | ___ | ___ |
| 4 | _______________ | ___ | ___ | ___ | ___ | ___ | ___ |
| 5 | _______________ | ___ | ___ | ___ | ___ | ___ | ___ |

**How to use:**

1. List all opportunities from your research and JTBD analysis.
2. Score each on Reach, Impact, Confidence, and Effort using a 1-10 scale.
3. Calculate the priority score: (Reach * Impact * Confidence) / Effort.
4. Rank by score. The top 3-5 are your focus candidates.
5. Discuss the ranking with the team. Use the scores as a starting point for debate, not as a final answer. If the team disagrees with the ranking, it usually means one of the scores is wrong -- update the score and recalculate.

**Important:** The formula is a conversation starter, not a decision-maker. If opportunity #3 scores highest but your team has zero expertise in that area, that context matters. Use the score to focus the discussion, not to end it.

### Enterprise Mode: Weighted Multi-Criteria Scoring

For larger teams with multiple stakeholders, a weighted scoring framework creates alignment by making criteria, weights, and estimates transparent and auditable.

**Step 1: Define criteria and assign weights.**

Gather key stakeholders (product, engineering, design, business). Agree on scoring criteria and assign weights based on strategic importance. Weights should sum to 100%.

| Criterion | Weight | Rationale |
|---|---|---|
| Reach | 20% | Important but not the only factor |
| Impact on target metric | 30% | Strongest signal of value |
| Confidence (evidence quality) | 20% | Penalizes speculation |
| Effort (inverse -- lower is better) | 15% | Accounts for resource constraints |
| Strategic alignment | 15% | Ensures work supports company objectives |

**Step 2: Teams estimate scores independently.**

Have 3-5 people score each opportunity independently (1-10 per criterion) before sharing scores. This prevents anchoring bias. Use a tool like Google Sheets where each person enters scores in their own tab.

**Step 3: Calibrate.**

Review scores where estimates diverge by 3+ points. Discuss: What information does one person have that the others don't? Update scores based on the discussion. The goal is not consensus -- it is shared understanding of the evidence.

**Step 4: Apply confidence weighting.**

Multiply each score by its confidence percentage. An impact score of 8 with 50% confidence becomes 4.0 effective impact. This mathematically penalizes opportunities where evidence is weak.

| Opportunity | Reach (R) | Conf-R | Impact (I) | Conf-I | Effort (E) | Strategic (S) | Weighted Score |
|---|---|---|---|---|---|---|---|
| Opp A | 7 | 80% | 9 | 60% | 3 | 8 | (7*.8*.2)+(9*.6*.3)+(7*.15)+(8*.15) = **4.99** |
| Opp B | 9 | 90% | 6 | 80% | 7 | 5 | (9*.9*.2)+(6*.8*.3)+(3*.15)+(5*.15) = **4.26** |

Note: Effort is inverted in the weighted score (10 - Effort score) so that lower effort receives a higher contribution.

**Step 5: Review and decide.**

Present the ranked list to the decision-making group. Use the weighted scores to structure the discussion, but allow for qualitative overrides when strategic context demands it. Document any overrides and the reasoning.

### Opportunity Assessment Template

Use this template for each opportunity that makes it past initial scoring and requires deeper evaluation before committing resources.

```
OPPORTUNITY ASSESSMENT
=======================
Opportunity: _______________
Date: _______________
Author: _______________
Status: [Evaluating / Approved / Rejected / Deferred]

1. OPPORTUNITY STATEMENT
   [2-3 sentences describing the unmet need or pain point]

2. EVIDENCE
   | Source | Finding | Strength |
   |--------|---------|----------|
   | [e.g., User interviews (N=8)] | [Key finding] | [Strong/Moderate/Weak] |
   | [e.g., Analytics data] | [Key finding] | [Strong/Moderate/Weak] |
   | [e.g., Support tickets (N=45)] | [Key finding] | [Strong/Moderate/Weak] |

3. SCORING
   | Criterion | Score (1-10) | Confidence | Weighted Score |
   |-----------|--------------|------------|----------------|
   | Reach | ___ | ___% | ___ |
   | Impact | ___ | ___% | ___ |
   | Effort | ___ | ___% | ___ |
   | Strategic alignment | ___ | ___% | ___ |
   | **Total** | | | **___** |

4. CUSTOMER SEGMENT AFFECTED
   - Primary persona: _______________
   - Secondary persona(s): _______________
   - Estimated users affected: ___

5. JOBS TO BE DONE ALIGNMENT
   - Core job served: [job statement]
   - Job map stage(s): [Define / Locate / Prepare / Confirm /
     Execute / Monitor / Modify / Conclude]
   - Outcome(s) addressed: [desired outcome statements from ODI]

6. PROPOSED SOLUTIONS (minimum 3)
   | Solution | Pros | Cons | Effort Estimate |
   |----------|------|------|-----------------|
   | A: ___ | ___ | ___ | ___ person-weeks |
   | B: ___ | ___ | ___ | ___ person-weeks |
   | C: ___ | ___ | ___ | ___ person-weeks |

7. RECOMMENDED EXPERIMENT
   - Hypothesis: If we [action], then [expected result],
     measured by [metric].
   - Method: [Prototype test / A/B test / Fake door / Survey /
     Concierge MVP]
   - Duration: ___
   - Success criteria: ___
   - Resources needed: ___

8. RISKS
   - [Risk 1 and mitigation]
   - [Risk 2 and mitigation]

9. DECISION
   - [ ] Approved -- proceed to experimentation
   - [ ] Deferred -- revisit in [timeframe]
   - [ ] Rejected -- reason: _______________
   Decision maker: _______________
   Date: _______________
```

---

## Output Formats

### Research Plan Template

```
RESEARCH PLAN
==============
Project: _______________
Date: _______________
Researcher: _______________
Sponsor: _______________

1. OBJECTIVE
   Primary question:
   Secondary questions:

2. BACKGROUND
   [What we know, what triggered this research]

3. METHODOLOGY
   Method: [Interviews / Survey / Usability test / Diary study]
   Sample size: ___
   Justification:

4. PARTICIPANT CRITERIA
   Target profile:
   Screener questions (3-5):
   Recruiting source:
   Incentive: $___

5. TIMELINE
   | Phase | Dates | Deliverable |
   |-------|-------|-------------|
   | Planning & recruiting | | |
   | Fieldwork | | |
   | Analysis | | |
   | Readout | | |

6. BUDGET
   | Item | Cost |
   |------|------|
   | Incentives | $___ |
   | Recruiting | $___ |
   | Tools | $___ |
   | Total | $___ |

7. DELIVERABLES
   - [ ] Executive summary
   - [ ] Full report
   - [ ] Highlight reel
   - [ ] Recommendations

8. RISKS AND LIMITATIONS
   -
   -
```

### Interview Guide Template

```
INTERVIEW GUIDE
================
Study: _______________
Date: _______________
Participant ID: _______________
Interviewer: _______________

PRE-SESSION CHECKLIST:
- [ ] Recording tool tested
- [ ] Consent form ready
- [ ] Note-taker briefed (if applicable)
- [ ] Incentive ready

OPENING (5 min):
- Introduce yourself and the purpose
- "No right or wrong answers"
- Ask permission to record
- Consent form signed

CONTEXT (10 min):
- "Tell me about your role and responsibilities."
- "Walk me through a typical day/week."
- [Custom context question 1]
- [Custom context question 2]

EXPLORATION (30 min):
- "Tell me about the last time you [task]."
- "What's the hardest part of [workflow]?"
- "How do you currently handle [problem]?"
- [Custom exploration question 1]
- [Custom exploration question 2]
- [Custom exploration question 3]
- [Custom exploration question 4]

DEEP DIVE (10 min):
- "You mentioned [X]. Tell me more."
- "Can you show me how you do that?"
- "Why is that important to you?"
- "What would happen if you couldn't do that?"

CLOSING (5 min):
- "What should I have asked but didn't?"
- "One thing you'd want us to know?"
- Thank participant, provide incentive
- Explain next steps

POST-SESSION (5 min, interviewer only):
- Top 3 takeaways:
  1.
  2.
  3.
- Surprises:
- Follow-up questions for future sessions:
```

### Persona Template: Proto-Persona

```
PROTO-PERSONA
==============
Status: HYPOTHESIS -- validate by [date]

Name: _______________
Photo: [placeholder]
Role / Title: _______________

DEMOGRAPHICS:
- Age range: ___
- Location: ___
- Tech savviness: [Low / Medium / High]
- Company size: ___

GOALS (top 3):
1.
2.
3.

FRUSTRATIONS (top 3):
1.
2.
3.

TOOLS THEY USE TODAY:
-
-
-

REPRESENTATIVE QUOTE:
"_______________"

HOW THEY'D DESCRIBE THE PROBLEM:
[2-3 sentences in their own words]

VALIDATION STATUS:
- [ ] Based on 5+ conversations
- [ ] Goals confirmed with behavioral evidence
- [ ] Frustrations observed directly
- [ ] Updated within 30 days
```

### Persona Template: Data-Backed

```
DATA-BACKED PERSONA
=====================
Name: _______________
Last updated: _______________
Next review: _______________

SEGMENT SIZE:
- % of user base: ___%
- User count: ___
- Revenue contribution: ___%

DEMOGRAPHIC PROFILE:
- Job titles: ___
- Company size: ___
- Industry: ___
- Geography: ___

BEHAVIORAL PROFILE:
- Login frequency: ___
- Primary workflow: ___
- Top features: ___
- Session duration: ___
- Collaboration: [Solo / Team / Cross-functional]

GOALS (ranked by research frequency):
1. [Goal] -- __% of segment
2. [Goal] -- __% of segment
3. [Goal] -- __% of segment

FRUSTRATIONS (ranked by severity):
1. [Frustration] -- [High/Med/Low]
2. [Frustration] -- [High/Med/Low]
3. [Frustration] -- [High/Med/Low]

CORE JOBS TO BE DONE:
1. When I [context], I want to [action], so I can [outcome].
2. When I [context], I want to [action], so I can [outcome].
3. When I [context], I want to [action], so I can [outcome].

KEY METRICS:
- NPS: ___
- 12-month retention: ___%
- Feature adoption: ___/10
- Support tickets/month: ___

JOURNEY MAP:
- Awareness: ___
- Evaluation: ___
- Adoption: ___
- Retention: ___
- Expansion: ___
- Churn signals: ___
```

### Job Map Template

```
JOB MAP
========
Core Job: _______________
Persona: _______________
Date: _______________

| Stage | What User Does | Current Tools | Pain Points | Opportunities |
|-------|---------------|---------------|-------------|---------------|
| 1. Define | | | | |
| 2. Locate | | | | |
| 3. Prepare | | | | |
| 4. Confirm | | | | |
| 5. Execute | | | | |
| 6. Monitor | | | | |
| 7. Modify | | | | |
| 8. Conclude | | | | |

FUNCTIONAL JOB STATEMENT:
When I [context], I want to [action], so I can [outcome].

EMOTIONAL JOB:
I want to feel _______________ when performing this job.

SOCIAL JOB:
I want to be perceived as _______________ by [audience].

PRIORITY OUTCOMES (from ODI analysis, if available):
| Desired Outcome | Importance | Satisfaction | Opp Score |
|-----------------|------------|--------------|-----------|
| | | | |
| | | | |
| | | | |
```

### Opportunity Solution Tree Template

```
OPPORTUNITY SOLUTION TREE
==========================
Desired Outcome: _______________
Target Metric: _______________ from ___ to ___
Owner: _______________
Date: _______________

OPPORTUNITY 1: _______________
  Evidence: [source, N, key finding]
  |
  +-- Solution A: _______________
  |     Experiment: _______________
  |     Success criteria: _______________
  |
  +-- Solution B: _______________
  |     Experiment: _______________
  |     Success criteria: _______________
  |
  +-- Solution C: _______________
        Experiment: _______________
        Success criteria: _______________

OPPORTUNITY 2: _______________
  Evidence: [source, N, key finding]
  |
  +-- Solution A: _______________
  |     Experiment: _______________
  |     Success criteria: _______________
  |
  +-- Solution B: _______________
        Experiment: _______________
        Success criteria: _______________

OPPORTUNITY 3: _______________
  Evidence: [source, N, key finding]
  |
  +-- Solution A: _______________
  |     Experiment: _______________
  |     Success criteria: _______________
  |
  +-- Solution B: _______________
        Experiment: _______________
        Success criteria: _______________

DECISION LOG:
| Date | Opportunity | Solution Selected | Rationale |
|------|-------------|-------------------|-----------|
|      |             |                   |           |
```

### Opportunity Scoring Spreadsheet Template

```
OPPORTUNITY SCORING
====================
Date: _______________
Team: _______________
Scoring method: [Simple (R*I*C)/E | Weighted multi-criteria]

SIMPLE SCORING:
| # | Opportunity | Reach (1-10) | Impact (1-10) | Confidence (1-10) | Effort (1-10) | Score | Rank |
|---|-------------|--------------|---------------|-------------------|---------------|-------|------|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |
| 5 | | | | | | | |

Formula: Score = (Reach * Impact * Confidence) / Effort

WEIGHTED SCORING (enterprise):
Criteria weights (must sum to 100%):
- Reach: ___% | Impact: ___% | Confidence: ___% |
  Effort: ___% | Strategic alignment: ___%

| # | Opportunity | R | Conf-R | I | Conf-I | E (inv) | S | Weighted |
|---|-------------|---|--------|---|--------|---------|---|----------|
| 1 | | | % | | % | | | |
| 2 | | | % | | % | | | |
| 3 | | | % | | % | | | |

CALIBRATION NOTES:
- Score divergences discussed:
- Adjustments made:

DECISION:
- Top opportunities selected: ___
- Rationale for any overrides: ___
- Next step: [Experiment / Build / Defer / Kill]
```
