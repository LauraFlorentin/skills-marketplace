---
name: Exception Handling & Recovery
description: Patterns for ensuring system resilience by detecting failures (API errors, hallucinations, validation errors) and executing predefined fallback logic.
---

# Exception Handling & Recovery

Exception Handling ensures that an agentic system degrades gracefully rather than crashing. In the nondeterministic world of LLMs, failures are common: models hallucinate, APIs time out, and outputs are malformed. This pattern wraps critical operations in "try/catch" blocks that trigger recovery agents or fallback strategies.

## When to Use

-   **Production Systems**: Essential for any user-facing application.
-   **Unreliable Tools**: When using 3rd-party APIs that might be down or rate-limited.
-   **Structured Output**: When the model occasionally fails to output valid JSON.
-   **Safety**: When a tool might return dangerous or unexpected data.

## Use Cases

-   **API Fallback**: "Primary model API failed? Switch to backup model API." or "Tool A failed? Try Tool B."
-   **Refusal Handling**: If the model refuses to answer (due to safety filters), catch the refusal and rephrase the prompt or explain why it can't answer.
-   **Validation Repair**: If JSON validation fails, pass the error back to the model to fix the syntax.

## Implementation Pattern

```python
def resilient_tool_call(tool_name, args):
    max_retries = 3
    
    for attempt in range(max_retries):
        try:
            # Try to execute the tool
            return execute_tool(tool_name, args)
            
        except RateLimitError:
            # Specific handling for known errors
            backoff_sleep(attempt)
            
        except ValidationError as e:
            # Self-Correction: Ask the model to fix its input
            print(f"Validation failed: {e}. Asking model to fix...")
            args = repair_agent.fix_inputs(tool_name, args, error=e)
            
        except Exception as e:
            # General fallback
            log_error(e)
            return fallback_strategy(tool_name)
            
    raise SystemError("Max retries exceeded")
```
