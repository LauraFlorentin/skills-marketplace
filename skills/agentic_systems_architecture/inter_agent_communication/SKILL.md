---
name: Inter-Agent Communication
description: Protocols and patterns that allow independent agents to exchange messages, negotiate, and collaborate across network boundaries or process isolation.
---

# Inter-Agent Communication

Inter-Agent Communication defines the language and transport layer for agents to talk to each other. In a distributed system, Agent A (Booking) might run on a different server than Agent B (Payment). They need a standard way to find each other (Discovery), send requests (Messaging), and understand the data format (Protocol).

## When to Use

-   **Microservices Architecture**: Breaking a monolithic agent into smaller, deployable services.
-   **Ecosystem Integration**: Allowing your agent to talk to agents built by other teams or companies.
-   **Asynchronous Tasks**: "Fire and forget" tasks where Agent A sends a job to Agent B and checks back later.
-   **Load Balancing**: Distributing tasks across a pool of identical agents.

## Use Cases

-   **Agent Marketplace**: An agent searches a registry to find a "Translation Agent" and hires it for a task.
-   **Supply Chain**: A "Retail Agent" sends a restock order to a "Warehouse Agent", which confirms availability.
-   **Delegation**: A "Personal Assistant Agent" delegates a math problem to a specialized "Wolfram Alpha Agent".

## Implementation Pattern

```python
# Conceptual A2A (Agent-to-Agent) Interaction

class AgentA:
    def run(self):
        # Step 1: Discovery
        # Find an agent that supports the 'payment' skill
        payment_agent_url = directory.lookup(skill="process_payment")
        
        # Step 2: Messaging (HTTP/RPC)
        # Send a structured request
        payload = {
            "task": "pay_invoice",
            "amount": 100,
            "currency": "USD"
        }
        
        response = http.post(f"{payment_agent_url}/inbox", json=payload)
        
        # Step 3: Handle Response
        if response.status == "CONFIRMED":
            print("Payment successful")
```
