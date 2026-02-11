---
name: Resource-Aware Optimization
description: A routing pattern that optimizes for cost and latency by dynamically selecting the most efficient model or tool for a given task complexity.
---

# Resource-Aware Optimization

Not every task requires the smartest, most expensive model. Resource-Aware Optimization (or Dynamic Routing) classifies the complexity of a user request and routes it to the most appropriate model tier. This ensures you aren't using a sledgehammer to crack a nut, saving money and improving speed.

## When to Use

-   **High Volume APIs**: When 10% of requests are complex and 90% are simple.
-   **Latency Sensitivity**: Routing simple "Hello" or "Stop" commands to instant, small models.
-   **Budget Constraints**: Ensuring high-end models (like GPT-4 or Opus) are only used when absolutely necessary.
-   **Fallback**: Using a small model first, and only upgrading to a large model if the small one fails/expresses low confidence.

## Use Cases

-   **Tiered Chatbot**: 
    -   Simple (Greetings, FAQs) -> gpt-4o-mini
    -   Medium (Summarization, extraction) -> gpt-4o
    -   Complex (Coding, Reasoning) -> o1-preview
-   **Cascade**: Try Llama-70B -> if confidence < 0.8 -> Try GPT-4.
-   **SLA-based**: Free users -> Small Model. Paid users -> Large Model.

## Implementation Pattern

```python
def optimize_resources(task):
    # Step 1: Complexity Analysis
    # Use a very cheap model or heuristics
    complexity = classifier.classify(task)
    
    # Step 2: Dynamic Selection
    if complexity == "SIMPLE":
        model = "gpt-4o-mini"
    elif complexity == "HARD":
        model = "gpt-4o"
    else:
        model = "o1-preview" # For reasoning heavy tasks
        
    print(f"Routing to {model} for efficiency.")
    
    # Step 3: Execute
    return llm.generate(task, model=model)
```
