# Brand Studio — Commands

Slash commands for Claude Code. Plugin commands are namespaced by plugin name.

## Usage

In Claude Code, type `/` to see available commands from this plugin.

## Available Commands

| Command | Description |
|---------|-------------|
| `/brand-studio:brand-setup` | Configure or update your brand identity |
| `/brand-studio:brand-status` | Show a summary of your current brand config |
| `/brand-studio:brand-ppt` | Brand a PowerPoint or create one from scratch |
| `/brand-studio:brand-doc` | Brand a Word doc or create one from scratch |
| `/brand-studio:brand-logo` | Generate logo SVGs (3 variations) |
| `/brand-studio:brand-social` | Create social media assets (or full kit) |
| `/brand-studio:brand-web` | Create branded HTML artifacts |

## Adding a Command

Create a new `.md` file in this directory:

```markdown
---
description: Brief description of what this command does
---

Your command instructions here...
```

The filename becomes the command name inside the plugin namespace (for example, `brand-setup.md` → `/brand-studio:brand-setup`).
