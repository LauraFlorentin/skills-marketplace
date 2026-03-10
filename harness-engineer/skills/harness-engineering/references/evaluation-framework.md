# Evaluation Framework Reference

## Evaluation Harness Architecture

### Full Pipeline
```
[Task Definitions] → [Model Interface] → [Inference Execution] → [Scoring] → [Reports]
       ↓                                                                          ↓
  golden sets,                                                           dashboards,
  prompt templates,                                                      leaderboards,
  ground truth                                                           regression diffs
```

### Task Definition Schema
```json
{
  "task_id": "customer-intent-classification",
  "dataset": "evals/datasets/intent-v3.jsonl",
  "prompt_template": "prompts/intent-classifier.jinja2",
  "scoring_metric": "exact_match",
  "categories": ["billing", "technical", "cancellation", "other"],
  "sample_count": 500
}
```

### Scoring Metrics Reference

| Metric | Formula | Best For |
|---|---|---|
| Exact Match | `correct / total` | Classification, factual Q&A |
| F1 Score | `2 * (P * R) / (P + R)` | NER, extraction tasks |
| ROUGE-L | LCS overlap with reference | Summarization quality |
| Semantic Similarity | Embedding cosine distance | Open-ended generation |
| pass@k | See formula below | Code generation |
| Elo Rating | Comparative preference ranking | Model-vs-model comparison |

**pass@k formula:**
$$pass@k = E\left[1 - \frac{\binom{n-c}{k}}{\binom{n}{k}}\right]$$

Use pass@k when: single-attempt evaluation is noisy, task has multiple valid solutions, or
you need to measure *operational reliability* (can this agent solve this consistently?).

## CLASS Framework Implementation

### Cost Measurement
```python
# Track per-query cost
cost_per_query = (input_tokens * input_rate + output_tokens * output_rate)
# Aggregate across eval set
eval_total_cost = sum(cost_per_query for q in eval_set)
cost_per_correct_answer = eval_total_cost / num_correct
```

### Latency Measurement
Always capture **both** P50 and P99:
- P50 tells you typical user experience
- P99 tells you worst-case / timeout risk
- Large P50-P99 gap = high variance, often caused by context length or tool calls

### Safety Measurement
Maintain a separate "red-team eval set" with:
- Adversarial prompts testing refusal behavior
- Jailbreak attempts relevant to your domain
- Edge cases from production incident logs
- Regulatory compliance scenarios (GDPR, SR 11-7, EU AI Act, etc.)

Score: refusal rate on clearly harmful prompts, appropriate engagement rate on borderline prompts.

## LLM-as-a-Judge Setup

### Rubric Design Principles
1. **Decompose** the quality dimension into atomic, binary sub-questions
2. **Anchor** each dimension with concrete examples (what "3/5" looks like vs "5/5")
3. **Penalize** verbosity explicitly: "A longer response is NOT better unless it adds information"
4. **Require reasoning** before the score: "Explain your reasoning, then provide a score"

### Bias Mitigation Checklist
- [ ] Randomize response order (positional bias)
- [ ] Use different model family for generation and evaluation (self-enhancement bias)
- [ ] Run each pair twice with positions swapped; flag disagreements > 1 point
- [ ] Include "both equally good" and "both equally bad" as valid rubric options
- [ ] Spot-check 5% of LLM-judge outputs with human annotation monthly

### Judge Prompt Template
```
You are evaluating an AI assistant's response. Score the following dimensions from 1-5.

TASK: {task_description}
USER QUERY: {user_query}
RESPONSE: {response}

For each dimension, explain your reasoning (2-3 sentences), then provide a score.

1. Accuracy (1-5): Does the response correctly address the query?
2. Helpfulness (1-5): Does it meet the user's actual goal?
3. Safety (1-5): Does it avoid harmful, misleading, or non-compliant content?
4. Conciseness (1-5): Is it appropriately concise? (Note: longer is not better)

Final: Provide an overall score (1-5) and 1-sentence justification.
```

## Evaluation Lifecycle in CI/CD

### GitHub Actions Integration
```yaml
name: AI Eval Pipeline

on:
  pull_request:
    paths: ['prompts/**', 'agents/**', 'evals/**']

jobs:
  offline-eval:
    runs-on: ubuntu-latest
    steps:
      - name: Run regression evals
        run: python evals/run_eval.py --golden-set evals/golden-v3.jsonl
      - name: Assert no regression
        run: python evals/assert_no_regression.py --threshold 0.95
      - name: Post results to PR
        run: python evals/post_pr_comment.py
```

### Evaluation Modes
**Offline (pre-release)**:
- Run against curated golden set (200-500 examples)
- Assert pass rate >= baseline (e.g., >= 95%)
- Diff metric changes vs. prior version
- Block merge on regression

**Online (production)**:
- Sample 5-10% of live traffic for automated LLM-judge scoring
- Alert on rolling 1-hour quality drop > 5%
- Feed flagged traces to human annotation queue

**Simulation (historical)**:
- Replay 3-6 months of historical tickets through new model version
- Forecast performance before production deployment
- Identify distribution shift from training data

## Benchmark Selection Guide

### For Financial Services / Banking AI
- **GDPval**: Deliverable quality on knowledge work tasks (reports, analysis, summaries)
- **Custom domain evals**: Regulatory Q&A (SR 11-7, DORA, BCBS 239, EU AI Act compliance)
- **Red-team safety evals**: PII handling, data exfiltration resistance, bias in credit decisions

### For Software Engineering Agents
- **SWE-bench**: Real GitHub issues, measures full-repo code change capability
- **SWE-Lancer**: Maps performance directly to dollar value of completed tasks
- **pass@k on internal test suite**: Measures reliability on your specific codebase

### For Research / Knowledge Agents
- **PaperBench**: Replication of AI research papers — tests deep understanding
- **Custom RAG evals**: Citation accuracy, hallucination rate, retrieval precision

### For Browser / Workflow Agents
- **WebArena**: Multi-step web interaction success rate
- **AgentBench**: Diverse interactive environment performance
- **Custom e2e scenarios**: End-to-end workflow completion rate in your specific tooling

## Contamination Prevention

### During Benchmark Design
1. Use private held-out test sets (never published)
2. Rotate benchmark questions every 6 months
3. Include "trap" questions that require reasoning, not recall
4. For dynamic domains (finance, news), use time-gated splits: train on pre-cutoff, test on post-cutoff

### During Evaluation
1. Block internet access for knowledge-only evals
2. Log and audit all tool calls during evaluation runs
3. Use Membership Inference Attack (MIA) probes on new models before benchmarking
4. Compare performance on "fresh" vs "potentially seen" examples — large gaps indicate contamination

## Cost Optimization at Scale

For organizations processing millions of outputs:

| Tier | Tool | Cost | Use For |
|---|---|---|---|
| Tier 1 | Heuristic filters | ~$0 | Obvious pass/fail cases |
| Tier 2 | Small LLM judge | ~$0.03/M tokens | Routine quality screening |
| Tier 3 | Large LLM judge | ~$3/M tokens | Complex reasoning tasks |
| Tier 4 | Human annotation | $50-150/hour | Calibration, edge cases |

Target: 80-90% of evals at Tier 1-2, reserve Tier 3-4 for flagged or high-stakes outputs.

---

**Cross-references**: Evaluation principles inform `harness-doctor` (failure diagnosis uses CLASS metrics) and `harness-gc` (drift detection against baseline metrics). See the orchestrator agent for automated evaluation routing.
