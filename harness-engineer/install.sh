#!/usr/bin/env bash
# =============================================================================
# HARNESS ENGINEER PLUGIN — Install Script
# Wires all four skills + circuit breaker system into a Claude Code project
#
# Usage:
#   bash .claude/plugins/harness-engineer/install.sh           # install into current project
#   bash .claude/plugins/harness-engineer/install.sh --global  # install globally
#   bash .claude/plugins/harness-engineer/install.sh --verify  # check installation status
# =============================================================================

PLUGIN_DIR="$(cd "$(dirname "$0")" && pwd)"
MODE="project"
[[ "$1" == "--global" ]] && MODE="global"
[[ "$1" == "--verify" ]] && MODE="verify"

BOLD='\033[1m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

ok()   { echo -e "  ${GREEN}✓${NC} $1"; }
warn() { echo -e "  ${YELLOW}⚠${NC}  $1"; }
err()  { echo -e "  ${RED}✗${NC} $1"; }
info() { echo -e "  · $1"; }

echo ""
echo -e "${BOLD}🔧 Harness Engineer Plugin${NC}"
echo "   Multi-skill harness engineering toolkit for agent-first development"
echo "   Based on OpenAI, Anthropic, and LangChain research (Feb 2026)"
echo ""

# ── Verify mode ───────────────────────────────────────────────────────────────

if [ "$MODE" = "verify" ]; then
  echo -e "${BOLD}Checking installation...${NC}"
  echo ""
  
  [ -f ".harness/hooks/circuit-breaker.sh" ] && ok "Circuit breaker hook" || err "Circuit breaker hook missing"
  [ -f ".harness/hooks/dead-mans-switch.sh" ] && ok "Dead man's switch hook" || err "Dead man's switch hook missing"
  [ -f ".harness/hooks/watchdog.sh" ] && ok "Watchdog hook" || err "Watchdog hook missing"
  [ -f ".harness/hooks/model-context.sh" ] && ok "Model context hook" || err "Model context hook missing"
  [ -f ".claude/settings.json" ] && ok ".claude/settings.json" || err ".claude/settings.json missing"
  [ -f "AGENTS.md" ] && ok "AGENTS.md" || warn "AGENTS.md not found (run /harness-engineer:init)"
  [ -f "features.json" ] && ok "features.json" || warn "features.json not found (run /harness-engineer:init)"
  [ -f "init.sh" ] && ok "init.sh" || warn "init.sh not found (run /harness-engineer:init)"
  [ -f "claude-progress.txt" ] && ok "claude-progress.txt" || warn "claude-progress.txt not found"
  [ -d "current_tasks" ] && ok "current_tasks/ directory" || warn "current_tasks/ missing"
  
  # Check hooks are wired
  if [ -f ".claude/settings.json" ]; then
    grep -q "circuit-breaker" .claude/settings.json 2>/dev/null && ok "Hooks wired in settings.json" || err "Hooks not wired in settings.json"
  fi
  
  echo ""
  exit 0
fi

# ── Project install ───────────────────────────────────────────────────────────

echo -e "${BOLD}Installing circuit breaker system...${NC}"
echo ""

# 1. Create .harness directory
mkdir -p .harness/hooks .harness/state .harness/scripts
mkdir -p current_tasks

