# The AI-Augmented M&A Playbook
### Slash Commands · Deliverables · Workflow Chains

> **A practical, opinionated guide for senior M&A consultants on structuring AI into daily deal workflows.**  
> Synthesized from current adoption patterns at Goldman Sachs, Lazard, PwC/Harvey AI, McKinsey, Bain, and leading boutiques.

---

## Preface: Why Generic AI Fails in M&A

The traditional M&A lifecycle is characterized by compressed timelines, extreme data fragmentation, and high-stakes information asymmetry. Analysts and consultants routinely spend 70–90-hour weeks manually parsing virtual data rooms, cross-referencing poorly structured financials, and redlining dense legal contracts. This brute-force model is no longer competitive.

But the answer is **not** a generic chatbot. Generic AI tools fail in the M&A context because they lack understanding of corporate structures, financial nuances, and complex legal language. The productivity gains — firms report **35% faster deal completion**, **20% cost reduction**, and **23% higher seller valuations** — go to teams that deploy AI in *highly specialized, repeatable workflows*.

This guide is that toolkit: purpose-built slash commands, structured deliverable templates, and end-to-end workflow chains designed for live deal work. Every command assumes an enterprise AI environment (Claude Enterprise, Harvey, or equivalent) with document upload capability. **Never upload confidential deal materials to public consumer AI tools.**

---

## Part 1: Daily Slash Commands

Slash commands are reusable, pre-engineered prompt architectures mapped to recurring M&A tasks. Think of them as precision macros: type a trigger phrase, feed in deal-specific context, receive a structured output. The goal is to shift the consultant's time from data gathering and formatting to strategic judgment and client interaction.

The following 12 commands cover the full deal lifecycle — origination through integration.

---

### Command Reference Table

