---
name: Product Strategy
description: Product vision, OKRs, and competitive analysis for startup and enterprise PMs — lean canvas, full vision docs, cascading objectives, feature parity grids, and positioning maps.
triggers:
  - product vision
  - vision doc
  - lean canvas
  - elevator pitch
  - OKR
  - objectives and key results
  - competitive analysis
  - competitor
  - positioning
  - strategy
  - product strategy
  - market positioning
  - SWOT
  - feature comparison
---

# Product Strategy

## Disclaimer

Strategic outputs should be validated with stakeholders, market data, and real user signals before making product decisions.

## Product Vision

A product vision defines where you are going and why it matters. It is the single most important artifact a PM owns because every downstream decision -- roadmap priorities, hiring, partnerships, saying no -- flows from it. A weak vision produces a scattered product. A strong vision aligns an organization without requiring constant top-down direction.

### Startup Mode: Lean Canvas

For early-stage products, use Ash Maurya's Lean Canvas to capture the business model on one page. Complete all 9 blocks. The goal is speed and testability -- you should be able to fill this out in under 30 minutes and update it weekly as you learn.

**Lean Canvas Template:**

| Block | Prompt | Your Answer |
|---|---|---|
| **1. Problem** | List the top 3 problems your target customers face. What existing alternatives do they use today? | _______________ |
| **2. Customer Segments** | Who are your early adopters? Be specific: job title, company size, geography, behavior. Separate early adopters from mainstream customers. | _______________ |
| **3. Unique Value Proposition** | Single, clear, compelling sentence that explains why you are different and worth paying attention to. What is the high-level concept? (e.g., "Flickr for video") | _______________ |
| **4. Solution** | For each problem listed in Block 1, describe the simplest solution. Focus on MVP-level features, not the full vision. | _______________ |
| **5. Channels** | How will you reach your early adopters? List both free and paid channels. Prioritize channels where your customers already spend time. | _______________ |
| **6. Revenue Streams** | How will you make money? List pricing model (subscription, usage-based, freemium, transaction fee). What will you charge? What is the customer's willingness to pay? | _______________ |
| **7. Cost Structure** | What are your fixed costs (salaries, hosting, office) and variable costs (marketing, support per customer)? What does it cost to acquire a customer (CAC)? | _______________ |
| **8. Key Metrics** | What 3-5 numbers will you track to know if the business is working? Focus on activation, retention, and revenue metrics -- not vanity metrics like page views. | _______________ |
| **9. Unfair Advantage** | What do you have that cannot be easily copied or bought? Examples: proprietary data, network effects, domain expertise, existing audience, regulatory advantage. Be honest -- many startups don't have one yet. | _______________ |

**Fill-in order:** Start with Problem and Customer Segments (blocks 1-2) because everything else depends on them. Then UVP (3), Solution (4), Channels (5), Revenue (6), Cost (7), Metrics (8), Unfair Advantage (9).

**Elevator Pitch Template:**

Use this formula to distill the canvas into a single pitch:

> For **[target customer]** who **[need or opportunity]**, **[product name]** is a **[category]** that **[key benefit]**. Unlike **[primary competitor or current alternative]**, we **[differentiator]**.

**Worked example:**

> For **early-stage B2B SaaS founders** who **struggle to prioritize which features to build next**, **SignalPM** is a **product management tool** that **uses customer conversation data to rank features by revenue impact**. Unlike **Productboard**, we **require zero manual tagging -- our AI extracts signals from sales calls automatically**.

### Enterprise Mode: Full Vision Document

For products with established teams, multiple stakeholders, and organizational dependencies, a Lean Canvas is not sufficient. Use a structured vision document that can survive a quarterly review cycle and align cross-functional teams.

**Vision Document Structure:**

#### Vision Statement
One to two sentences. Aspirational but specific. Describes the future state you are creating, not the product you are building today.

- Good: "Every product team makes data-informed prioritization decisions in under 5 minutes, without needing a data analyst."
- Weak: "Build the best product management platform." (Too vague to guide decisions.)
- Weak: "Ship feature X by Q3." (That is a goal, not a vision.)

