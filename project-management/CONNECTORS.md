# Connectors

Commands in this plugin reference external tools using `~~placeholder` syntax. You do **not** need any of these tools to use the plugin — commands work standalone and produce richer output when tools are connected.

## Placeholder Reference

| Placeholder | Category | Example Tools |
|-------------|----------|---------------|
| `~~project-tracker` | Issue tracking & sprints | Jira, Linear, Asana, Monday, Shortcut |
| `~~docs` | Documentation & wikis | Notion, Confluence, Google Docs |
| `~~time-tracker` | Time tracking & capacity | Harvest, Toggl, Clockify |
| `~~messaging` | Team communication | Slack, Teams |
| `~~calendar` | Scheduling & availability | Google Calendar, Outlook |
| `~~ci-cd` | Build & deploy pipelines | GitHub Actions, Jenkins, CircleCI |
| `~~repo` | Source code & PRs | GitHub, GitLab, Bitbucket |

## Notes

- **`~~ci-cd` and `~~repo`** are software-mode-only connectors. General PM mode does not reference them.
- **`~~docs`** can serve as a project wiki, meeting notes repo, and decision log — same tool, multiple uses.
- **Pre-configured MCP servers** are listed in [`.mcp.json`](./.mcp.json). Enable whichever tools your team uses.