| # | Command | Trigger Phrase | What It Does | Time Saved / Why It Matters |
|---|---------|---------------|--------------|----------------------------|
| 1 | `/cim-extract` | *"Extract historical EBITDA, proposed adjustments, and the primary defensibility narratives from the attached CIM."* | Bypasses sell-side marketing rhetoric to isolate concrete financials, margin trends, customer concentration, revenue quality indicators, and risk disclosures. Flags inconsistencies between narrative sections and financial tables. | **3–5 hrs → 20 min per CIM.** Enables rapid screening of dozens of inbound opportunities without getting lost in glossy formatting. Inconsistency flagging catches issues humans miss under time pressure. |
| 2 | `/vdr-classify` | *"Classify and auto-folder these raw VDR uploads into standard DD categories based on document content."* | Scans unstructured files using NLP and OCR; identifies document types (cap tables, IP licenses, vendor contracts, tax returns); applies standardized naming conventions and folder hierarchies across thousands of misfiled documents. | **10+ hrs per VDR drop.** Eliminates the administrative black hole of organizing poorly named seller documents — creating a diligence-ready environment from day one instead of day three. |
| 3 | `/redline-nda` | *"Review this bidder markup against our standard 24-month confidentiality playbook and generate a counter-draft."* | Compares counterparty NDA markups against the firm's pre-approved negotiation playbook. Flags unacceptable deviations (non-solicit duration, confidentiality term reductions, permitted disclosure expansion). Accepts benign formatting changes; reverts substantive deviations for senior partner review. | **60–90 min → 5 min per NDA.** In a sell-side auction with 30–100 NDAs, this reclaims days of associate time while maintaining consistent, defensible positions across all bidders. |
| 4 | `/flag-coc` | *"Scan these material contracts for change-of-control provisions, assignment restrictions, and termination-for-convenience clauses."* | Executes a semantic search — not just keyword matching — across hundreds of vendor, supplier, and customer contracts to identify clauses triggered by ownership change. Compiles findings into an actionable risk register with recommended pre-close consent requests. | **20+ hrs during Legal DD.** Non-standard CoC provisions can threaten revenue continuity post-close. Semantic understanding catches bespoke phrasing that keyword searches consistently miss. |
| 5 | `/synergy-map` | *"Compare the target's back-office headcount and vendor lists with the buyer's organization to identify redundancies."* | Digests employee census, benefits structures, and third-party spend ledgers from both entities. Normalizes taxonomies and job titles; identifies overlapping back-office functions, duplicate software licenses, and redundant vendor relationships — with dollar values attached. | **15+ hrs per synergy model.** Replaces manual cross-referencing of incompatible corporate data systems. Output is what lenders require for debt underwriting — third-party validation of proposed synergies. |
| 6 | `/draft-qna` | *"Draft a response to this buyer diligence question using the approved Phase 2 disclosure schedules and VDR Index."* | Synthesizes approved internal data to formulate precise, defensible answers to buy-side diligence inquiries. Auto-routes each response for expert approval. Prevents inconsistencies in seller representations across a multi-bidder process. | **30 min per query × hundreds of questions.** Eliminates the coordination nightmare of routing, chasing, and formatting Q&A responses while maintaining strict confidentiality boundaries. |
| 7 | `/mgmt-qa` | *"Generate 30 likely buyer questions for the management presentation on [Target] in [Industry], with 'green flag' and 'red flag' answer benchmarks for each."* | Produces a structured Q&A prep book organized by theme — revenue quality, competitive positioning, margin sustainability, key person risk, growth credibility — with explicit evaluation criteria per answer. Flags the 5 questions most likely to surface hidden risk. | **8–12 hrs → 2 hrs.** The green/red flag framework transforms passive prep into an active evaluation tool. Junior team members stop collecting answers and start knowing what to probe. |
| 8 | `/screen-fdi` | *"Screen the target's revenue footprint across these jurisdictions against current antitrust and FDI threshold triggers."* | Cross-references geographic revenue distribution, physical asset locations, and customer footprint against global FDI and merger control thresholds. Flags mandatory filing jurisdictions, estimated timelines, and specific triggers (CFIUS, EU FDI Screening, UK NSI Act, Reverse CFIUS for China-adjacent tech). | **8+ hrs preliminary legal research → same day.** Catches jurisdictional filing obligations that experienced cross-border practitioners occasionally miss. Critical for timeline forecasting and risk allocation in definitive agreements. |
| 9 | `/schedule-disclosure` | *"Draft the initial material contracts disclosure schedule mapping to Section 3.14 of the Purchase Agreement."* | Extracts data from the VDR to populate initial drafts of disclosure schedules. Pulls contracts above defined thresholds, aggregates equity grants, and checks for internal consistency against the main operative agreement. | **12+ hrs of manual drafting.** Reduces the risk of omitted liabilities or misaligned representations between schedules and the definitive agreement — a common source of post-close indemnification claims. |
| 10 | `/culture-diag` | *"Analyze the target's internal communication protocols and decision frameworks to highlight cultural friction points with the acquirer."* | Evaluates unstructured behavioral data — decision velocity, approval hierarchies, meeting cadence, cross-departmental communication patterns (where legally permissible and fully anonymized) — to identify fundamental operational incompatibilities. | **Days of subjective interviewing → objective behavioral baseline.** Cultural mismatch is the #1 cited cause of PMI failure. AI enables proactive change-management design before Day 1. |
| 11 | `/dd-flag` | *"Review these uploaded documents and issue log. Rate each finding by severity, map to deal impact, and identify documentation gaps."* | Assigns severity ratings (Critical / Material / Notable / Minor), maps each issue to a deal impact category (valuation, structure, integration, regulatory), and surfaces gaps — documents requested but not received, or workstreams with suspiciously few findings. | **Continuous savings across 6–8 week DD process.** The gap analysis is the real value: AI flags conspicuous absence of findings in areas that warrant investigation — a blind spot human reviewers routinely miss. |
| 12 | `/model-commentary` | *"Write DCF commentary covering: revenue assumption credibility, margin bridge logic, WACC derivation, sensitivity interpretation, and a 2-sentence conclusion on whether the DCF supports the proposed price range."* | Generates publication-ready valuation narrative from raw model outputs. Covers assumption rationale, margin bridge, WACC derivation with justification for each input, and sensitivity interpretation in the voice of a senior banker presenting to a client board. | **4–8 hrs → 1–2 hrs.** Converts spreadsheet outputs into persuasive client-facing narrative — the translation junior analysts consistently struggle with. Senior bankers refine rather than originate. |

