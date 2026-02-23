# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user connects in that category. For example, `~~project tracker` might mean Asana, Jira, Monday.com, or any other project management tool with an MCP server.

Plugins are **tool-agnostic** — they describe workflows in terms of categories rather than specific products. The `.mcp.json` pre-configures specific MCP servers, but any MCP server in that category works.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|----------|-------------|-----------------|---------------|
| Email | `~~email` | Microsoft 365 | Gmail |
| Office suite | `~~office suite` | Microsoft 365 | Google Workspace |
| Chat | `~~chat` | Slack | Microsoft Teams |
| CRM | `~~crm` | — (connect your preferred CRM) | Salesforce, HubSpot |
| Project tracker | `~~project tracker` | — (connect your preferred tracker) | Asana, Jira, Monday.com |
| Documents | `~~documents` | — (connect your preferred doc store) | SharePoint, Google Drive, Box, Notion |
| Data warehouse | `~~data warehouse` | — (connect if available) | Snowflake, BigQuery |