The vision should be stable over 2-3 years. If you are rewriting it every quarter, it is not a vision -- it is a quarterly goal.

#### Strategic Context
Document the external and internal forces that make this vision relevant right now:

- **Market trends:** What is changing in your market that creates the opportunity? Cite specific data points (e.g., "73% of mid-market companies now have a dedicated product ops role, up from 18% in 2021 -- source: ProductPlan survey").
- **Company strategy alignment:** How does this product vision support the broader company mission and current strategic priorities? Reference the company's annual plan or CEO objectives directly.
- **Technology shifts:** Are there enabling technologies (AI, APIs, platform changes) that make this vision newly achievable?
- **Competitive pressure:** What competitors or substitutes are forcing a strategic response?

#### Target Customer
Define primary and secondary segments with enough specificity to be actionable:

- **Primary segment:** The customer you optimize every decision for. Include: job title, company size, industry, key pain points, buying behavior, current tools, willingness to pay.
- **Secondary segment:** Customers who benefit but are not the primary focus. Document explicitly where their needs diverge from the primary segment and how you will handle those trade-offs.

#### Value Proposition by Segment
For each target segment, articulate the value proposition separately. What matters most to each group will differ:

| Segment | Primary Pain Point | Value We Deliver | How We Prove It |
|---|---|---|---|
| Primary: Product Managers at Series B-D SaaS | Spending 10+ hours/week on manual prioritization | Automated signal extraction reduces prioritization time by 80% | Time-to-decision metric in onboarding |
| Secondary: VP Product at Enterprise | No visibility into what PMs are prioritizing across teams | Portfolio-level dashboard with real-time roadmap alignment scores | Executive dashboard adoption rate |

#### Key Differentiators
List 3-5 differentiators. Each must pass the defensibility test: Could a well-funded competitor replicate this within 12 months? If yes, it is a feature, not a differentiator.

- **Defensible differentiators:** Proprietary data, network effects, deep integrations, unique methodology, switching costs, brand trust built over years.
- **Non-defensible (still valuable, but not differentiators):** UI quality, speed, specific features, pricing.

For each differentiator, document: what it is, why it matters to the customer, and why it is hard to replicate.

#### Success Metrics
Define both leading and lagging indicators:

- **Leading indicators** (predict future success): Activation rate, weekly active usage, NPS of new cohorts, time-to-value during onboarding, feature adoption of core workflows.
- **Lagging indicators** (confirm past success): Revenue, retention rate, market share, customer lifetime value, net revenue retention.

Set targets for each metric. Without targets, metrics are just numbers.

#### Stakeholder Alignment Matrix
Document key stakeholders who must support the vision for it to succeed:

| Stakeholder | Their Primary Concern | How We Address It | Alignment Status |
|---|---|---|---|
| CEO | Revenue growth + market positioning | Vision targets $X ARR opportunity with clear path to market leadership | Aligned |
| VP Engineering | Technical debt and team capacity | Phased rollout with dedicated tech-debt sprints in Q2 and Q4 | Partially aligned -- needs capacity discussion |
| Head of Sales | Pipeline impact and competitive win rate | New capabilities enable upsell to existing accounts; competitive positioning doc in progress | Needs review |
| CFO | Unit economics and payback period | CAC payback within 18 months; margin improvement from platform consolidation | Pending data |

#### Review Cadence
- **Quarterly:** Review vision document with leadership. Update strategic context and metrics. Vision statement itself should rarely change.
- **Annually:** Full vision refresh. Reassess market trends, customer segments, and competitive landscape. Revalidate or pivot differentiators.

### Vision Quality Checklist

Before finalizing any vision document, validate it against these criteria:

- [ ] **Is it inspiring?** Would someone talented want to join the team to work on this?
- [ ] **Is it specific enough to guide decisions?** If two reasonable PMs would make different roadmap decisions based on the vision, it is too vague.
- [ ] **Is it stable over 2-3 years?** If it needs rewriting every quarter, it is a goal, not a vision.
- [ ] **Is it falsifiable?** Can you imagine a world where this vision turns out to be wrong? If not, it is too generic (e.g., "Make customers happy" is unfalsifiable and therefore useless).
- [ ] **Does it exclude?** A good vision says what you are NOT doing as clearly as what you are doing. If everything fits under the vision, it is not doing its job.
- [ ] **Can a new team member read it and understand the product direction in 10 minutes?** If not, simplify.

