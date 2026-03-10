---
name: memory-management
description: Techniques for persisting, retrieving, and managing state across agent interactions, enabling long-coherency and personalization. Use when user asks to "add memory to my agent", "persistent context", "conversation history", or mentions long-term memory, memory retrieval, or context windows.
---

# Memory Management

Memory management provides agents with a "brain" that persists beyond the current context window. It involves storing user preferences, conversation history, and factual knowledge in a database (like a Vector DB or SQL) and retrieving relevant information when needed. Without memory, an agent is amnesic, resetting after every session.

## When to Use

-   **Personalization**: Remembering user names, preferences, and past choices.
-   **Long-Running Tasks**: Tracking progress on a project that spans days or weeks.
-   **Context Awareness**: Understanding references to previous conversations ("As I mentioned earlier...").
-   **Learning**: Improving performance by recalling past mistakes or feedback.

## Use Cases

-   **Chatbots**: Maintaining conversation history for context (Short-term memory).
-   **User Profiles**: Storing "User is a vegetarian" in a profile database (Long-term memory).
-   **Knowledge Base**: Accumulating facts learned from searching the web (Episodic memory).

## Implementation Pattern

```python
class Memory:
    def add(self, content):
        # Store in Vector DB or SQL
        pass
        
    def retrieve(self, query):
        # Search for relevant memories
        pass

def memory_augmented_agent(user_input, user_id):
    # Step 1: Recall
    # Retrieve relevant history and user facts
    context = memory.retrieve(query=user_input, tags=[user_id])
    
    # Step 2: Augment Prompt
    prompt = f"""
    Context from memory: {context}
    User Input: {user_input}
    Answer the user, taking into account their history.
    """
    
    # Step 3: Generate
    response = llm.generate(prompt)
    
    # Step 4: Memorize
    # Store the new interaction
    memory.add(f"User: {user_input} | Agent: {response}")
    
    return response
```


## Examples

**Input**: A customer support agent needs to remember user preferences across sessions.

```python
# Write to memory
memory.store("user:123:preferences", {"language": "Spanish", "tone": "formal"})

# Retrieve on next session
prefs = memory.retrieve("user:123:preferences")
response = agent.run(prompt, context=prefs)
```

**Output**: The agent greets the user in Spanish using formal language, without requiring them to re-specify preferences.

---

**Input**: "My agent keeps forgetting what we discussed earlier in a long conversation."

**Fix**: Implement a sliding window summary: every 10 turns, summarize the conversation so far and store it as a compressed context document. Inject this summary at the start of each new prompt.


## Troubleshooting

| Problem | Cause | Fix |
|---|---|---|
| Agent retrieves wrong memories | Similarity threshold too low | Raise cosine similarity threshold to ≥0.8 for semantic retrieval |
| Memory grows unbounded | No expiry policy | Implement TTL on episodic memory; archive after 30 days |
| Context window overflow | Too much memory injected | Use summarization; only inject top-3 most relevant memories |
| Agent ignores stored memories | Memory not injected into prompt | Ensure retrieved context is passed before the user message, not after |
| Stale preferences causing errors | No invalidation on update | Add a `last_modified` timestamp; re-retrieve if > N days old |
