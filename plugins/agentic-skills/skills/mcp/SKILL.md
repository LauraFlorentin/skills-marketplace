---
name: Model Context Protocol (MCP)
description: An interoperability standard that allows AI models to connect to external data and tools securely and consistently, decoupling the tool implementation from the agent.
---

# Model Context Protocol (MCP)

The Model Context Protocol (MCP) forces a separation between the *definition* of a tool (the server) and the *consumption* of a tool (the client/agent). Instead of hardcoding API integrations inside your agent's codebase, you build an MCP Server that exposes resources (data) and tools (functions). Any MCP-compliant agent can then discover and use these tools without custom glue code.

## When to Use

-   **Standardization**: When building an ecosystem of tools that many different agents need to use.
-   **Security**: To expose internal data safely without giving the LLM direct database access.
-   **Modularity**: To keep your agent logic clean and focused on reasoning, while the MCP server handles the "dirty work" of API connections.
-   **Portability**: Tools built with MCP can be used by Claude Desktop, IDEs, and custom agents alike.

## Use Cases

-   **Database Access**: An MCP server that exposes safe SQL queries as tools.
-   **File System**: An MCP server that allows an agent to read/write files in a sandboxed directory.
-   **API Wrapper**: An MCP server that wraps the GitHub API, exposing actions like `create_issue` or `list_prs`.

## Implementation Pattern

```python
# MCP Server Implementation (Conceptual)
from fastmcp import FastMCP, tool

# Create a server
mcp = FastMCP("MyTools")

# Expose a tool
@mcp.tool()
def calculate_vat(amount: float, country: str) -> float:
    """Calculates VAT for a given country."""
    rate = get_rate(country)
    return amount * rate

# The Agent (Client) simply connects to this server
# and automatically "sees" the calculate_vat tool available for use.
# client.connect(mcp_server)
# response = client.chat("How much VAT for 100 EUR in Germany?")
```