---

## OKRs

OKRs (Objectives and Key Results) translate vision into measurable quarterly commitments. They are the bridge between "where we are going" (vision) and "what we are doing this quarter" (roadmap). Done well, OKRs create alignment and focus. Done poorly, they become bureaucratic overhead.

### OKR Writing Principles

- **Objectives are qualitative and inspiring.** They describe a desired outcome in human-readable language. "Become the most trusted platform for mid-market PMs" -- not "Increase NPS to 55."
- **Key Results are quantitative and measurable.** They define how you will know the objective has been achieved. There is no ambiguity about whether a KR was met.
- **KRs measure outcomes, not activities.** "Increase activation rate from 25% to 40%" (outcome) -- not "Launch onboarding redesign" (activity). The activity might fail to move the metric. The KR holds you accountable to impact.
- **3-5 objectives per team per quarter.** More than 5 means nothing is truly prioritized. If everything is important, nothing is.
- **3-4 key results per objective.** Fewer than 3 means the objective is probably too narrow. More than 4 means you are measuring too many things and losing focus.

### Startup Mode: Team-Level Quarterly OKRs

For small teams (2-15 people), keep OKRs simple. One page. One planning session. Review weekly in a 15-minute standup.

**Template:**

```
Quarter: Q_ 20__
Team: _______________

Objective 1: [Qualitative, inspiring outcome statement]
  KR 1.1: [Metric] from [current baseline] to [target]
  KR 1.2: [Metric] from [current baseline] to [target]
  KR 1.3: [Metric] from [current baseline] to [target]

Objective 2: [Qualitative, inspiring outcome statement]
  KR 2.1: [Metric] from [current baseline] to [target]
  KR 2.2: [Metric] from [current baseline] to [target]
  KR 2.3: [Metric] from [current baseline] to [target]
```

**Worked Example:**

```
Quarter: Q2 2026
Team: Growth Pod (SignalPM)

Objective 1: Become the go-to solution for early-stage founders
  KR 1.1: Increase monthly signups from founder segment from 120 to 350
  KR 1.2: Improve Day-7 activation rate from 22% to 40%
  KR 1.3: Achieve 15 organic mentions in founder communities
           (Indie Hackers, Hacker News, Twitter/X) -- baseline: 3
  KR 1.4: Reduce time-to-first-value from 25 minutes to under 8 minutes

Objective 2: Prove repeatable revenue model
  KR 2.1: Increase free-to-paid conversion rate from 3.1% to 6%
  KR 2.2: Reach $18K MRR -- baseline: $7K
  KR 2.3: Achieve net revenue retention of 105%+ across paying cohorts
```

### Enterprise Mode: Cascading OKRs

For organizations with multiple teams, OKRs must cascade: company-level objectives flow into department objectives, which flow into team objectives. Each level answers: "How does our work contribute to the level above?"

**Cascade Structure:**

```
Company Objective: Win the mid-market segment in North America
  |
  +-- Department (Product) Objective: Deliver the features mid-market
  |   buyers rank as must-haves
  |     KR: Close feature parity gap on top 10 requested capabilities
  |         (from 4/10 to 8/10)
  |     KR: Achieve "Strong" rating on G2 for mid-market category
  |         (current: "Moderate")
  |
  +-- Department (Sales) Objective: Build a repeatable mid-market
  |   sales motion
  |     KR: Increase mid-market pipeline from $2M to $6M
  |     KR: Reduce mid-market sales cycle from 95 days to 65 days
  |
  +-- Department (Engineering) Objective: Ensure platform reliability
      meets enterprise buyer expectations
        KR: Achieve 99.95% uptime (current: 99.8%)
        KR: Reduce P1 incident response time from 45 min to 15 min
```

**How team OKRs ladder up:** Each team should be able to draw a direct line from their KRs to a department-level KR. If a team cannot explain how their work supports the level above, their OKRs are misaligned.

**Dependency Mapping Between Teams:**

