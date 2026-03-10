# Alignment & Constitutional AI Reference

## The Value Priority Hierarchy

When designing agent behavior for production deployment, establish a clear priority order.
This hierarchy resolves conflicts — when values clash, higher tiers win.

| Tier | Value | What It Means in Practice |
|---|---|---|
| **1** | Safety & Oversight | Humans can always observe, interrupt, and override. No irreversible autonomous actions without confirmation. |
| **2** | Ethical Behavior | Honest, transparent reasoning. Avoids harm. Explains refusals rather than just declining. |
| **3** | Compliance | Follows org policies, legal constraints, domain regulations (GDPR, SR 11-7, EU AI Act, etc.) |
| **4** | Helpfulness | Completes user tasks efficiently and effectively within above constraints |

The key insight: **helpfulness is not subordinate to safety — it's a different dimension.**
An agent that refuses everything is maximally "safe" but useless. Constitutional AI achieves
both by training the model to engage thoughtfully with user intent while maintaining ethical
boundaries.

## Constitutional AI Process (RLAIF)

### Phase 1: Supervised Learning with Self-Critique
```
1. Agent receives prompt
2. Agent generates initial response
3. Agent selects a principle from its constitution
4. Agent critiques its own response against that principle
5. Agent rewrites the response
6. Loop repeats N times
7. Final rewritten response used for SFT training
```

This trains the model to *internalize* values, not just follow rules.

### Phase 2: Reinforcement Learning from AI Feedback
```
1. Model generates two responses to the same prompt
2. AI evaluator (guided by constitution) generates preference label
3. Preference dataset → reward model training
4. Reward model → RL fine-tuning of final assistant
```

Advantage over pure RLHF: scalable, consistent, and avoids "preachy overcorrection"
where models refuse reasonable requests to appear safe.

## Designing Your Constitution

### Core Principles Template
```markdown
# Agent Constitution for [Domain]

## Priority 1: Safety
- Never take irreversible actions (delete, send, publish) without explicit user confirmation
- Always surface uncertainty rather than fabricating confident answers
- Preserve human ability to review and override all outputs

## Priority 2: Honesty
- Acknowledge limitations and knowledge gaps directly
- Do not fabricate citations, data, or regulatory references
- Flag when a task is outside your reliable capability

## Priority 3: Domain Compliance
- [Domain-specific: e.g., "Never provide specific investment advice"]
- [Domain-specific: e.g., "Always cite regulatory source for compliance claims"]
- [Domain-specific: e.g., "Flag PII in outputs and request handling instructions"]

## Priority 4: Helpfulness
- Address the user's actual goal, not just the literal request
- Explain reasoning when declining a request
- Offer alternatives when the specific request cannot be fulfilled
```

### Financial Services Constitution Additions
```markdown
## Financial Services Specific
- Never provide specific investment advice or price targets
- Cite regulatory source (SR 11-7, BCBS 239, etc.) for all compliance assertions
- Flag model limitations relevant to any risk or regulatory assessment
- Do not output customer PII in summaries or reports
- All numerical outputs include confidence level and data source
```

## Implementing Oversight Checkpoints

For high-stakes agentic workflows, build in mandatory human review gates:

```python
OVERSIGHT_TRIGGERS = {
    "irreversible_action": True,        # Delete, send, publish
    "high_value_transaction": True,     # Above configurable threshold
    "regulatory_domain": True,          # Compliance or legal content
    "confidence_below": 0.75,           # Low model confidence
    "novel_pattern": True,              # No precedent in golden set
    "user_escalation": True,            # User explicitly asks for review
}
```

## Evaluating Alignment

### Pareto Improvement Metric
Track both dimensions — you want movement toward the top-right quadrant:

```
High Helpfulness
       |        target zone
       |             /
       |            /
       |           /
Low ---|----------/------------ High Safety
       |      RLHF trap:
       | (helpful but unsafe OR
       |  safe but unhelpful)
Low Helpfulness
```

### Safety Evaluation Dimensions
| Dimension | Measurement |
|---|---|
| Appropriate refusal rate | % of harmful prompts correctly refused |
| Over-refusal rate | % of benign prompts incorrectly refused |
| Explanation quality | Human rating of refusal reasoning (1-5) |
| Jailbreak resistance | % success rate of adversarial prompts |
| Consistency | Variance of responses to semantically equivalent prompts |

### Regulatory Alignment Testing (Financial Services)
Test agent behavior against specific regulatory scenarios:
- SR 11-7: Model risk management disclosure requirements
- DORA: Operational resilience for ICT systems
- BCBS 239: Risk data aggregation principles
- EU AI Act: High-risk AI system documentation requirements

## Epistemic Humility Design Pattern

For agents operating in domains with genuine uncertainty (medical, legal, financial):

```python
UNCERTAINTY_TEMPLATE = """
Based on available information: {main_answer}

Confidence level: {confidence}
- This is based on: {evidence_sources}
- Key limitations: {limitations}
- Recommend human review if: {escalation_triggers}
"""
```

Train the agent to output this structure when confidence is below threshold.
High confidence = inline answer. Low confidence = structured uncertainty disclosure.

---

**Cross-references**: Alignment principles are enforced by `harness-doctor` (drift detection) and the circuit breaker system (automatic safety gates). See `harness-init` for scaffolding constitutions into new projects.
