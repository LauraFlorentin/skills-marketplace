# Changelog

All notable changes to this marketplace are documented here. Versions follow
[Semantic Versioning](https://semver.org/).

## Unreleased

### Added

- Repository-wide validation for marketplace, plugin, skill, agent, hook, and
  local-link integrity.
- GitHub Actions validation and community contribution files.
- Explicit MIT license file.

### Changed

- Normalized plugin catalog metadata and made plugin manifests the version
  source of truth.
- Updated plugin hooks to use the supported `hooks/hooks.json` layout and
  installation-safe paths.
- Reworked all skill frontmatter for concise, intent-based triggering and
  removed redundant trigger sections from skill bodies.
- Reduced Product and Project Management lifecycle skills and orchestrators to
  focused workflows that load detailed references only when needed.
- Rebuilt Real Estate specialist agents around dated evidence, traceable math,
  scenario analysis, and professional legal, tax, and lending review instead
  of embedded market defaults.
- Reworked M&A legal and regulatory workflows for source citations,
  confidentiality, approval gates, and current official-source research.
- Reworked Agentic Skills guidance for private reasoning, safe tool execution,
  memory privacy, and retrieval access control.
- Updated Skill Checker to distinguish platform errors from editorial warnings
  and added safe optional script syntax checks.
- Updated plugin versions for this behavior release: Agentic Skills 1.1.0,
  Brand Studio 1.1.0, Deck Studio 1.1.0, Harness Engineer 1.2.0, M&A Advisory
  1.1.0, Management Consulting 1.3.0, Product Management 1.1.0, Project
  Management 1.1.0, Real Estate Investment 1.1.0, and Skill Checker 1.1.0.

### Fixed

- Added the missing Deck Studio catalog entry.
- Added required frontmatter to orchestrator agents.
- Corrected Brand Guard configuration lookup and hook output behavior.
- Replaced Harness Engineer's automatic stashing, reverting, staging,
  committing, and stale-lock deletion behavior with opt-in warnings and
  permission prompts that never mutate project or Git state.
- Promoted nested Real Estate specialist references into discoverable flat
  plugin agents and repaired all command routing.
- Removed hard-coded host filesystem paths and normalized namespaced command
  documentation.
