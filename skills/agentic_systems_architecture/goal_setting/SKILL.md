---
name: Goal Setting & Monitoring
description: An iterative pattern where an agent defines clear success criteria and continuously evaluates its progress, adjusting its actions until the goal is achieved.
---

# Goal Setting & Monitoring

Goal Setting is the process of defining *what* success looks like before starting work. Monitoring is the continuous loop of checking "Are we there yet?". Together, they allow an agent to maintain focus over long horizons. Instead of executing a single prompt, the agent enters a loop: **Act -> Observe -> Evaluate -> Adjust**.

## When to Use

-   **Open-Ended Tasks**: "Write a high-quality blog post." (Requires iterative refinement).
-   **Code Generation**: "Write code that passes all tests." (Requires Act -> Test -> Fix loop).
-   **Autonomous Agents**: When the agent must operate without human intervention for a period.
-   **Ambiguous Instructions**: To force the agent to clarify what "done" means.

## Use Cases

-   **Test-Driven Development (TDD)**: Goal = "All tests pass". Loop: Write code -> Run tests -> Fix errors -> Repeat.
-   **Research**: Goal = "Find 5 sources". Loop: Search -> Count sources -> Search more if < 5.
-   **Content Polish**: Goal = "Score > 8/10 on readability". Loop: Rewrite -> Evaluate -> Rewrite.

## Implementation Pattern

```python
def goal_loop(objective, criteria):
    # Step 1: Initialize
    current_state = get_initial_state()
    iterations = 0
    max_iterations = 10
    
    while iterations < max_iterations:
        # Step 2: Check Goal
        status = evaluator.check(
            goal=objective, 
            criteria=criteria, 
            current_state=current_state
        )
        
        if status.is_complete:
            return current_state
            
        print(f"Goal not met: {status.feedback}")
        
        # Step 3: Act to reduce gap
        # The agent sees the feedback and tries to fix it.
        action = planner.decide_next_step(
            goal=objective, 
            feedback=status.feedback
        )
        current_state = execute(action)
        
        iterations += 1
        
    raise TimeoutError("Goal not reached within iteration limit.")
```
