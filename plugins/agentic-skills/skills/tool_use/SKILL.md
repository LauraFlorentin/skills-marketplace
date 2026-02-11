---
name: Tool Use
description: The capability that transforms an LLM from a text generator into an agent by allowing it to execute actions and retrieve information from the real world.
---

# Tool Use

Tool Use (or Function Calling) is the core mechanism of agency. It allows an LLM to recognize when it needs external information or needs to perform an action. Instead of hallucinating an answer, the model outputs a structured command (like a JSON object) to call a specific function (e.g., `get_weather(city="London")`). The system executes the function and feeds the result back to the model.

## When to Use

-   **Real-time Data**: When the answer requires current information (stock prices, weather, sports scores).
-   **Computational Tasks**: When precise math or data processing is needed (using a calculator or Python REPL).
-   **System Interaction**: When the agent needs to modify the environment (sending emails, updating databases, creating files).
-   **Private Data Access**: Querying internal knowledge bases or APIs.

## Use Cases

-   **Search**: Integrating Google Search or Bing to answer current events questions.
-   **Code Execution**: Using a Python sandbox to generate charts or analyze CSV files.
-   **API Integration**: Connecting to Slack, Jira, or GitHub to automate workflows.

## Implementation Pattern

```python
def tool_use_loop(user_query):
    messages = [{"role": "user", "content": user_query}]
    
    # Available tools definition
    tools = [{
        "name": "get_stock_price",
        "parameters": {"symbol": "string"}
    }]
    
    # Step 1: Agent decides to call a tool
    response = llm.chat(messages, tools=tools)
    
    if response.tool_calls:
        # Step 2: System executes the tool
        tool_call = response.tool_calls[0]
        result = execute_tool(tool_call.name, tool_call.arguments)
        
        # Step 3: Result is fed back to the Agent
        messages.append(response.message) # Keep the assistant's "intent"
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": str(result)
        })
        
        # Step 4: Agent generates final answer using tool result
        final_answer = llm.chat(messages)
        return final_answer
        
    return response.content
```
