# Interview Guides — Detailed Reference

Detailed frameworks, templates, and field-level guidance. Read when SKILL.md directs you here.

---

## Cross-Interview Synthesis

### Affinity Mapping

Take findings from 20+ interviews and organize into patterns.

**Process:**
1. Extract key quotes/insights on index cards or stickies
2. Lay them all out
3. Look for patterns: Which insights cluster together?
4. Move cards into groups based on theme
5. Create higher-level categories
6. Name each category with a theme

**Example:**

Raw insights:
- "We spend 40% of our time on exceptions"
- "System doesn't handle special orders"
- "Manual work-around for international orders"
- "Rules engine is limited; we're doing business logic in spreadsheets"
- "Approval process can't handle edge cases"
- "We have dozens of different workflows"

Organized themes:

**Theme: Process Inflexibility**
- System doesn't handle special orders
- Rules engine is limited; doing business logic in spreadsheets
- System can't handle all order types; we have workarounds

**Theme: Exception Handling Burden**
- 40% of team time on exceptions
- Approval process can't handle edge cases
- We have dozens of different workflows
- Manual work-arounds for international orders

Higher-level insight: **System constraints driving high manual/exception work = cost + quality risk**

### Theme Identification

Look across all interviews for:

**Frequency:** How many respondents mentioned this?
- Consensus themes (90%+ mention): Critical finding
- Strong themes (70-90%): Very important
- Moderate themes (50-70%): Important
- Weak themes (<50%): May be individual concerns

**Intensity:** How strongly did they feel?
- Passionate language, emotion, repeated emphasis = high intensity
- Examples: "frustrating," "waste," "love," "would never work"

**Impact:** How important is this issue?
- Does it affect revenue/cost/risk?
- Does it affect customer experience?
- Does it touch multiple functions?

**Examples:**

| Theme | Frequency | Intensity | Impact | Importance |
|-------|-----------|-----------|--------|-----------|
| Approval bottleneck takes 2-3 days | 85% | High (frustrated language) | Delays 20% of orders | Critical |
| System UI is hard to learn | 60% | Medium | Extends training time | Moderate |
| Lack of real-time visibility | 90% | High (repeated emphasis) | Kills customer service, creates workarounds | Critical |
| Compensation doesn't incentivize efficiency | 70% | Medium (resigned tone) | Misaligned incentives, poor adoption risk | Important |

### Contradiction Resolution

When you have contradictory findings, investigate:

**Scenario:** Finance says approval process takes 30 min; Operations says 2-3 days.

**Dig deeper:**
- Finance person: Describes actual approval time (their time)
- Operations person: Describes queue time (waiting for approval)

**Resolution:** Approval is 30 min; bottleneck is queue waiting time (process handles limited volume)

**Lesson:** When contradiction exists, likely different perspectives on same issue. Dig into the specifics.

### Synthesis Output: Insight Summary

Create a 5-10 page summary:

**Page 1: Executive Summary**
- 2-3 key findings
- 2-3 major pain points
- Recommended direction

**Pages 2-3: Finding Details**
- Each key finding: What did we hear? From how many people? What's the impact?
- Include quotes from interviews
- Anonymize: Don't attribute to individuals

**Pages 4-5: Pain Point Analysis**
- Each major pain point
- Who experiences it? How often? What's the impact?
- Underlying root causes
- How would stakeholders fix it (their ideas)

**Pages 6-7: Preliminary Hypotheses** (if appropriate)
- Based on interviews, here's what we think should change
- Pressure-tested with stakeholders in interviews
- Next steps for validation

## Presenting Interview Findings

### Anonymization

**Do:**
- Quote by role: "As the operations manager told us..."
- Aggregate findings: "80% of team members mentioned approval delays"
- Reference function: "The finance team noted..."
- Use titles/roles: "Controllers told us..."

**Don't:**
- Name individuals: "Sarah Chen said..."
- Quote unique details that identify person: Avoid very specific or unusual comments that would point to one person
- Attribute controversial views to individuals
- Use direct quotes with identifying details

**Example of poor practice:** "John, VP of Finance, disagreed with the new system approach"
**Better:** "Finance leadership expressed concerns about system selection criteria"

### Quoting Techniques

**Strong quotes to illustrate themes:**

Good quotes are:
- Concise (under 15 words if possible)
- Specific (not vague)
- Illustrative of broader theme
- Not overly negative/inflammatory

