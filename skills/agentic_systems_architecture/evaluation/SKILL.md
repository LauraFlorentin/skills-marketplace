---
name: Evaluation & Monitoring
description: Systems for quantitatively and qualitatively measuring agent performance, reliability, and cost.
---

# Evaluation & Monitoring

Evaluation determines *how well* an agent performs (correctness, helpfulness, safety), usually on a test dataset. Monitoring determines *how the system is running* (latency, errors, cost) in a live environment. Both are essential for the lifecycle management of AI systems.

## When to Use

-   **CI/CD**: Rejecting code changes if they drop accuracy below a threshold.
-   **A/B Testing**: Comparing Prompt A vs. Prompt B to see which users prefer.
-   **Cost Auditing**: Understanding which agents or tools are driving up the bill.
-   **Drift Detection**: Noticing if the model starts hallucinating more often on new data.

## Use Cases

-   **LLM-as-a-Judge**: Using GPT-4 to grade the answers of a smaller model.
-   **Latency Tracking**: Measuring the time-to-first-token (TTFT) and total generation time.
-   **Topic Clustering**: Analyzing user queries to see what topics are trending or failing.

## Implementation Pattern

```python
def evaluate_agent(agent, test_set):
    score = 0
    total = len(test_set)
    
    for case in test_set:
        # Run agent
        prediction = agent.run(case.input)
        
        # Evaluate vs Golden Answer
        # Simple exact match or fuzzy match
        if is_correct(prediction, case.expected):
            score += 1
        else:
            # Semantic Evaluation using an LLM Judge
            judge_score = llm_judge.evaluate(
                prediction, 
                case.expected
            )
            score += judge_score
            
    return score / total
```
