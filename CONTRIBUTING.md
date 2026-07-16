# Contributing

Thank you for improving the AI Skills Marketplace. Keep contributions focused,
portable, and easy to review.

## Before you start

- Open an issue for a new plugin or a change that affects several plugins.
- Keep credentials, client data, generated archives, and local agent settings
  out of the repository.
- Use a focused branch and a pull request; do not mix unrelated cleanup into a
  skill change.

## Repository conventions

Each plugin lives at the repository root and uses this layout when applicable:

```text
plugin-name/
├── .claude-plugin/plugin.json
├── skills/<skill-name>/SKILL.md
├── commands/
├── agents/
├── hooks/hooks.json
└── README.md
```

- Use lowercase kebab-case for plugin and skill directories.
- Match every skill's frontmatter `name` to its directory name.
- Make each skill description state both what it does and when it should run.
- Keep `SKILL.md` under 500 lines. Move detailed frameworks, examples, and
  domain references into directly linked `references/` files.
- Use relative paths within a plugin. Hook commands must reference bundled
  files through `${CLAUDE_PLUGIN_ROOT}`.
- Avoid silently destructive hooks. Require an explicit user decision before
  modifying Git state, deleting files, sending messages, or changing external
  systems.
- Cite authoritative sources for legal, financial, medical, regulatory, or
  time-sensitive claims, and tell the executing agent to verify current data.

Flat files under `commands/` remain for compatibility. Prefer a skill directory
for new workflows that need supporting files or automatic invocation.

## Validate changes

Run the repository validator from the root:

```bash
python3 scripts/validate_marketplace.py
```

If Claude Code is installed, also run its strict validator:

```bash
claude plugin validate . --strict
```

Test changed scripts directly and load changed plugins locally before opening a
pull request. Include the test commands and results in the pull request body.

## Versioning

Plugin manifests are the source of truth for versions. Follow semantic
versioning and update `CHANGELOG.md` when behavior changes:

- Patch: fixes and wording corrections without changed behavior.
- Minor: new skills, commands, agents, hooks, or backward-compatible behavior.
- Major: breaking names, removed workflows, or incompatible output changes.

## Pull requests

A pull request should explain the user problem, list the affected plugins, and
show how the change was validated. Reviewers will prioritize trigger quality,
context efficiency, safe tool use, portability, and verifiable outputs.
