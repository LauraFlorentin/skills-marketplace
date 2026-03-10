---
name: strategy
description: Product vision, OKRs, and competitive analysis for startup and enterprise PMs — lean canvas, full vision docs, cascading objectives, feature parity grids, and positioning maps. Use when user asks to "write a product vision", "set OKRs", "competitive analysis", or mentions product strategy, lean canvas, positioning, or market analysis.
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

---

## References

For detailed templates, frameworks, and field-level guidance, read:

- [`references/strategy-reference.md`](references/strategy-reference.md) — Complete framework details, templates, and examples

Read this file when the task requires:
- OKRs
- Competitive Analysis
- Output Formats