**Example:**
- Weak: "The system doesn't work well."
- Strong: "We spend 40% of our time on manual exceptions the system can't handle."

**Multiple quotes to illustrate one theme:**
- Quote 1 (Ops): "We have workarounds for everything."
- Quote 2 (Finance): "Approval process can't handle edge cases."
- Quote 3 (IT): "Rules engine has limitations we've hit."

**Integrating quote with analysis:**

"Operations described high exception volumes as a fundamental constraint. As one process owner noted, 'We spend 40% of our time on manual exceptions.' Finance and IT corroborated this, citing system limitations preventing handling of edge cases. The implication: current process inflexibility is driving significant non-value work."

### Connecting Themes to Recommendations

**Interview finding → Implication → Recommendation**

Example chain:

1. **Finding:** 85% of respondents cited approval delays (2-3 days)
2. **Implication:** Approval process is sequential bottleneck; limited by single approval resource; creates queue time
3. **Root cause:** Process design (all orders to one person) + system inability to pre-route
4. **Recommendation:** Implement tiered approval (3-tier model based on order amount); system auto-routes based on tier

**Another example:**

1. **Finding:** Ops and Finance have different views of "fast"—Ops thinks 4 hours; Finance says overnight acceptable
2. **Implication:** Misaligned definitions of success; unclear what we're optimizing for
3. **Root cause:** No shared metrics or SLA; process designed without clear requirement
4. **Recommendation:** Establish order-to-cash SLA (definition, targets, governance); cascade to sub-processes

## Common Interview Mistakes

| Mistake | How It Happens | How to Avoid |
|---------|---|---|
| **Leading questions** | Unconscious bias; want to validate hypothesis | Write questions before interview; review for bias; ask neutrally |
| **Confirmation bias** | Hear what you expect; ignore contradictions | Listen for disconfirming evidence; ask "tell me why you think that"; revisit surprising answers |
| **Talking too much** | Nervous; want to fill silence; explain yourself | Prepare questions ahead; practice listening; use silence |
| **Surface-level answers** | Ask closed question; accept first answer | Probe with follow-ups; chain probing for roots; use scenarios |
| **Interviewing the wrong people** | Talk to people in office; miss frontline; skip executives | Plan sample deliberately; talk to doers, managers, leaders, customers |
| **Not adjusting questions based on earlier interviews** | Ask same questions rigidly | Reflect after each interview; adjust questions for next wave based on learnings |
| **Failing to capture decisions and accountability** | Focus on "what" not "who" | Explicitly ask: "Who decides?" "Who owns this?" "Who would need to approve?" |
| **Too many interviews** | Try to talk to everyone; dilutes insights | Target 20-30 strategic interviews; get breadth and depth |
| **Writing up notes weeks later** | Memory fades; lose detail | Write up notes within 24 hours; capture while fresh |
| **Assuming findings are universal** | One function's view = everyone's | Test findings across functions; look for consensus, not individual views |

## Interview Sampling Strategy

### Determining Sample Size

**Rule of thumb:** 20-30 interviews sufficient for most engagements to reach saturation (no new themes emerging).

**More interviews needed (40-50) if:**
- Highly distributed organization (offices in 5+ locations)
- Highly functional (need deep expertise in 8+ functions)
- Change program (need buy-in from many stakeholders)

**Fewer interviews OK (10-15) if:**
- Engagement very focused (single process, single location)
- Clear SMEs available
- Previous recent engagement (can reference prior findings)

### Sample Composition

**Strategic sampling (not random):**

| Sample Group | Count | Reason |
|---|---|---|
| **Process owners** | 3-5 | Understand current process, key decisions, pain points |
| **Practitioners** | 8-12 | Day-to-day reality, workarounds, detailed pain points |
| **Managers** | 4-6 | People strategy, team capacity, change perspective |
| **IT/System owners** | 2-3 | Technical constraints, roadmap, feasibility |
| **Finance/Business stakeholders** | 2-3 | Financial drivers, business priorities, ROI perspective |
| **Leadership** | 2-3 | Strategic context, governance, decision-making |
| **Customers** | 2-3 | External perspective, pain points, unmet needs |
| **TOTAL** | 25-35 | |

### Interview Schedule

**Week 1-2:**
- Interviews with process owners and key leaders
- Allow questions to evolve based on early learnings

**Week 2-3:**
- Interviews with practitioners (bulk of interviews)
- Test emerging themes

**Week 3-4:**
- Targeted interviews (deep dives on specific areas, customer interviews)
- Validation interviews on preliminary hypotheses

