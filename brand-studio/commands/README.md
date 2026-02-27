# Brand Studio — Commands

Slash commands for Claude Code. Each `.md` file in this directory becomes a `/command-name` you can invoke directly.

## Usage

In Claude Code, type `/` to see available commands from this plugin.

## Available Commands

| Command | Description |
|---------|-------------|
| `/brand-setup` | Configure or update your brand identity |
| `/brand-status` | Show a summary of your current brand config |
| `/brand-ppt` | Brand a PowerPoint or create one from scratch |
| `/brand-doc` | Brand a Word doc or create one from scratch |
| `/brand-logo` | Generate logo SVGs (3 variations) |
| `/brand-social` | Create social media assets (or full kit) |
| `/brand-web` | Create branded HTML artifacts |

## Adding a Command

Create a new `.md` file in this directory:

```markdown
---
description: Brief description of what this command does
---

Your command instructions here...
```

The filename becomes the command name (e.g., `brand-setup.md` → `/brand-setup`).
