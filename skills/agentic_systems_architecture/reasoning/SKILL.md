---
name: Reasoning Techniques
description: Prompting patterns that encourage the model to articulate its specific thought process (Chain of Thought) to improve performance on complex logical, mathematical, or reasoning tasks.
---

# Reasoning Techniques

Reasoning techniques (like Chain-of-Thought, Tree-of-Thought) force the LLM to show its work. Large Language Models are statistical, not logical. By making them output a step-by-step reasoning path before the final answer, you allow the model to provide context to itself, significantly reducing logic errors and "hallucinations of calculation".

## When to Use

-   **Math & Logic**: Word problems, puzzles, navigation tasks.
-   **Complex Planning**: "How do I move this couch through this door?"
-   **Legal/Medical reasoning**: Deriving a conclusion from a set of rules and facts.
-   **Debugging**: Asking the model to explain *why* code is failing before fixing it.

## Use Cases

-   **Zero-Shot CoT**: Simply adding "Let's think step by step" to the prompt.
-   **Few-Shot CoT**: Providing examples of [Question -> Reasoning -> Answer] to guide the model.
-   **Self-Consistency**: Generating 5 different Chain-of-Thought paths and picking the answer that appears most frequently (Majority Voting).
-   **Tree of Thoughts**: Exploring multiple possible reasoning branches and backtracking if one leads to a dead end.

## Implementation Pattern

```python
def chain_of_thought_prompt(question):
    prompt = f"""
    Question: {question}
    
    Instruction: Answer the question by reasoning step-by-step. 
    Format your answer as:
    
    Reasoning:
    1. [First Step]
    2. [Second Step]
    ...
    
    Final Answer: [Answer]
    """
    
    return llm.generate(prompt)
```
