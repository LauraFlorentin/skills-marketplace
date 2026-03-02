# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user connects in that category. For example, `~~project-tracker` might mean Linear, Jira, Asana, or any other project tracker with an MCP server.

Plugins are **tool-agnostic** — they describe workflows in terms of categories rather than specific products. The `.mcp.json` pre-configures specific MCP servers, but any MCP server in that category works.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|----------|-------------|-----------------|---------------|
| Roadmap & planning | `~~roadmap-tool` | Linear, Notion | Productboard, Aha! |
| Product analytics | `~~analytics` | PostHog | Amplitude, Mixpanel, Heap |
| Tickets & sprints | `~~project-tracker` | Linear | Jira, Shortcut, Asana |
| Documentation | `~~docs` | Notion | Confluence, Google Docs |
| Research repository | `~~research-repo` | Notion | Dovetail, EnjoyHQ |
| Team communication | `~~messaging` | Slack | Microsoft Teams |
| Design files | `~~design` | Figma | — |

## Shared tool note

`~~research-repo` and `~~docs` can point to the same tool (e.g., Notion). Configure the tool once — no duplicate configuration needed.
