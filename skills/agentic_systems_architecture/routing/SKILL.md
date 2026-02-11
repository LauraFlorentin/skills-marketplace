---
name: Routing
description: A control flow pattern where a central component classifies an input request and directs it to the most appropriate specialized agent or tool.
---

# Routing

Routing acts as the traffic controller for an agentic system. Instead of a single generalist agent trying to handle every type of user request, a "Router" (often a fast, lightweight LLM or a classifier) analyzes the intent of the incoming message and delegates it to a specialized handler. This creates a system that is modular, scalable, and easier to maintain.

## When to Use

-   **Specialization**: When you have diverse tasks that require different prompts, tools, or context (e.g., Tech Support vs. Sales vs. Refund).
-   **Cost Optimization**: To route simple queries to smaller/cheaper models and complex queries to reasoning models.
-   **Security**: To ensure sensitive requests are handled by agents with stricter guardrails.
-   **SoC (Separation of Concerns)**: To keep individual agent prompts focused and clean.

## Use Cases

-   **Customer Service Dispatch**: Routing "My internet is down" to Tech Support and "How much is the upgrade?" to Sales.
-   **Model Selection**: Routing logic puzzles to o1 and creative writing to GPT-4.
-   **Tool Selection**: Deciding whether to use a Search tool, a Calculator, or a Database Query tool based on the question.

## Implementation Pattern

```python
def routing_workflow(user_query):
    # Step 1: Classification
    # The router's only job is to pick the right path.
    intent = classify_intent(
        prompt="Classify this query into: [SALES, SUPPORT, BILLING]",
        input=user_query
    )
    
    # Step 2: Delegation
    # Based on the intent, we call a specific sub-agent.
    if intent == "SALES":
        return sales_agent.run(user_query)
    elif intent == "SUPPORT":
        return support_agent.run(user_query)
    elif intent == "BILLING":
        return billing_agent.run(user_query)
    else:
        return default_agent.run(user_query)
```
