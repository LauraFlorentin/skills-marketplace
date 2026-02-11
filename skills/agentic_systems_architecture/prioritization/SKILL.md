---
name: Prioritization
description: A management pattern where an agent assesses the urgency and importance of incoming tasks to organize a dynamic execution queue.
---

# Prioritization

Prioritization allows an agent to work smarter, not just harder. Instead of processing tasks First-In-First-Out (FIFO), a "Manager Agent" analyzes each request's urgency and business value. It assigns a priority score (P0, P1, P2) and reorders the queue effectively. This is vital for resource-constrained environments.

## When to Use

-   **Queue Management**: When the system receives more requests than it can handle instantly.
-   **SLA Enforcement**: Ensuring premium users or critical alerts get processed first.
-   **Resource Allocation**: Assigning the smartest (and most expensive) models to P0 tasks, and cheaper models to P2 tasks.
-   **Triage**: Filtering out spam or low-value requests entirely.

## Use Cases

-   **Ticket Triage**: Analyzing support tickets and tagging them as "Critical" (Server Down) or "Low" (Typo).
-   **Inbox Management**: Sorting emails by "Needs Reply", "Read Later", and "Spam".
-   **Agent Dispatch**: A Project Manager agent assigning urgent bugs to Senior Dev Agents and documentation tasks to Junior Agents.

## Implementation Pattern

```python
def prioritization_loop(task_queue):
    while True:
        # Step 1: Ingest
        new_request = ingest_request()
        
        # Step 2: Assess Priority
        # Manager agent determines importance
        priority_score = manager_agent.evaluate(
            prompt="Rate urgency 1-10",
            input=new_request
        )
        
        # Step 3: Insert into Priority Queue
        task_queue.push(new_request, priority=priority_score)
        
        # Step 4: Process Highest Priority
        next_task = task_queue.pop()
        worker_agent.run(next_task)
```
