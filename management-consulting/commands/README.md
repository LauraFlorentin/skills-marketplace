# Management Consulting — Commands

Slash commands for Claude Code. Each `.md` file in this directory becomes a `/command-name` you can invoke directly.

## Usage

In Claude Code, type `/` to see available commands from this plugin.

## Available Commands

### Proposals & Deliverables
| Command | Skill | Description |
|---------|-------|-------------|
| `/proposal` | Proposal & SOW | Draft a client proposal or statement of work |
| `/deliverable` | Client Deliverables | Create a client deliverable — report, deck, framework, or recommendations |
| `/business-case` | Financial Modeling | Build a financial business case or ROI analysis for a recommendation |

### Research & Analysis
| Command | Skill | Description |
|---------|-------|-------------|
| `/research` | Research & Analysis | Conduct market research, competitive analysis, or benchmarking |
| `/interview-guide` | Interview Guides | Create a stakeholder interview guide with questions and synthesis plan |

### Project Management
| Command | Skill | Description |
|---------|-------|-------------|
| `/status-update` | Project Management | Generate an engagement status update or steering committee report |
| `/contract-tracker` | Contract Management | Review contract status, track renewals, or manage change orders |
| `/bench-report` | Bench Management | Generate a bench and utilization report |

### Thought Leadership
| Command | Skill | Description |
|---------|-------|-------------|
| `/pov` | Point of View | Develop a point of view or thought leadership piece |
| `/whitepaper` | Whitepaper & Thought Leadership | Draft a whitepaper or thought leadership piece through a structured pipeline |

### Change & Workshops
| Command | Skill | Description |
|---------|-------|-------------|
| `/change-management` | Change Management | Develop a change management plan for a transformation or initiative |
| `/workshop` | Workshop Facilitation | Design a client workshop — agenda, facilitation plan, and follow-up |

### Structured Thinking Frameworks
| Command | Skill | Description |
|---------|-------|-------------|
| `/2x2` | Structured Thinking | Map items on a 2x2 matrix for prioritization or classification |
| `/crawl-walk-run` | Structured Thinking | Break an initiative into Crawl-Walk-Run phases with milestones, gate criteria, and success measures |
| `/day-one` | Structured Thinking | Plan what Day 1 actually looks like for a new initiative, role, or transformation launch |
| `/elevator-pitch` | Structured Thinking | Distill an idea or recommendation into 30-second, 60-second, and 2-minute versions |
| `/five-whys` | Structured Thinking | Drill past symptoms to find the root cause of a problem |
| `/red-amber-green` | Structured Thinking | Perform a structured RAG traffic-light assessment across multiple dimensions |
| `/storyline` | Structured Thinking | Structure a communication into a persuasive consulting narrative using SCR or Pyramid Principle |
| `/what-by-when` | Structured Thinking | Turn actions into concrete commitments with owners, deadlines, and dependencies |

## Adding a Command

Create a new `.md` file in this directory:

```markdown
---
description: Brief description of what this command does
---

Your command instructions here...
```

The filename becomes the command name (e.g., `proposal.md` → `/proposal`).