## Interview Guides Deliverables

### Template 1: Interview Guide

```
ENGAGEMENT: Order-to-Cash Process Improvement
DATE PREPARED: March 5, 2024
INTERVIEW TYPE: Discovery

OBJECTIVES
Understand current order-to-cash process and key pain points across operations, finance, and IT

SAMPLE COMPOSITION
- Process owner: 1-2 interviews
- Finance operations: 3-4 interviews
- Approval/management level: 2-3 interviews
- IT systems: 1-2 interviews
- Total: 8-10 interviews

TIME & LOGISTICS
- Duration: 50 minutes
- Scheduling: Send 2-week calendar invite with intro/overview
- Location: Their office (in-person preferred for first interviews) or Teams
- Recording: "May I record for my notes? This is just for my reference; not shared."

INTERVIEW PROTOCOL

[INTRO & RAPPORT - 2 min]
"Thanks for taking the time to chat. I'm [name] with [consulting firm]. We're working with [client] on improving their order-to-cash process. I'm interviewing people across the organization to understand how it works today and where we see opportunities. Anything you share is confidential; I won't attribute comments to you in reports. I'll take notes and we'll wrap in about 50 minutes. Sound good?"

[CONTEXT SETTING - 3 min]
"Just to set context: We're looking at how orders flow from entry through fulfillment and cash collection. Your role is critical to understanding how this works. I appreciate you sharing your perspective."

[CORE QUESTIONS - 30 min]

1. [WALK THROUGH] "Walk me through your typical day. What do you spend most of your time on?"
   - [Probe]: "Tell me more about [task]"
   - [Probe]: "How often does that happen?"

2. [CURRENT PROCESS] "Now let's focus on the order-to-cash process specifically. Walk me through how an order flows from receipt to cash collection. What are the steps? Who's involved?"
   - [Probe]: "You mentioned [step]. Tell me more about what happens there. How long does it take? Who does it?"
   - [Probe chain]: "You said it takes 2-3 days for approval. Why?" → "Why isn't [person] available?" → "What prevents them from prioritizing this?"

3. [VOLUME & VARIABILITY] "How many orders go through this process? What percentage flow smoothly? What percentage have problems?"
   - [Probe]: "When something goes wrong, what typically causes it?"
   - [Probe]: "Give me an example of an order that had issues. What happened?"

4. [PAIN POINTS] "What's the biggest pain point in this process for you? What takes too much time? What frustrates you?"
   - [Probe]: "Tell me about the last time that happened. What was the impact?"
   - [Probe]: "How often does this happen? What's the cost?"

5. [WORKAROUNDS] "How do you work around the system when it doesn't do what you need?"
   - [Probe]: "What would it be like if you didn't have these workarounds?"
   - [Probe]: "How many people are spending time on workarounds?"

6. [FUTURE STATE] "If you could redesign this process, what would you keep? What would you change?"
   - [Probe]: "What would that enable? What would be the benefit?"

7. [DECISION MAKING] "How are decisions made about changes to this process? Who would need to approve a change? Who has the most influence?"
   - [Probe]: "What would convince [decision-maker] to approve a change?"

[PROBING - 10 min]
- Dig deeper on themes/surprising findings
- Test any preliminary hypotheses

[WRAP-UP - 5 min]
"Is there anything I haven't asked that you think is important for me to know?"
"If you could tell leadership one thing about this process, what would it be?"
"Who else should I talk to? Who has good perspective on this area?"
"May I follow up if I need clarification?"
[Thank them sincerely]

NOTES FOR INTERVIEWER
- Listen more than talk (aim for 70% them talking, 30% you talking)
- Don't be defensive if they critique current state
- Acknowledge their pain points: "That sounds frustrating"
- Probe when you hear interesting themes
- Capture verbatim quotes for good illustrative comments
- Take notes on tone/energy/engagement level
- Mark confusing areas so you can ask follow-up questions later
```

### Template 2: Interview Summary (Post-Interview)