When team A's OKR depends on team B's output, document the dependency explicitly:

| Team A OKR | Depends On | Team B OKR | Handoff Date | Status |
|---|---|---|---|---|
| Product: Close feature parity gap to 8/10 | API infrastructure for SSO and SCIM | Engineering: Ship enterprise auth platform | March 15 | On track |
| Sales: Reduce mid-market cycle to 65 days | Product demo environment | Product: Launch self-serve demo sandbox | February 28 | At risk |

**Cross-Team Alignment Scoring:**

At the start of each quarter, run an alignment exercise. Each team rates how well every other team's OKRs support shared goals on a 1-5 scale:

| Rating Team | Rates: Product OKRs | Rates: Eng OKRs | Rates: Sales OKRs |
|---|---|---|---|
| Product | -- | 4 (strong support) | 3 (some gaps in enablement) |
| Engineering | 5 (clear requirements) | -- | 2 (unclear on sales tooling needs) |
| Sales | 3 (missing demo capability) | 4 (reliability improvements help deals) | -- |

Scores below 3 trigger a cross-team alignment meeting before the quarter begins. Resolve conflicts in priorities before execution, not during.

**Quarterly Review Format:**

1. **Score each KR** on 0.0-1.0 scale (see grading below).
2. **Narrative per objective:** What worked, what didn't, what we learned.
3. **Dependency retrospective:** Did cross-team handoffs happen on time? What broke?
4. **Carry-forward decisions:** Which OKRs roll into next quarter vs. retire?

### OKR Grading

Use a 0.0 to 1.0 scale for each key result:

| Score | Interpretation |
|---|---|
| 0.0 - 0.3 | Failed to make meaningful progress. Investigate root cause. |
| 0.4 - 0.6 | Made progress but fell short. Acceptable if the goal was truly ambitious. |
| **0.7** | **Target. This is what you are aiming for. OKRs are stretch goals -- hitting 70% means the goal was appropriately ambitious.** |
| 0.8 - 0.9 | Exceeded expectations. Either exceptional execution or the goal was not ambitious enough. |
| 1.0 | Fully achieved. If this happens consistently, goals are too easy. Increase ambition. |

**Team-level grading:** Average KR scores per objective, then average objectives for an overall team score. Share scores transparently across teams.

**Grading is for learning, not punishment.** OKR scores should never be tied directly to compensation or performance reviews. This incentivizes sandbagging and destroys the stretch-goal culture that makes OKRs effective.

### OKR Anti-Patterns

Watch for these failure modes and correct them immediately:

- **Vanity metrics as key results.** "Reach 10,000 page views" -- page views do not indicate product value. Replace with metrics that reflect actual user outcomes: activation, retention, revenue, satisfaction.
- **Too many objectives (>5).** If you have 7 objectives, you have 0 priorities. Force-rank and cut to 3-5. The pain of cutting is the point -- it forces strategic clarity.
- **Activity-based KRs.** "Launch feature X" or "Ship redesign" are activities, not outcomes. The feature might launch and fail. Rewrite as: "Increase activation rate by 15% via onboarding improvements" -- this holds you accountable to impact, not output.
- **Sandbagging.** Teams set easy goals they know they can hit at 1.0. Fix this by reviewing historical scores: if a team consistently scores 0.9+, they are not stretching. Coach them on ambitious goal-setting.
- **Set and forget.** OKRs written in January and not reviewed until April are worthless. Review progress weekly (5-minute check-in), update confidence levels bi-weekly, and do a formal mid-quarter review to course-correct.
- **Top-down only.** If leadership dictates all OKRs without team input, teams have no ownership. Use a 60/40 split: 60% of OKRs cascade from leadership priorities, 40% are proposed bottom-up by teams based on their domain expertise.
- **Confusing OKRs with task lists.** OKRs define outcomes. Task lists and sprint backlogs define how you get there. They are complementary, not interchangeable.

---

## Competitive Analysis

Competitive analysis tells you who you are fighting, where you are winning, and where you are vulnerable. The depth of analysis should match the stakes: a quick landscape scan for early product decisions, a full competitive matrix for pricing changes, market entry, or board presentations.

