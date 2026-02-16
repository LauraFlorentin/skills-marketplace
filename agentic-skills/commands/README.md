# Agentic Skills — Commands

Slash commands for Claude Code. Each `.md` file in this directory becomes a `/command-name` you can invoke directly.

## Usage

In Claude Code, type `/` to see available commands from this plugin.

## Available Commands

| Command | Skill | Description |
|---------|-------|-------------|
| `/adapt` | Adaptation | Modify agent behavior dynamically based on feedback |
| `/agent-communication` | Inter-Agent Communication | Enable agents to exchange messages and collaborate |
| `/chain` | Prompt Chaining | Chain LLM calls where each output feeds the next |
| `/evaluate` | Evaluation & Monitoring | Measure agent performance, reliability, and cost |
| `/explore` | Exploration & Discovery | Autonomously research and explore solution spaces |
| `/guardrails` | Guardrails & Safety | Inspect inputs/outputs to prevent misuse |
| `/handle-exceptions` | Exception Handling | Detect failures and execute fallback logic |
| `/human-in-the-loop` | Human-in-the-Loop | Pause execution for human approval on critical actions |
| `/mcp` | Model Context Protocol | Connect AI to external data and tools securely |
| `/memory` | Memory Management | Persist and retrieve state across interactions |
| `/multi-agent` | Multi-Agent Collaboration | Coordinate specialized agents on complex problems |
| `/optimize` | Resource-Aware Optimization | Select the most efficient model or tool per task |
| `/parallelize` | Parallelization | Execute multiple agent tasks concurrently |
| `/plan` | Planning | Formulate structured action sequences before execution |
| `/prioritize` | Prioritization | Assess task urgency and importance |
| `/rag` | Knowledge Retrieval (RAG) | Augment generation with external knowledge |
| `/reason` | Reasoning Techniques | Use Chain of Thought for complex logical tasks |
| `/reflect` | Reflection | Evaluate and critique output to improve quality |
| `/route` | Routing | Classify inputs and direct to specialized agents |
| `/set-goals` | Goal Setting & Monitoring | Define success criteria and track progress |
| `/tool-use` | Tool Use | Enable LLMs to execute actions via external systems |

## Adding a Command

Create a new `.md` file in this directory:

```markdown
---
description: Brief description of what this command does
---

Your command instructions here...
```

The filename becomes the command name (e.g., `analyze.md` → `/analyze`).
