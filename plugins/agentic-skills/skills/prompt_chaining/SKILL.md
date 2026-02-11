---
name: Prompt Chaining
description: A fundamental pattern where the output of one LLM call serves as the input for the next, enabling complex tasks to be broken down into manageable sequential steps.
---

# Prompt Chaining

Prompt Chaining is the practice of decomposing a complex task into a series of smaller, sequential sub-tasks. Each sub-task is handled by a specific LLM call, with the output of one step feeding into the next. This approach improves reliability, testability, and allows for intermediate processing (like validation or formatting) between steps.

## When to Use

-   **Complex Transformations**: When a single prompt is too complex or prone to error (e.g., "Research topic X, then write an article, then translate it").
-   **Step-by-Step Logic**: When the logic requires a strict sequence of operations (e.g., Extract Data -> Validate Data -> Summarize Data).
-   **Token Limits**: When the input or intermediate context exceeds the context window of a single call.
-   **Debugging**: To isolate failures in a complex workflow by inspecting intermediate outputs.

## Use Cases

-   **Document Processing**: Extract text -> Summarize -> Translate -> Format as JSON.
-   **Code Generation**: Write tests -> Write code to pass tests -> Refactor code.
-   **Content Creation**: Generate outline -> Draft sections -> Polish tone -> Generate Title.

## Implementation Pattern

```python
def prompt_chain_workflow(input_data):
    # Step 1: Extraction
    # Focuses solely on getting the right data out of the raw input.
    extracted_data = llm_call(
        prompt="Extract key entities from this text...",
        input=input_data
    )
    
    # Optional: Deterministic Validation
    # We can run code check here before proceeding.
    if not validate(extracted_data):
        raise ValueError("Extraction failed")

    # Step 2: Transformation
    # Focuses on converting the data into the desired format/style.
    final_output = llm_call(
        prompt="Transform this extraction into a marketing summary...",
        input=extracted_data
    )
    
    return final_output
```
