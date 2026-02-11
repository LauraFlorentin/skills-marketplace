---
name: Human-in-the-Loop
description: A hybrid pattern where the system pauses execution to request human approval, input, or disambiguation before proceeding with critical actions.
---

# Human-in-the-Loop

Human-in-the-Loop (HITL) bridges the gap between full automation and manual control. It treats the human user as a "privileged tool" or "approver". This is crucial for high-stakes domains where AI errors are unacceptable, or for ambiguous tasks where human intuition is required to guide the agent.

## When to Use

-   **High Consequence**: Transferring money, deploying code to production, sending emails to customers.
-   **Ambiguity Resolution**: When the user's intent is unclear ("Book me a flight" -> "Which day?").
-   **Active Learning**: Collecting human feedback to improve the model (RLHF).
-   **Quality Assurance**: Reviewing the final draft of a report before publication.

## Use Cases

-   **Approval Workflow**: Agent drafts a reply -> Human approves/edits -> Agent sends.
-   **Escalation**: Chatbot handles simple queries -> Escalates to human support for complex issues.
-   **Clarification**: Agent: "I found 3 files. Which one do you mean?" -> Human selects.

## Implementation Pattern

```python
def hitl_workflow(user_request):
    # Step 1: Plan/Draft
    plan = agent.create_plan(user_request)
    
    # Step 2: Risk Assessment
    if is_high_risk(plan):
        # Step 3: Pause for Approval
        # Send notification to user UI
        approval = notify_user(
            message="Agent wants to execute the following plan:",
            payload=plan
        )
        
        if approval.status == "REJECTED":
            return "Action cancelled by user."
        elif approval.status == "EDITED":
            plan = approval.new_plan
            
    # Step 4: Execute
    return agent.execute(plan)
```