### Startup Mode: Quick Landscape Scan

For early-stage products, you do not need a 50-page competitive report. You need enough understanding of the market to make informed positioning and prioritization decisions. Use the 2-hour research sprint below.

**2-Hour Research Sprint Protocol:**

**Hour 1: Identify and profile competitors (60 min)**

1. **List competitors (15 min).** Google your problem space, not your product category. Search for what your customers search for. Check G2, Capterra, Product Hunt, and Reddit threads. Identify 5 competitors: 3 direct (same problem, same customer) + 2 indirect (same problem, different approach -- or different problem, competing for same budget).
2. **Profile each competitor (45 min, ~9 min each).** For each competitor, fill out:

| Attribute | Competitor 1 | Competitor 2 | Competitor 3 | Competitor 4 | Competitor 5 |
|---|---|---|---|---|---|
| What they do well | | | | | |
| Where they fall short | | | | | |
| Pricing model | | | | | |
| Target customer | | | | | |
| Funding stage / revenue (if known) | | | | | |

Sources: Competitor websites, G2 reviews (read the 2-3 star reviews -- they reveal real weaknesses), Crunchbase for funding, LinkedIn for headcount.

**Hour 2: Synthesize and position (60 min)**

3. **Draw a positioning map (15 min).** Pick 2 axes that matter most to your customers. Plot all competitors and yourself. Identify clusters and whitespace.
4. **Write the 1-page landscape summary (30 min).** Structure: Market overview (3-4 sentences), Top competitors (1-2 sentences each), Key insight (what this means for your strategy), Open questions (what you still need to learn).
5. **Identify 3 next steps (15 min).** What will you do differently based on this analysis? If the analysis does not change any decision, it was not worth doing.

**Output: 1-page landscape summary** suitable for sharing with co-founders, advisors, or investors.

### Enterprise Mode: Full Competitive Matrix

For mature products competing in established markets, you need rigorous, structured competitive intelligence that can support pricing decisions, roadmap prioritization, and board-level strategy discussions.

#### Feature Parity Grid

List the 15-25 features that matter most to your target customer's buying decision. Score each competitor (and your own product) on a 1-5 scale:

| Score | Definition |
|---|---|
| 1 | Absent -- feature does not exist |
| 2 | Basic -- feature exists but is minimal, often cited as a weakness in reviews |
| 3 | Adequate -- feature works but is not a differentiator |
| 4 | Strong -- feature is well-regarded, frequently cited as a positive |
| 5 | Best-in-class -- feature is a recognized market leader capability |

**Feature Parity Grid Template:**

| Feature | Customer Importance (H/M/L) | Weight | Your Product | Competitor A | Competitor B | Competitor C |
|---|---|---|---|---|---|---|
| SSO / SAML integration | H | 3 | 2 | 5 | 4 | 3 |
| Custom reporting | H | 3 | 4 | 3 | 4 | 5 |
| API extensibility | M | 2 | 5 | 3 | 2 | 4 |
| Mobile app | M | 2 | 3 | 4 | 3 | 2 |
| Onboarding / time-to-value | H | 3 | 4 | 2 | 3 | 3 |
| ... (15-25 rows total) | | | | | | |
| **Weighted Total** | | | **___** | **___** | **___** | **___** |

**How to weight:** Assign weights based on customer importance. High = 3, Medium = 2, Low = 1. Multiply each feature score by weight, then sum for a weighted total per competitor. This prevents overweighting features that only matter to a small segment.

**Data sources for scoring:** G2 reviews, customer interviews, your own product testing, analyst reports, competitor documentation. Never score based on marketing claims alone -- verify with user-reported evidence.

#### Positioning Map

Select 2 axes that represent the key trade-offs your customers face when choosing a product. These should be attributes where competitors genuinely differ -- not axes where everyone clusters in the same spot.

**Good axis choices:**
- Ease of use vs. Feature depth
- Price vs. Quality of support
- SMB-focused vs. Enterprise-focused
- Vertical-specific vs. Horizontal platform
- Self-serve vs. Sales-assisted