```
DATE: March 10, 2024 | TIME: 2:00-2:50 PM
NAME: Sarah Chen | ROLE: Senior Operations Manager, Order Fulfillment
TENURE: 8 years in role
ENGAGEMENT: Order-to-Cash Process Improvement

KEY INSIGHTS

Volume & Current Process
- Process ~500 orders/day, 2,500/week
- Order entry → Validation → Credit check → Approval → Fulfillment → Billing → Cash app
- For standard orders: ~4 hours start to cash received. For exceptions: 2-5 days
- Systems: Legacy order system + SAP + Excel spreadsheets for workarounds

Pain Points (ranked by frequency/intensity)
1. Approval bottleneck: Takes 2-3 days
   - "All large orders ($10K+) require VP Finance approval. He's in meetings constantly. We can't move forward until he approves."
   - Impact: 20% of orders delayed; customer complaints; late cash receipts
   - Frequency: Daily issue

2. System inflexibility: 40% of time spent on exceptions
   - "We have workarounds for everything. If order doesn't fit the standard box, system can't handle it."
   - Examples: International orders, custom pricing, multi-leg shipments, revenue recognition
   - Impact: High labor cost; quality risk; scalability limited

3. No visibility: Finance and operations see different data
   - "We have no real-time view of what's pending approval or stuck in fulfillment."
   - Impact: Customer service can't answer questions; leadership flying blind

Workarounds
- Excel tracking spreadsheets (replicate system data)
- Manual escalation process for exceptions (email, calls, meetings)
- Local agreements/exceptions documented in emails, not system
- Data entry sometimes happens 2x (order system + SAP)

Decision Making
- VP Finance has final approval authority
- Process owner tries to pre-screen, but VP doesn't delegate
- No clear SLA or approval criteria

Future State Ideas
- "We need faster approval. Tiering by risk would help: small orders auto-approve, medium delegated, large to VP."
- "If system could handle international orders natively, we'd save hours."
- "Real-time dashboard showing status would transform how we work."

Sentiment
- Engaged and thoughtful (high energy throughout)
- Frustrated by approval bottleneck (noted multiple times with emotion)
- Pragmatic about system constraints ("we've learned to work around them")
- Positive about organization but realistic about improvements needed

Referrals
- John Martinez (VP Finance) for approval process perspective
- Maria Gonzalez (IT systems) for technical constraints
- James Chen (Customer service) for customer impact

INTERVIEWER NOTES
- Sarah is a credible voice; been here 8 years; deep process knowledge
- Frustration seems legitimate (not personality-driven); systemic issues
- Interesting tension: She's accepted workarounds as "normal" but acknowledges they're not sustainable
- Would be good to involve her in solution design (she has good ideas)

PRELIMINARY THEMES TO VALIDATE IN NEXT INTERVIEWS
1. Approval is a universal bottleneck (heard from process owner; test with finance)
2. Exception handling is a big cost driver (heard from ops; test with finance/IT)
3. System limitations driving manual work (heard from ops; test with IT on feasibility)
```

### Template 3: Cross-Interview Synthesis