---

### On AI Limitations: A Necessary Flag

These commands are powerful, but they are not infallible. Large language models currently cannot independently verify the economic substance of related-party transactions for tax purposes, nor can they perfectly interpret highly subjective legal standards — such as what constitutes a "Material Adverse Effect" under varying jurisdictional case law. AI can also identify the *legal existence* of a finding while missing its *commercial significance*. All outputs in definitive legal agreements and final deliverables must remain strictly advisory, with rigorous human validation at every stage. The risk of catastrophic liability exposure from unreviewed AI outputs in M&A is real and well-documented.

---

## Part 2: High-Value Reports & AI-Assisted Deliverables

While slash commands accelerate micro-tasks, the ultimate output of an advisory engagement is the formal, structured deliverable. The eight reports below represent the highest-leverage documents in the deal lifecycle — the ones that dictate valuation, govern risk allocation, market the company, and serve as the binding blueprint for integration. AI compresses drafting timelines dramatically; human judgment remains essential for strategic interpretation, negotiation positioning, and the subjective calls that determine deal outcomes.

---

### 1. Confidential Information Memorandum (CIM)

**Purpose:** The single most important sell-side marketing document. Bridges buyer curiosity and the decision to submit an IOI by presenting the target in its optimal commercial light — highlighting competitive moats, financial trajectory, and strategic expansion opportunities to maximize bidding tension.

**M&A Phase:** Origination & Marketing

| Section | Analytical Focus |
|---------|-----------------|
| Executive Summary | Investment thesis and transaction rationale in plain language |
| Company Overview | Corporate evolution, milestones, and precise ownership structure |
| Market & Industry Analysis | TAM/SAM, macroeconomic tailwinds, competitive positioning |
| Products & Services | Core offerings, revenue models, pricing strategy, customer value proposition |
| Sales & Marketing | CAC, LTV, churn rates, pipeline velocity, NRR |
| Management & Employees | Leadership biographies, org structure, cultural attributes |
| Financial Results & Projections | Historical income statements, balance sheets, management-adjusted 5-year forecast |

**AI Application:** A comprehensive 60-page CIM historically takes 4–6 weeks to finalize. AI synthesizes raw internal data into cohesive narrative drafts for the Market Analysis and Operations sections. It cross-references internal KPIs against external industry benchmarks to stress-test competitive positioning claims. For financial sections, AI maps messy historical GL data to formatted, management-adjusted EBITDA presentations — dramatically reducing iteration cycles. Senior advisors focus on deal positioning and narrative differentiation rather than formatting.

---

### 2. Indication of Interest (IOI) Memorandum

**Purpose:** A non-binding letter expressing a prospective buyer's quantified intent to acquire. Serves as an early screening mechanism, demonstrating valuation logic, financial capacity, and strategic alignment before committing resources to expensive confirmatory diligence.

**M&A Phase:** Initial Bidding & Negotiation

| Section | Analytical Focus |
|---------|-----------------|
| Purchase Price Range | Enterprise valuation estimate expressed as an EBITDA multiple range |
| Proposed Transaction Structure | Asset vs. stock, cash / equity rollover / seller note / earn-out mix |
| Sources of Financing | Proof of funds, committed equity capital, anticipated leverage levels |
| Key Assumptions | Financial/operational metrics the valuation relies upon |
| Due Diligence Scope | Remaining access required to reach a definitive agreement |
| Timing & Approvals | Estimated timeline to LOI; internal IC approvals required |

**AI Application:** When a buy-side firm evaluates multiple targets simultaneously, generating customized IOIs rapidly is a competitive differentiator. Chain `/cim-extract` → comps analysis → `/synergy-map` to produce the valuation range, comparable context, and synergy upside. The AI then drafts the IOI, mapping the buyer's strategic advantages directly to the CIM's growth pillars — making the offer feel bespoke and strategic to the seller rather than a generic form letter. The entire origination-to-bid cycle can complete before competing firms have scheduled their initial review meetings.