**How to build:**
1. Select axes based on customer research (what do buyers compare when evaluating?).
2. Plot each competitor as a dot. Use relative positioning, not precise coordinates.
3. Plot your own product. Be honest about where you sit today, not where you aspire to be.
4. Identify whitespace -- areas with customer demand but no strong competitor.
5. Identify clusters -- areas where 3+ competitors are crowded. Competing here means winning on execution, not differentiation.

**Interpretation:** Whitespace is not automatically valuable. Validate that customers actually want the combination of attributes the whitespace represents. Sometimes a quadrant is empty because no one wants what it offers.

#### Competitive Threat Assessment

For each major competitor, assess their strategic momentum across five dimensions:

| Dimension | What to Look For | Competitor A | Competitor B |
|---|---|---|---|
| **Market share / growth** | Revenue growth rate, customer count trajectory, win/loss trends | Growing 40% YoY; winning in mid-market | Flat growth; losing enterprise deals |
| **Funding / resources** | Recent fundraise, cash reserves, burn rate, profitability | Series C ($80M); 3+ years runway | Bootstrapped; profitable but resource-constrained |
| **Product velocity** | Major releases per quarter, changelog frequency, beta features | 2 major releases/quarter; aggressive roadmap | 1 release/quarter; focused on stability |
| **Talent signals** | Key hires, headcount growth, job posting patterns | Hiring 15 engineers + new VP Product | Flat headcount; backfilling attrition only |
| **Strategic direction** | Public statements, partnership announcements, market moves | Expanding into enterprise; launched SOC 2 compliance | Doubling down on SMB; launched freemium tier |

**Interpretation:** A competitor that is growing fast, well-funded, shipping quickly, and hiring aggressively is a serious threat regardless of current feature parity. A competitor with better features but flat growth and no funding is a declining threat.

#### SWOT per Competitor

For each major competitor, complete a concise SWOT:

```
Competitor: _______________

Strengths (internal, positive):
-
-
-

Weaknesses (internal, negative):
-
-
-

Opportunities (external, positive):
-
-
-

Threats (external, negative):
-
-
-

Strategic implication for us:
[1-2 sentences: What does this competitor's SWOT mean for our strategy?]
```

### Data Sources for Competitive Intelligence

Use multiple sources. No single source gives the full picture.

| Source | What It Reveals | Refresh Cadence |
|---|---|---|
| **G2 / Capterra / TrustRadius** | Real user sentiment, feature strengths/weaknesses, satisfaction trends | Monthly (check new reviews) |
| **LinkedIn** | Headcount trends, key hires, departures, team structure, hiring signals | Monthly |
| **Crunchbase / PitchBook** | Funding rounds, investors, valuation signals, M&A activity | Quarterly |
| **Press releases** | Product launches, partnerships, customer wins, strategic direction | As published (set alerts) |
| **Product changelogs** | Feature velocity, engineering priorities, areas of investment | Monthly |
| **Pricing pages** | Pricing model changes, tier restructuring, feature gating | Quarterly |
| **Job postings** | Strategic direction (hiring ML engineers = AI investment; hiring enterprise sales = upmarket move) | Monthly |
| **Earnings calls** (public companies) | Revenue, growth, strategic priorities, competitive commentary | Quarterly |
| **Patent filings** | Technology direction, defensible IP, future product bets | Semi-annually |

### Competitive Monitoring

One-time analysis goes stale quickly. Set up ongoing monitoring:

1. **Google Alerts:** Set alerts for each competitor's name, product name, and key executives. Review weekly.
2. **Changelog tracking:** Bookmark each competitor's changelog or release notes page. Review monthly. Note: some tools (e.g., Feedly, Visualping) can auto-detect page changes.
3. **Review site monitoring:** Check G2 and Capterra monthly for new reviews of competitors. Pay special attention to negative reviews of market leaders -- these reveal opportunities.
4. **Quarterly competitive refresh:** Every quarter, update the feature parity grid, positioning map, and threat assessment. Present findings to the product and leadership team. Update strategy if competitive landscape has shifted materially.
5. **Win/loss analysis integration:** Every closed deal (won or lost), ask: Which competitors were in the evaluation? Why did the customer choose us or them? Feed these signals into the competitive matrix.

