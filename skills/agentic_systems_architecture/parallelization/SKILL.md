---
name: Parallelization
description: A concurrency pattern where multiple agent tasks are executed at the same time to speed up processing or gather diverse perspectives.
---

# Parallelization

Parallelization allows an agentic system to perform multiple independent operations simultaneously. This is commonly used in distinct flavors: "Sectioning" (breaking a large task into independent chunks to process in parallel) and "Voting" (running the same task multiple times to get diverse outputs for consensus or increasing quality).

## When to Use

-   **Speed**: When tasks are independent and can be run concurrently to reduce total latency (e.g., verifying 5 different facts).
-   **Diversity**: When you want multiple creative options (e.g., generate 5 different headlines).
-   **Reliability**: When used in a "majority vote" pattern to reduce hallucinations (Self-Consistency).
-   **Aggregating Information**: Researching a topic from multiple sources simultaneously.

## Use Cases

-   **Batch Processing**: Grading 100 student essays concurrently.
-   **Multi-Perspective Analysis**: Asking a "Skeptic Agent", an "Optimist Agent", and a "Realist Agent" to review a plan simultaneously.
-   **Map-Reduce**: Identifying key themes in 50 documents by summarizing them all in parallel (Map) and then synthesizing the summaries (Reduce).

## Implementation Pattern

```python
import asyncio

async def parallel_workflow(topic):
    # Define independent tasks
    tasks = [
        research_agent.run(f"Research history of {topic}"),
        research_agent.run(f"Research economic impact of {topic}"),
        research_agent.run(f"Research cultural significance of {topic}")
    ]
    
    # Execute all concurrently
    # This takes as long as the slowest single task, not the sum of all tasks.
    results = await asyncio.gather(*tasks)
    
    # Synthesize results
    final_report = synthesize_agent.run(
        prompt="Combine these research findings into a report...",
        input=results
    )
    
    return final_report
```
