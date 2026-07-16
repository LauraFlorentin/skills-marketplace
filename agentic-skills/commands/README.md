# Agentic Skills — Commands

Slash commands for Claude Code. Each `.md` file in this directory becomes a `/agentic-skills:command-name` you can invoke directly.

## Usage

In Claude Code, type `/agentic-skills:` to see available commands from this plugin.

## Available Commands

| Command | Skill | Description |
|---------|-------|-------------|
| `/agentic-skills:adapt` | Adaptation | Modify agent behavior dynamically based on feedback |
| `/agentic-skills:agent-communication` | Inter-Agent Communication | Enable agents to exchange messages and collaborate |
| `/agentic-skills:chain` | Prompt Chaining | Chain LLM calls where each output feeds the next |
| `/agentic-skills:evaluate` | Evaluation & Monitoring | Measure agent performance, reliability, and cost |
| `/agentic-skills:explore` | Exploration & Discovery | Autonomously research and explore solution spaces |
| `/agentic-skills:guardrails` | Guardrails & Safety | Inspect inputs/outputs to prevent misuse |
| `/agentic-skills:handle-exceptions` | Exception Handling | Detect failures and execute fallback logic |
| `/agentic-skills:human-in-the-loop` | Human-in-the-Loop | Pause execution for human approval on critical actions |
| `/agentic-skills:mcp` | Model Context Protocol | Connect AI to external data and tools securely |
| `/agentic-skills:memory` | Memory Management | Persist and retrieve state across interactions |
| `/agentic-skills:multi-agent` | Multi-Agent Collaboration | Coordinate specialized agents on complex problems |
| `/agentic-skills:optimize` | Resource-Aware Optimization | Select the most efficient model or tool per task |
| `/agentic-skills:parallelize` | Parallelization | Execute multiple agent tasks concurrently |
| `/agentic-skills:plan` | Planning | Formulate structured action sequences before execution |
| `/agentic-skills:prioritize` | Prioritization | Assess task urgency and importance |
| `/agentic-skills:rag` | Knowledge Retrieval (RAG) | Augment generation with external knowledge |
| `/agentic-skills:reason` | Reasoning Techniques | Apply decomposition and verification to complex tasks |
| `/agentic-skills:reflect` | Reflection | Evaluate and critique output to improve quality |
| `/agentic-skills:route` | Routing | Classify inputs and direct to specialized agents |
| `/agentic-skills:set-goals` | Goal Setting & Monitoring | Define success criteria and track progress |
| `/agentic-skills:tool-use` | Tool Use | Enable LLMs to execute actions via external systems |

## Adding a Command

Create a new `.md` file in this directory:

```markdown
---
description: Brief description of what this command does
---

Your command instructions here...
```

The filename becomes the command name (e.g., `analyze.md` → `/agentic-skills:analyze`).