```
SYNTHESIS REPORT: Order-to-Cash Process Discovery
INTERVIEWS COMPLETED: 28 across functions
DATE COMPLETED: March 22, 2024
INTERVIEWER: [Name]

KEY FINDINGS

1. APPROVAL PROCESS IS CRITICAL BOTTLENECK
   Frequency: 85% mentioned (23/28 respondents)
   Intensity: High (frustrated language, emphasis on impact)
   Details:
   - 2-3 day median wait time for approval (VP Finance approval required for $10K+ orders)
   - 20% of orders delayed waiting for approval
   - Process designed for much lower volume (historical artifact)
   - Root cause: Single decision-maker (VP Finance); no delegation; volume exceeds capacity

   Quotes:
   - "All large orders bottleneck at one person's desk" (Operations)
   - "We can't move forward until he signs off" (Sales manager)
   - "I'm available 4 hours/week for approvals; we need 20 hours" (VP Finance) ← Honest acknowledgment

   Impact:
   - Customer delays and complaints
   - Late cash collection
   - Sales friction (sales team frustrated)
   - Operational stress (team working around the constraint)

2. SYSTEM INFLEXIBILITY DRIVES HIGH MANUAL WORK
   Frequency: 90% mentioned (25/28 respondents)
   Intensity: High (described as "frustrating," "waste," "daily problem")
   Details:
   - ~40% of operations team time spent on exceptions
   - System handles "happy path" but breaks on: international orders, custom pricing, multi-leg shipments, revenue recognition nuances
   - Team has built Excel workarounds (spreadsheets replicate system data)
   - Manual data entry sometimes happens 2x (order system + SAP)

   Quotes:
   - "We have workarounds for everything" (Operations manager)
   - "System can't handle what our business actually does" (Finance analyst)
   - "We lose data in translation between systems" (IT)

   Impact:
   - High labor cost ($200K+ per year in exception handling)
   - Data quality risk (manual entry, multiple systems of truth)
   - Scalability limitation (can't handle more volume without proportional labor)
   - Adoption risk (new team members take weeks to learn workarounds)

3. NO REAL-TIME VISIBILITY INTO ORDER STATUS
   Frequency: 78% mentioned (22/28 respondents)
   Intensity: Medium-high
   Details:
   - Finance, operations, customer service see different views of order status
   - No integrated dashboard
   - Customer service reps can't answer customer questions ("Is my order approved?")
   - Leadership doesn't have real-time metrics on process performance

   Quotes:
   - "Customer asks status; I have to email three people" (Customer service rep)
   - "I don't know what's stuck in fulfillment" (Finance)

   Impact:
   - Poor customer experience
   - Operational inefficiency (time spent searching for status)
   - Limited leadership visibility into process

4. ORGANIZATION HAS GROWTH ASPIRATIONS; CURRENT PROCESS WILL LIMIT IT
   Frequency: 73% mentioned (20/28 respondents, mostly leadership)
   Intensity: High
   Details:
   - Company planning 25% volume growth in next 2 years
   - Current process already breaking at current volume
   - Headcount scaling not feasible (would need +15 FTE just to handle exceptions)

   Quotes:
   - "If we grow 25%, our manual process breaks. We need to automate." (VP Operations)
   - "We need system to handle complexity, not more people." (CFO)

   Impact:
   - Strategic constraint: Can't execute growth strategy with current process/system

PAIN POINT INVENTORY (by function)

Operations (High impact)
- Approval delays (85% mentioned)
- Exception handling burden (90%)
- Lack of visibility (75%)
- System inflexibility (95%)

Finance (High impact)
- Approval queue (85%)
- System limitations (80%)
- Data quality (60%)
- Manual reconciliation (55%)

IT (Moderate impact)
- System limitations (acknowledge but=lower urgency)
- Integration gaps (70%)
- Scalability concerns with growth (60%)

Sales (High impact)
- Approval delays impacting customer response time (70%)
- Lack of visibility (60%)

Customer Service (Moderate impact)
- Can't answer customer questions (78%)
- Manual status lookups (60%)

ORGANIZATIONAL DYNAMICS
- Operations & Finance misaligned on approval criteria (different views of "high risk")
- Operations sees Finance as bottleneck; Finance sees operations as disorganized
- Sales and operations have different urgencies (speed vs. control)
- Leadership alignment on need to fix this (CFO, VP Ops, VP Sales all want change)
- VP Finance (approval authority) is aware of bottleneck; willing to delegate with proper governance

PRELIMINARY RECOMMENDATIONS (hypothesis to validate)

1. Implement tiered approval model
   - Auto-approve orders <$10K (87% of volume)
   - Delegate $10-50K to operations manager with set criteria
   - VP Finance reviews >$50K and exceptions
   - Expected impact: Reduce approval time from 2-3 days to <4 hours

2. Implement new system with exception handling
   - Evaluate cloud-native solutions that handle international orders, custom pricing, etc.
   - Possible candidates: Salesforce, SAP Commerce Cloud, specialized O2C suites
   - Expected impact: Reduce exception handling from 40% to <15% of time; reduce manual rework

3. Build integrated dashboard for real-time visibility
   - Single system of truth for order status
   - Accessible to operations, finance, sales, customer service
   - Real-time metrics on order volume, approvals, fulfillment, cash
   - Expected impact: Improved customer service, leadership visibility, faster problem resolution

NEXT STEPS
1. Validate recommendations with stakeholder validation interviews (Week of April 1)
2. Get financial impact analysis (cost of current process, ROI of improvements)
3. Assess system feasibility and options
4. Create business case with implementation roadmap
```

---

**Key Principles for Effective Interviews:**
- **Listen more than talk:** Your job is to understand, not convince
- **Dig deeper:** Surface answers are rarely root causes; probe to understand why
- **Stay neutral:** Don't lead; don't bias; don't show your hypothesis
- **Capture specifics:** Quotes, examples, data points; avoid vague generalizations
- **Interview strategically:** Talk to doers, managers, leaders, customers—get multiple perspectives
- **Synthesize across interviews:** Look for patterns, not individual opinions
- **Act quickly:** Write up notes within 24 hours; synthesize while findings are fresh
- **Use findings to inform, not confirm:** Let interviews surprise you and change your thinking