### Competitive Response Framework

When a competitor launches a notable feature, ships a major update, or makes a strategic move, use this framework to decide how to respond:

**Step 1: Assess relevance**
- Is this feature or move in our strategic lane? (Does it affect the same customer segment and use case we are targeting?)
- If no, document and move on. Not every competitor move requires a response.

**Step 2: Assess impact on positioning**
- Does this move change how customers perceive us relative to this competitor?
- Will our sales team start losing deals because of this?
- Check with sales and customer success: Are customers asking about this?

**Step 3: Choose a response**

| Response | When to Use | Example |
|---|---|---|
| **Match** | Feature is table-stakes and customers expect it. Not having it is a deal-breaker. | Competitor adds SSO; your enterprise buyers require it. Build SSO. |
| **Differentiate** | Feature is in your space but you can offer a meaningfully better or different approach. | Competitor launches basic reporting. You invest in self-serve analytics that goes deeper. |
| **Ignore** | Feature targets a different segment, does not affect your positioning, or is not what your customers need. | Competitor adds a mobile app; your users are desktop-only power users. Ignore. |
| **Leapfrog** | Competitor move reveals a larger opportunity that you can address more ambitiously. | Competitor adds manual data import. You build automated, real-time data sync. Skip their approach entirely. |

**Step 4: Communicate the decision.** Share the assessment and response with product, sales, and leadership. Sales needs talking points. Leadership needs to know the competitive landscape is being actively managed.

---

## Output Formats

### Vision Doc Template: Lean Canvas

```
Product: _______________
Date: _______________
Author: _______________

+-----------------+------------------+------------------+
| PROBLEM         | SOLUTION         | UNIQUE VALUE     |
| 1.              | 1.               | PROPOSITION      |
| 2.              | 2.               |                  |
| 3.              | 3.               | [Single clear    |
|                 |                  |  sentence]       |
| Existing        |                  |                  |
| Alternatives:   |                  | High-Level       |
|                 |                  | Concept:         |
+-----------------+------------------+------------------+
| UNFAIR          | CHANNELS         | CUSTOMER         |
| ADVANTAGE       |                  | SEGMENTS         |
|                 | 1.               |                  |
|                 | 2.               | Early Adopters:  |
|                 | 3.               |                  |
+-----------------+------------------+------------------+
| KEY METRICS     | COST STRUCTURE   | REVENUE STREAMS  |
| 1.              |                  |                  |
| 2.              | Fixed:           | Model:           |
| 3.              | Variable:        | Price:           |
|                 | CAC:             | LTV:             |
+-----------------+------------------+------------------+

Elevator Pitch:
For [target customer] who [need], [product] is a [category]
that [key benefit]. Unlike [competitor], we [differentiator].
```

### Vision Doc Template: Full Enterprise

```
PRODUCT VISION DOCUMENT
=======================
Product: _______________
Version: ___  |  Date: _______________
Owner: _______________  |  Approver: _______________

1. VISION STATEMENT
   [1-2 sentences, aspirational, stable over 2-3 years]

2. STRATEGIC CONTEXT
   Market trends:
   Company strategy alignment:
   Technology shifts:
   Competitive pressure:

3. TARGET CUSTOMER
   Primary segment:
   Secondary segment:
   Trade-offs between segments:

4. VALUE PROPOSITION BY SEGMENT
   | Segment | Pain Point | Value Delivered | Proof Point |
   |---------|------------|-----------------|-------------|
   |         |            |                 |             |

5. KEY DIFFERENTIATORS (3-5)
   | Differentiator | Why It Matters | Why It's Hard to Copy |
   |----------------|----------------|-----------------------|
   |                |                |                       |

6. SUCCESS METRICS
   Leading indicators:
   Lagging indicators:
   Targets:

7. STAKEHOLDER ALIGNMENT
   | Stakeholder | Concern | How Addressed | Status |
   |-------------|---------|---------------|--------|
   |             |         |               |        |

8. REVIEW CADENCE
   Quarterly: [date of next review]
   Annual refresh: [date]

QUALITY CHECK:
[ ] Inspiring  [ ] Decision-guiding  [ ] Stable 2-3 yrs
[ ] Falsifiable  [ ] Exclusionary  [ ] 10-min readable
```

