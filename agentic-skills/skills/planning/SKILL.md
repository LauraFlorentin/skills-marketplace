---
name: planning
description: A high-level cognitive pattern where an agent formulates a structured sequence of actions (a plan) before executing any of them, ensuring goal-directed behavior. Use when user asks to "add planning to my agent", "task planning", "agent planning", or mentions plan generation, plan execution, or step-by-step planning.
---

# Planning

Planning (sometimes called "Reasoning & Acting") decouples the strategy from the execution. Instead of reacting immediately to a user request, the agent pauses to decompose the goal into sub-goals, identifies dependencies, and creates an ordered list of steps. This allows agents to tackle complex, multi-step problems that require foresight.

## Use Cases

-   **Travel Itinerary**: Searching for flights, hotels, and activities, then checking availability, then booking.
-   **Software Development**: Designing a system -> Writing code -> Writing documentation.
-   **Data Analysis**: Plan -> Data Collection -> Cleaning -> Analysis -> Visualization.

## Implementation Pattern

```python
def planning_workflow(goal):
    # Step 1: Create Plan
    # The planner generates a list of steps, not the actual work.
    plan = planner_agent.run(
        prompt="Create a step-by-step plan to achieve this goal...",
        input=goal
    )
    
    results = {}
    
    # Step 2: Execute Plan
    for step in plan.steps:
        # Check dependencies
        if not check_dependencies(step, results):
            raise RuntimeError(f"Cannot execute {step.id}: dependencies are incomplete")
            
        # Execute the specific step using a worker agent
        result = worker_agent.run(
            prompt=f"Execute this step: {step.description}",
            context=results # Pass context from previous steps
        )
        
        results[step.id] = result
        
    # Step 3: Summarize
    return synthesizer_agent.run(results)
```
