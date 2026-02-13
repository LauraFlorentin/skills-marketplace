# Agentic Systems Architecture — Design Patterns

21 foundational patterns for building autonomous AI agents. Each skill includes a conceptual overview, strategic use cases, and reference implementations.

## Skills Overview

### Core Patterns
| Pattern | Description |
| :--- | :--- |
| [Prompt Chaining](./prompt_chaining/SKILL.md) | Decomposing tasks into sequential LLM calls. |
| [Routing](./routing/SKILL.md) | Directing requests to specialized agents or tools. |
| [Parallelization](./parallelization/SKILL.md) | Running multiple agents concurrently for speed or diverse perspectives. |
| [Reflection](./reflection/SKILL.md) | Agents critiquing and improving their own outputs. |
| [Tool Use](./tool_use/SKILL.md) | Enabling agents to interact with the outside world (APIs, Code). |

### Advanced Workflows
| Pattern | Description |
| :--- | :--- |
| [Planning](./planning/SKILL.md) | Creating multi-step plans before execution. |
| [Multi-Agent Collaboration](./multi_agent_collaboration/SKILL.md) | Agents working together with distinct roles. |
| [Goal Setting & Monitoring](./goal_setting/SKILL.md) | Iterative loops working towards a clear objective. |
| [Prioritization](./prioritization/SKILL.md) | Managing task queues based on urgency and importance. |
| [Exploration & Discovery](./exploration/SKILL.md) | Open-ended research and hypothesis generation. |

### Robustness & Safety
| Pattern | Description |
| :--- | :--- |
| [Exception Handling](./exception_handling/SKILL.md) | Graceful recovery from errors and tool failures. |
| [Guardrails & Safety](./guardrails/SKILL.md) | Filtering unsafe inputs and outputs. |
| [Human-in-the-Loop](./human_in_the_loop/SKILL.md) | Escalation to human review for critical decisions. |
| [Evaluation & Monitoring](./evaluation/SKILL.md) | Tracking metrics like accuracy, latency, and cost. |

### Technical Capabilities
| Pattern | Description |
| :--- | :--- |
| [Memory Management](./memory_management/SKILL.md) | Persisting state and context across interactions. |
| [RAG](./rag/SKILL.md) | Retrieving external knowledge to augment generation. |
| [Model Context Protocol](./mcp/SKILL.md) | Standardized connection to external data and tools. |
| [Inter-Agent Communication](./inter_agent_communication/SKILL.md) | Protocols for agents to talk to each other (e.g., A2A). |
| [Resource-Aware Optimization](./resource_optimization/SKILL.md) | Routing to cost-effective models based on task complexity. |
| [Reasoning Techniques](./reasoning/SKILL.md) | Chain of Thought (CoT) and other reasoning prompts. |
| [Adaptation](./adaptation/SKILL.md) | Evolving code or prompts based on feedback. |

## Installation

### Claude Code / Cowork

Add the marketplace (`LauraFlorentin/skills-marketplace`) via Plugins, then install **agentic-skills**.

### Vercel AI SDK

```bash
npx skills add LauraFlorentin/skills-marketplace/plugins/agentic-skills
```

Install a single skill:
```bash
npx skills add LauraFlorentin/skills-marketplace/plugins/agentic-skills/skills/planning
```