# 2. Copy hooks
cp "$PLUGIN_DIR/hooks/circuit-breaker.sh" .harness/hooks/
cp "$PLUGIN_DIR/hooks/dead-mans-switch.sh" .harness/hooks/
cp "$PLUGIN_DIR/hooks/watchdog.sh" .harness/hooks/
cp "$PLUGIN_DIR/hooks/model-context.sh" .harness/hooks/
chmod +x .harness/hooks/*.sh
ok "Circuit breaker hooks installed"

# 3. Copy layer checker script
cp "$PLUGIN_DIR/skills/harness-gc/scripts/check-layers.sh" .harness/scripts/
cp "$PLUGIN_DIR/skills/harness-gc/scripts/check-doc-refs.py" .harness/scripts/
chmod +x .harness/scripts/check-layers.sh
ok "GC scripts installed"

# 4. Wire .claude/settings.json
mkdir -p .claude

if [ -f ".claude/settings.json" ]; then
  warn ".claude/settings.json already exists — merging hooks..."
  python3 << PYEOF
import json, sys

try:
    with open('.claude/settings.json', 'r') as f:
        existing = json.load(f)
except:
    existing = {}

with open('$PLUGIN_DIR/templates/settings.json.template', 'r') as f:
    new_config = json.load(f)

# Merge hooks
existing_hooks = existing.get('hooks', {})
new_hooks = new_config.get('hooks', {})

for event, entries in new_hooks.items():
    if event not in existing_hooks:
        existing_hooks[event] = []
    existing_cmds = set()
    for entry in existing_hooks[event]:
        for h in entry.get('hooks', []):
            existing_cmds.add(h.get('command', ''))
    for entry in entries:
        entry_cmds = {h.get('command', '') for h in entry.get('hooks', [])}
        if not entry_cmds.intersection(existing_cmds):
            existing_hooks[event].append(entry)

existing['hooks'] = existing_hooks
existing['harness'] = new_config.get('harness', {})

with open('.claude/settings.json', 'w') as f:
    json.dump(existing, f, indent=2)
print("  Merged successfully")
PYEOF
else
  cp "$PLUGIN_DIR/templates/settings.json.template" .claude/settings.json
fi
ok "Wired .claude/settings.json"

# 5. Create .harness/config.json
if [ ! -f ".harness/config.json" ]; then
cat > .harness/config.json << 'EOF'
{
  "_comment": "Harness Engineer plugin configuration. Edit as needed.",
  "model": "claude",
  "_model_options": ["claude", "codex", "gemini"],
  "_model_note": "Controls model-specific prompt tuning in AGENTS.md and harness-onboard. Claude responds better to explicit reasoning instructions; Codex to terse constraints.",
  "dev_server_port": null,
  "circuit_breaker": {
    "soft_threshold": 5,
    "hard_threshold": 10
  },
  "dead_mans_switch": {
    "warning_minutes": 15,
    "critical_minutes": 30
  },
  "watchdog": {
    "check_interval_tool_calls": 10,
    "lock_stale_minutes": 20
  },
  "browser_automation": {
    "enabled": false,
    "mcp_server": "puppeteer",
    "_note": "Set enabled=true and configure Puppeteer MCP for end-to-end verification (Anthropic recommendation)"
  }
}
EOF
ok "Created .harness/config.json"
fi

# 6. Create claude-progress.txt if missing
if [ ! -f "claude-progress.txt" ]; then
cat > claude-progress.txt << EOF
# Claude Progress Log
# Generated by harness-engineer plugin
# Update at the end of every session.
# Format: === SESSION [timestamp] === ... ==================

=== HARNESS INITIALIZED $(date '+%Y-%m-%d %H:%M') ===
Harness-engineer plugin installed.
Next session: run /harness-engineer:init to scaffold the full harness for this project.
===========================================
EOF
ok "Created claude-progress.txt"
fi

# 7. Create current_tasks/.gitkeep
touch current_tasks/.gitkeep

# 8. Update .gitignore
if [ -f ".gitignore" ]; then
  if ! grep -q ".harness/state" .gitignore; then
    printf "\n# Harness Engineer runtime state\n.harness/state/\n" >> .gitignore
    ok "Updated .gitignore"
  fi
else
  printf "# Harness Engineer runtime state\n.harness/state/\n" > .gitignore
  ok "Created .gitignore"
fi

# 9. Stage everything for commit
if git rev-parse --git-dir > /dev/null 2>&1; then
  git add .harness/hooks/ .harness/scripts/ .harness/config.json .claude/settings.json .gitignore current_tasks/ claude-progress.txt 2>/dev/null
  ok "Staged all files for commit"
fi

echo ""
echo -e "${BOLD}✅ Harness Engineer plugin installed.${NC}"
echo ""
echo "Next steps:"
echo "  1. Commit: git commit -m 'feat: install harness-engineer plugin'"
echo "  2. Scaffold: /harness-engineer:init"
echo "  3. Verify: bash install.sh --verify"
echo ""
echo "Configuration: .harness/config.json"
echo "Logs (runtime): .harness/state/ (gitignored)"
echo ""
echo -e "Circuit breaker thresholds:"
echo "  Soft nudge:     5 edits to same file"
echo "  Hard break:     10 edits → git stash + revert + requeue"
echo "  Commit warning: 15 min without commit"
echo "  Auto-stash:     30 min without commit"
echo "  Health check:   every 10 tool calls"
echo "  Lock cleanup:   20 min stale locks"
