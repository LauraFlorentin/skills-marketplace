---
name: rag
description: A pattern that augments the model's generation by retrieving relevant documents from an external knowledge base, ensuring factual accuracy and access to private data. Use when user asks to "add RAG to my agent", "retrieval augmented generation", "search and answer", or mentions document retrieval, knowledge bases, or semantic search.
---

# Knowledge Retrieval (RAG)

Retrieval-Augmented Generation (RAG) connects an LLM to your data. Since LLMs have a cutoff date and don't know your private documents, RAG solves this by first *searching* for relevant information in a database and then *pasting* it into the prompt context. This grounds the answer in facts and reduces hallucinations.

## When to Use

-   **Domain-Specific QA**: Answering questions about internal documentation, legal contracts, or medical records.
-   **Dynamic Data**: When the information changes frequently (news, stock analysis).
-   **Verifiability**: When the answer must cite sources ("According to policy document A...").
-   **Cost**: To avoid fine-tuning models on new data, which is expensive and slow.

## Use Cases

-   **Enterprise Search**: "How do I reset my VPN password?" (Searches IT Wiki).
-   **Legal Analysis**: "Summarize the liability clause in this contract." (Searches contract PDF).
-   **Customer Support**: "What is my order status?" (Searches Order Database).

## Implementation Pattern

```python
def rag_workflow(user_query):
    # Step 1: Retrieval
    # Convert query to vector and search vector DB
    relevant_docs = vector_db.similarity_search(user_query, k=3)
    
    # Step 2: Prompt Construction
    # Combine the context with the user question
    context_text = "\n".join([doc.content for doc in relevant_docs])
    
    prompt = f"""
    You are a helpful assistant. Answer the question based ONLY on the context below.
    
    Context:
    {context_text}
    
    Question: {user_query}
    """
    
    # Step 3: Generation
    answer = llm.generate(prompt)
    
    return answer
```


## Examples

**Input**: "Answer questions about our internal HR handbook using RAG."

```python
# Index
docs = load_documents("hr-handbook.pdf")
chunks = chunk(docs, size=512, overlap=50)
vector_store.upsert(embed(chunks))

# Query
query = "What is the parental leave policy?"
relevant = vector_store.search(embed(query), top_k=5)
answer = llm.answer(query, context=relevant)
```

**Output**: "Our policy provides 16 weeks of fully paid leave for primary caregivers [HR Handbook, Section 7.2]." — with source citation.

---

**Input**: "My RAG pipeline returns irrelevant chunks."

**Diagnostic**: Check chunk size (too large dilutes signal), embedding model alignment, and whether query expansion is needed for short queries.


## Troubleshooting

| Problem | Cause | Fix |
|---|---|---|
| Retrieves irrelevant chunks | Chunk size too large | Reduce to 256–512 tokens with 10% overlap |
| Misses obvious answers | Query too short | Add query expansion: generate 3 semantic variants before searching |
| Hallucinated citations | Model ignores context | Constrain prompt: "Answer ONLY using the provided context. If unknown, say so." |
| Slow retrieval at scale | No ANN index | Switch to HNSW or IVF index for >100K chunks |
| Stale knowledge | Documents not re-indexed | Set up incremental indexing triggered on document updates |