---

### 3. Red Flag Due Diligence Report

**Purpose:** A rapid-assessment diagnostic identifying critical deal-breakers and severe valuation risks before executing definitive agreements. Unlike a comprehensive legal diligence report, the red flag report is exception-based — focused exclusively on systemic liabilities and structural threats.

**M&A Phase:** Confirmatory Due Diligence

| Section | Analytical Focus |
|---------|-----------------|
| Executive Risk Summary | Prioritized dashboard of critical findings by severity and valuation impact |
| Corporate Governance & Capitalization | Unresolved equity claims, missing board consents, undocumented stock options |
| Material Contracts | Onerous CoC provisions, exclusivity clauses, single-supplier concentration, unfavorable termination rights |
| Intellectual Property | Unsecured chain of title, open-source contamination in proprietary code, infringement litigation |
| Regulatory & Compliance | Pending investigations, data privacy exposure, environmental liabilities |
| Labor & Employment | Contractor misclassification, unfunded pension liabilities, key executive flight risk |

**AI Application:** This is the most direct application of AI pattern recognition in the deal lifecycle. Chain `/vdr-classify` → `/flag-coc` → `/dd-flag` to ingest, structure, and analyze the VDR continuously as documents arrive. The AI compares contracts, permits, and corporate records against a predefined risk database — flagging missing IP assignment clauses, undocumented equity issuances breaking the cap table, and anomalous GL entries made immediately pre-deal launch. The consultant applies commercial and legal judgment: direct price reduction, indemnification carve-out, or deal-breaker. PwC's Harvey integration executes this workflow over 10,000 times per engagement.

---

### 4. Financial Due Diligence (Quality of Earnings) Report

**Purpose:** An independent assessment of the target's true financial health. Validates sustainability of historical earnings, verifies normal working capital requirements, and uncovers hidden, off-balance-sheet debt-like liabilities. The QoE directly dictates final purchase price adjustments and protects the buyer from overpaying for inflated performance.

**M&A Phase:** Confirmatory Due Diligence

| Section | Analytical Focus |
|---------|-----------------|
| Quality of Earnings Summary | Bridge between reported EBITDA and definitive, run-rate adjusted EBITDA |
| Revenue & Margin Analysis | Customer concentration, product mix profitability, volume vs. price trend analysis |
| EBITDA Adjustments | Detailed schedules defending or refuting management's proposed add-backs |
| Net Working Capital Analysis | Historical NWC peg, cash-flow seasonality, aged receivables, obsolete inventory |
| Debt and Debt-Like Items | Off-balance-sheet liabilities, deferred revenue, unpaid executive bonuses, unfunded capex |

**AI Application:** The foundational QoE labor is the "tie-out" process — ensuring trial balances reconcile with audited financials, bank statements, and tax returns over a 3–5 year lookback. AI automates this ingestion and reconciliation. When a trial balance uploads, AI maps granular account codes to standard FDD groupings and detects GL anomalies — unexplained expense spikes, unusual journal entries immediately pre-deal launch — that manual review misses under fatigue. `/model-commentary` drafts routine descriptive sections; human expertise focuses on the subjective, negotiated debates over valid EBITDA add-backs and the definitive working capital peg.

---

### 5. Synergy & Cost Savings Analysis Report

**Purpose:** Systematically identifies, quantifies, and validates value enhancement opportunities that justify the acquisition premium. Moves beyond historical earnings to detail exactly how the combined entity will reduce run-rate costs, achieve operational scale, and drive accretion.

**M&A Phase:** Valuation & Due Diligence

| Section | Analytical Focus |
|---------|-----------------|
| Synergy Thesis & Strategy | Strategic rationale for the cost-takeout plan and integration philosophy |
| Headcount & Organizational Overlap | Quantified cost reductions from consolidating duplicate corporate and back-office roles |
| Third-Party Spend Rationalization | Savings from renegotiating vendors, consolidating professional services, combined purchasing leverage |
| Technology & Infrastructure | ERP migration, redundant software license elimination, real estate consolidation |
| Phase-In Timeline | Year-by-year realization schedule (standard 20/50/80/100% curve over years 1–4) |
| Costs to Achieve | Severance packages, lease break fees, IT migration costs |
| Three Scenarios | Conservative / base / stretch with explicit assumption differences and NPV of each |