### OKR Template: Team-Level

```
OKR PLAN — TEAM LEVEL
======================
Quarter: Q_ 20__
Team: _______________
Owner: _______________

OBJECTIVE 1: [Qualitative, inspiring outcome]
  KR 1.1: [Metric] from [baseline] to [target]
          Confidence: __% | Score (end of quarter): __/1.0
  KR 1.2: [Metric] from [baseline] to [target]
          Confidence: __% | Score (end of quarter): __/1.0
  KR 1.3: [Metric] from [baseline] to [target]
          Confidence: __% | Score (end of quarter): __/1.0

OBJECTIVE 2: [Qualitative, inspiring outcome]
  KR 2.1: [Metric] from [baseline] to [target]
          Confidence: __% | Score (end of quarter): __/1.0
  KR 2.2: [Metric] from [baseline] to [target]
          Confidence: __% | Score (end of quarter): __/1.0
  KR 2.3: [Metric] from [baseline] to [target]
          Confidence: __% | Score (end of quarter): __/1.0

OVERALL SCORE: __/1.0
KEY LEARNINGS:
CARRY-FORWARD:
```

### OKR Template: Cascading (Enterprise)

```
CASCADING OKR PLAN
===================
Period: Q_ 20__  |  Company: _______________

COMPANY OBJECTIVE: [Top-level outcome]
  Company KR 1:
  Company KR 2:
  Company KR 3:

  DEPARTMENT: [Name]
  Department Objective: [Supports Company KR #__]
    Dept KR 1:
    Dept KR 2:

    TEAM: [Name]
    Team Objective: [Supports Dept KR #__]
      Team KR 1:
      Team KR 2:
      Team KR 3:

DEPENDENCY MAP:
| Team A KR | Depends On | Team B KR | Handoff Date | Status |
|-----------|------------|-----------|--------------|--------|
|           |            |           |              |        |

CROSS-TEAM ALIGNMENT SCORES (1-5):
| Rating Team | Team 1 | Team 2 | Team 3 |
|-------------|--------|--------|--------|
| Team 1      | --     |        |        |
| Team 2      |        | --     |        |
| Team 3      |        |        | --     |

Action items for scores below 3:
-
```

### Competitive Matrix Template

```
COMPETITIVE ANALYSIS
=====================
Date: _______________  |  Author: _______________
Market: _______________

LANDSCAPE SUMMARY (1 page):
[3-4 sentence market overview]
[Key insight that changes our strategy]

FEATURE PARITY GRID:
| Feature | Importance | Weight | Us | Comp A | Comp B | Comp C |
|---------|------------|--------|----|--------|--------|--------|
|         |            |        |    |        |        |        |
| WEIGHTED TOTAL       |        |    |        |        |        |

THREAT ASSESSMENT:
| Dimension         | Comp A | Comp B | Comp C |
|-------------------|--------|--------|--------|
| Market share/growth|       |        |        |
| Funding/resources  |       |        |        |
| Product velocity   |       |        |        |
| Talent signals     |       |        |        |
| Strategic direction|       |        |        |

SWOT (per competitor):
[Use template from Competitive Analysis section]

RESPONSE LOG:
| Date | Competitor Move | Our Assessment | Response |
|------|-----------------|----------------|----------|
|      |                 |                |          |
```

### Positioning Map Template

```
POSITIONING MAP
================
Axis X: _______________ (e.g., Ease of Use)
Axis Y: _______________ (e.g., Feature Depth)

         High Y
           |
           |    [Comp B]
           |              [Comp C]
           |
           |        * [Us]
           |
  Low X ---+--------------------------- High X
           |
           |  [Comp A]
           |
           |              [Comp D]
           |
         Low Y

WHITESPACE IDENTIFIED:
- [Quadrant/area]: [Why it may be an opportunity]
- [Quadrant/area]: [Why it may be empty for a reason]

CLUSTERS:
- [Area]: [Competitors clustered here; implications]

STRATEGIC IMPLICATION:
[1-2 sentences: What does this map tell us about where to
 position or reposition?]
```
