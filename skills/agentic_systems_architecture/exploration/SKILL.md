---
name: Exploration & Discovery
description: An open-ended pattern where agents autonomously conduct research, generate hypotheses, and explore solution spaces without a predefined path.
---

# Exploration & Discovery

In the Exploration pattern, the goal is not to execute a known task, but to *find* new information or solutions. Agents act as scientists or researchers: they formulate a hypothesis, test it (by searching, coding, or simulating), analyze the results, and iterate. This allows for genuine novelty and discovery.

## When to Use

-   **Literature Review**: "Survey the field of Quantum Computing and identify gaps."
-   **Idea Generation**: "Brainstorm 50 potential names for this product and check domain availability."
-   **Scientific Discovery**: Analyzing large datasets to find correlations.
-   **Market Research**: Exploring competitor websites to map out their feature sets.

## Use Cases

-   **Agent Laboratory**: A team of agents (Professor, Postdoc, Reviewer) writing a research paper.
-   **Creative Studio**: Agents collaborating to write a screenplay or design a game.
-   **Scenario Planning**: Simulating how a stock portfolio would perform under various economic conditions.

## Implementation Pattern

```python
def exploration_loop(topic):
    knowledge_base = []
    
    # Phase 1: Hypothesis Generation
    hypotheses = brainstorming_agent.run(f"Generate ideas about {topic}")
    
    for hypothesis in hypotheses:
        # Phase 2: Experiment / Research
        # Agent autonomously decides search queries or code to run
        evidence = researcher_agent.run(f"Test this hypothesis: {hypothesis}")
        
        # Phase 3: Analysis
        conclusion = analyst_agent.run(
            prompt="Does the evidence support the hypothesis?",
            input={"hypothesis": hypothesis, "evidence": evidence}
        )
        
        knowledge_base.append(conclusion)
        
    # Phase 4: Synthesis
    return writer_agent.run("Write a report based on these conclusions", input=knowledge_base)
```