**AI Application:** `/synergy-map` normalizes disparate data from two distinct corporate operating systems, standardizes job titles, and clusters overlapping vendor spend — generating specific line items like "Duplicate Cloud Hosting Costs: $2.3M" or "Overlapping Regional Sales Management: 14 FTE." This quantitative foundation is what lenders require for debt underwriting. The consultant's role shifts to validating assumptions and assessing execution risk — the place where synergy models most commonly fail, and where human judgment is irreplaceable.

---

### 6. Management Presentation (Equity Story) Deck

**Purpose:** A highly visual, compelling narrative delivered live by the target's management team to prospective buyers. Projects vision, operational culture, and future expansion potential — the ultimate pitch for valuation maximization.

**M&A Phase:** Management Meetings & Diligence

| Section | Analytical Focus |
|---------|-----------------|
| Vision & Market Leadership | The foundational "why," competitive moat, and authentic corporate values |
| Historical Performance Review | Key inflection points and strategic decisions driving past growth |
| Go-To-Market Strategy | Expansion vectors, up-sell/cross-sell opportunities, channel strategy |
| 5-Year Forecast | Financial roadmap and core assumptions driving projected growth |
| Platform Value & Synergy Potential | Explicit discussion of how a specific acquirer benefits from the combination |

**AI Application:** Translating a dense 60-page CIM into a dynamic 25-slide management presentation historically consumes dozens of hours of junior analyst time in PowerPoint. AI extracts KPIs and narrative arcs from approved financials and CIM content, generates the storyboard, drafts executive summaries for each slide, and formats complex financial tables into digestible visuals. This frees senior advisors to coach management on authentic delivery and simulate aggressive buyer Q&A — the work that determines whether buyers leave the room impressed or skeptical.

---

### 7. Regulatory Risk Summary

**Purpose:** Maps all regulatory approval requirements across jurisdictions, identifies the critical path to closing, and flags deal structure elements that could trigger extended review or prohibition.

**M&A Phase:** Due Diligence / Negotiation

| Section | Analytical Focus |
|---------|-----------------|
| Jurisdiction Map | Every country requiring a filing, with statute, threshold, and mandatory/voluntary status |
| Timeline Analysis | Expected review period; Phase I vs. Phase II scenarios; critical path jurisdiction |
| Antitrust Risk Assessment | Market definition, combined market shares, HHI analysis, enforcement precedent |
| FDI & National Security | CFIUS, EU FDI Screening Regulation, UK NSI Act, sector-specific triggers |
| Remedies Analysis | Likely divestiture or behavioral commitment requirements; impact on deal economics and synergy capture |
| Reverse CFIUS | U.S. outbound investment screening for Chinese AI/semiconductor/quantum deals (effective Jan 2, 2025) |
| Recommended Strategy | Filing sequencing, pre-filing engagement recommendations, contingency planning |

**AI Application:** `/screen-fdi` generates the initial jurisdictional roadmap. Regulators now scrutinize innovation control and ecosystem dominance beyond traditional market share metrics — the regulatory surface area is expanding faster than institutional knowledge. AI catches filing triggers in secondary jurisdictions that experienced practitioners occasionally miss. Reverse CFIUS is new enough that many deal teams are still building institutional knowledge — AI trained on the final rule text costs dramatically less than specialist counsel at $1,500+/hour for initial screening.

---

### 8. Post-Merger Integration (PMI) Target Operating Model

**Purpose:** A rigorous, actionable blueprint for combining two entities post-close. Establishes governance structure, minimizes business disruption, and ensures tracked realization of underwritten financial synergies.

**M&A Phase:** Pre-Close Planning & Post-Close Integration

