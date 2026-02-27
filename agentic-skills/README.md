# Agentic Skills

Core building blocks for autonomous AI agents — 21 foundational patterns covering planning, routing, tool use, RAG, memory, reflection, and more.

## Skills

### Core Patterns
| Skill | Description |
| :--- | :--- |
| [Prompt Chaining](./skills/prompt_chaining/SKILL.md) | Decomposing tasks into sequential LLM calls. |
| [Routing](./skills/routing/SKILL.md) | Directing requests to specialized agents or tools. |
| [Parallelization](./skills/parallelization/SKILL.md) | Running multiple agents concurrently for speed or diverse perspectives. |
| [Reflection](./skills/reflection/SKILL.md) | Agents critiquing and improving their own outputs. |
| [Tool Use](./skills/tool_use/SKILL.md) | Enabling agents to interact with the outside world (APIs, Code). |

### Advanced Workflows
| Skill | Description |
| :--- | :--- |
| [Planning](./skills/planning/SKILL.md) | Creating multi-step plans before execution. |
| [Multi-Agent Collaboration](./skills/multi_agent_collaboration/SKILL.md) | Agents working together with distinct roles. |
| [Goal Setting & Monitoring](./skills/goal_setting/SKILL.md) | Iterative loops working towards a clear objective. |
| [Prioritization](./skills/prioritization/SKILL.md) | Managing task queues based on urgency and importance. |
| [Exploration & Discovery](./skills/exploration/SKILL.md) | Open-ended research and hypothesis generation. |

### Robustness & Safety
| Skill | Description |
| :--- | :--- |
| [Exception Handling](./skills/exception_handling/SKILL.md) | Graceful recovery from errors and tool failures. |
| [Guardrails & Safety](./skills/guardrails/SKILL.md) | Filtering unsafe inputs and outputs. |
| [Human-in-the-Loop](./skills/human_in_the_loop/SKILL.md) | Escalation to human review for critical decisions. |
| [Evaluation & Monitoring](./skills/evaluation/SKILL.md) | Tracking metrics like accuracy, latency, and cost. |

### Technical Capabilities
| Skill | Description |
| :--- | :--- |
| [Memory Management](./skills/memory_management/SKILL.md) | Persisting state and context across interactions. |
| [RAG](./skills/rag/SKILL.md) | Retrieving external knowledge to augment generation. |
| [Model Context Protocol](./skills/mcp/SKILL.md) | Standardized connection to external data and tools. |
| [Inter-Agent Communication](./skills/inter_agent_communication/SKILL.md) | Protocols for agents to talk to each other (e.g., A2A). |
| [Resource-Aware Optimization](./skills/resource_optimization/SKILL.md) | Routing to cost-effective models based on task complexity. |
| [Reasoning Techniques](./skills/reasoning/SKILL.md) | Chain of Thought (CoT) and other reasoning prompts. |
| [Adaptation](./skills/adaptation/SKILL.md) | Evolving code or prompts based on feedback. |

## Commands

21 slash commands — one for each skill. See [`commands/README.md`](./commands/README.md) for the full list.

## Agents

None. These are standalone patterns — combine them to build your own agent architectures.

## Hooks

None.

## Installation

### Claude Code / Cowork

Add the marketplace (`LauraFlorentin/skills-marketplace`) via Plugins, then install **agentic-skills**.

### Vercel AI SDK

```bash
npx skills add LauraFlorentin/skills-marketplace/agentic-skills
```

Install a single skill:
```bash
npx skills add LauraFlorentin/skills-marketplace/agentic-skills/skills/planning
```