| Section | Analytical Focus |
|---------|-----------------|
| Integration Governance | Steering committee structure, escalation protocols, IMO roles and accountabilities |
| Day 1 Readiness Checklist | Payroll continuity, legal entity transfer, systems access, initial communications |
| Functional Workstreams | 100-day execution plans for HR, IT, Finance, Operations, Legal, Go-to-Market |
| Systems & IT Architecture | Application rationalization roadmap, secure data migration, infrastructure consolidation |
| Cultural Integration & Change Management | Retention strategies, benefit rationalization, internal communication sequencing |
| Synergy Realization Tracker | Actual vs. planned realization by category with variance explanations |
| RAID Log | Open risks, actions, issues, and decisions by severity with trend indicators |

**AI Application:** The consultant prompts the AI with specific deal parameters ("Draft a Day 1 Readiness plan for a carve-out acquisition in the regulated manufacturing sector"). AI generates workstream charters populated with standard timelines, risk registers, and cross-functional dependency maps. `/culture-diag` outputs feed directly into the change management section. For cross-border deals: AI cross-references employment law by jurisdiction, GDPR data transfer requirements, currency management procedures, and tax structure implementation checklists. Cultural sensitivity, leadership messaging, and key stakeholder relationships remain irreducibly human — this is where the senior consultant earns their fee.

---

## Part 3: Workflow Chains

The highest evolution of AI in M&A advisory is the **workflow chain** — the strategic sequencing of slash commands and report generators into continuous, end-to-end pipelines. Individual commands save hours; chains compress multi-week processes into days.

---

### Chain 1: Origination to IOI
**Time compressed from 5–7 days to ~4 hours**

When a high-quality asset hits the market, the speed of evaluation and bid submission directly determines auction participation. Late followers get outbid or excluded.

**Step 1 — CIM Extraction (0:00–0:20)**  
Run `/cim-extract` on the uploaded CIM. Output: structured financial table, customer concentration analysis, growth driver ranking, risk flags, and one-paragraph investment thesis. Verify accuracy — CIMs frequently contain inconsistencies between their narrative sections and detailed financial tables.

**Step 2 — Comps & Valuation Range (0:20–0:50)**  
Feed extracted financials into a comps analysis. Output: trading comps table with 8–12 peers, transaction comps with 5–10 precedent deals, implied valuation range. Adjust the peer group for any companies with materially different business models.

**Step 3 — Synergy Sizing (0:50–1:15)**  
Run `/synergy-map` using CIM extraction outputs and knowledge of the acquirer's operations. Output: three-scenario synergy bridge with phase-in curves. The senior consultant's role: does the headcount overlap and procurement leverage pass the smell test for this specific industry?

**Step 4 — IOI Drafting (1:15–1:50)**  
Draft the IOI using the three AI outputs as building blocks. Apply judgment: where in the valuation range do you bid, what conditions do you attach, how do you frame strategic rationale to differentiate from other bidders?

**Step 5 — Regulatory Pre-Check (1:50–2:00)**  
Run `/screen-fdi` to identify any regulatory filing requirements affecting timeline or certainty. Include material findings in the IOI's conditions section.

*The senior consultant's time shifts from data gathering to deal positioning — the output that actually wins mandates.*

---

### Chain 2: VDR Drop to Initial Red Flag Report
**Time compressed from 5 days to 6 hours**

When a buyer gains access to the sell-side VDR, the race to uncover liabilities begins. Delays create deal fatigue and erode negotiating leverage.

**Step 1 — Ingestion & Classification**  
Initiate `/vdr-classify`. The AI ingests a 5,000-file document dump, categorizing files into Legal, Financial, HR, and Operational folders with standardized nomenclature. The buy-side team arrives to a diligence-ready environment rather than document chaos.

**Step 2 — Semantic Risk Extraction**  
Chain `/flag-coc` and `/schedule-disclosure` simultaneously. The AI hunts for structural legal risks in commercial contracts while extracting core representations on capitalization and employee benefits.

**Step 3 — Issue Triage**  
Run `/dd-flag` across all extracted findings. Output: severity-rated issue register with deal impact mapping and gap analysis — identifying not just what was found, but what's conspicuously absent.

**Step 4 — Red Flag Report Population**  
Route all outputs into the Red Flag DD Report template. The AI populates the Executive Risk Summary with CoC triggers, environmental liabilities, and EBITDA-to-CIM discrepancies.

**Step 5 — Consultant Review**  
The senior consultant reviews the pre-populated report the next morning, refines the legal interpretations, applies commercial judgment, and delivers actionable intelligence to the IC days ahead of schedule — preventing resources from being committed to a fatally flawed asset.

---

### Chain 3: Synergy Underwriting to Day 1 Integration Readiness
**Time compressed from 3 weeks to 3 days**

Once the Purchase Agreement is signed and purchase price is locked, speed of integration execution directly determines synergy capture or leakage.

**Step 1 — Quantitative Synergy Mapping**  
Execute `/synergy-map`. Output: overlapping operational footprints, redundant software licenses, duplicated vendor contracts, overlapping administrative headcount — all with dollar values attached.

**Step 2 — Synergy Report Generation**  
Compile outputs into the Synergy & Cost Savings Analysis Report. This provides PE sponsors, corporate boards, and syndication lenders with the empirically validated data required to secure acquisition financing.

**Step 3 — Integration Risk Assessment**  
Run `/culture-diag` and `/dd-flag` to populate the integration risk register. Rate cultural, operational, customer, regulatory, and synergy execution risks. Adjust synergy phase-in curves based on risk ratings — if IT consolidation scores High risk, extend the IT-related synergy timeline by 6–12 months.

**Step 4 — PMI Plan Generation**  
Chain validated synergy data directly into the PMI Target Operating Model. The AI takes identified headcount redundancies and auto-populates the HR workstream's 30-day severance and retention planning checklist. Duplicate vendor lists populate IT and Procurement workstreams with specific contract termination dates, notice periods, and penalty fee calculations.

**Step 5 — Day 1 Readiness Checklist**  
Generate the final checklist, cross-referencing purchase agreement closing conditions, TSA term sheet, and integration plan. For cross-border deals: add employment law compliance by jurisdiction (TUPE, works council consultations, labor authority notifications), GDPR data transfer mechanisms, currency and cash management, and tax structure implementation.

*The transition from theoretical valuation modeling to an executable Day 1 roadmap becomes seamless — AI handles the volume and cross-referencing; the consultant handles judgment, culture, and key stakeholder relationships.*

---

## Appendix: Adoption Context & Where to Start

The adoption curve is steep but uneven. McKinsey's January 2026 survey found **40% of AI-using deal teams achieved 30–50% faster deal cycles**. Bain projects **80% adoption by 2028** (up from 16% in 2023). Harvey AI reports **up to 75% time savings** on unstructured data room reviews. Kira Systems processes **450,000+ documents monthly** across 84% of the top 25 global M&A firms.

Most current usage is concentrated in document review and data extraction — the equivalents of `/cim-extract` and `/redline-nda`. Synergy modeling, integration planning, and regulatory screening are the frontier applications where early movers gain competitive advantage precisely because few firms have yet systematized AI workflows for these tasks.

**Three practical starting points:**

**1. Build your prompt library.** Start with the 12 commands above. Customize each to your firm's playbook, formatting standards, and negotiation positions. Iterate across 5–10 live deals to refine output quality.

**2. Invest in an enterprise platform.** Harvey, Claude Enterprise, or equivalent — not consumer chatbots. The requirements for live deal work: document upload capability, adequate context window, enterprise security posture, and data residency controls. Consumer tools fail on all four.

**3. Chain commands into workflows.** The compounding savings from the three chains above illustrate that the real leverage is sequential automation, not isolated prompts. Each chain is designed to produce board-ready intelligence by the time the next working day begins.

---

> *The firms that win the next cycle of M&A advisory are not those with the most AI tools — they are those that have embedded AI into repeatable, quality-controlled workflows that free senior professionals to spend their time on judgment, relationships, and strategy. The slash commands are the building blocks. The deliverable templates are the quality standard. The chains are how it all fits together on a live deal.*
