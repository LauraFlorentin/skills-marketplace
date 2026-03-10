#!/usr/bin/env bash
# =============================================================================
# HARNESS ENGINEER — Model Context Injector
# Reads .harness/config.json and injects model-specific operating context.
#
# Fires on: SessionStart (via settings.json)
# Effect: prints model-tuned operating hints to stdout so the agent reads them
#
# Based on LangChain finding: "same harness, different model = different results"
# Claude and Codex need different constraint framing to perform optimally.
# =============================================================================

CONFIG=".harness/config.json"

if [ ! -f "$CONFIG" ]; then
  echo "[HARNESS] No config.json found — using default (claude) model profile."
  MODEL="claude"
else
  MODEL=$(python3 -c "
import json, sys
try:
    with open('$CONFIG') as f:
        config = json.load(f)
    print(config.get('model', 'claude').lower())
except:
    print('claude')
" 2>/dev/null || echo "claude")
fi

BROWSER_ENABLED=$(python3 -c "
import json
try:
    with open('$CONFIG') as f:
        config = json.load(f)
    ba = config.get('browser_automation', {})
    print('true' if ba.get('enabled') else 'false')
except:
    print('false')
" 2>/dev/null || echo "false")

# ── Model-specific operating hints ────────────────────────────────────────────

case "$MODEL" in
  claude)
    cat << 'EOF'

[HARNESS: MODEL=claude]
You are Claude. Your harness is tuned for your strengths and failure modes.

REASONING: You perform best with explicit reasoning phase separation.
  Use xhigh reasoning for planning and verification, high for implementation.
  Do not skip the reasoning sandwich — it measurably improves output quality.

VERIFICATION: You tend toward premature completion. Counter this:
  Always execute the steps array as behavioral tests, not code review.
  "The code looks correct" is not verification. Clicking through the UI is.

CONTEXT: You handle long context well but suffer from context rot past ~40%.
  If you feel confused, you probably have too much context loaded.
  Re-read only the relevant section of docs/ rather than everything.

LOOPS: You can loop subtly — making small edits that don't converge.
  If you've edited the same file 3+ times, stop and write out your plan first.
EOF
    ;;
  codex)
    cat << 'EOF'

[HARNESS: MODEL=codex]
You are Codex. Your harness is tuned for your strengths and failure modes.

REASONING: You perform best with terse, concrete constraints — not verbose explanations.
  Read features.json steps as literal test cases. Execute them exactly.
  Do not infer intent — execute the spec as written.

VERIFICATION: You tend to one-shot large implementations.
  Hard constraint: one feature, one commit. No exceptions.
  Build → verify → commit before picking the next feature.

CONTEXT: You are sensitive to context window overload.
  Load only the files you are actively editing. Close mental context aggressively.
  If init.sh fails, debug it immediately — do not continue on a broken foundation.

LOOPS: You can enter tight fix-loops on compilation errors.
  If you fix the same error 3 times, read the architecture docs before continuing.
EOF
    ;;
  gemini)
    cat << 'EOF'

[HARNESS: MODEL=gemini]
You are Gemini. Your harness is tuned for your strengths and failure modes.

REASONING: You handle large context windows well — use this for full-repo reads.
  Read the full docs/ directory at session start, not just AGENTS.md.
  Your failure mode is imprecision — be explicit about which feature you're building.

VERIFICATION: You can generate plausible-looking but incorrect implementations.
  Execute every step in features.json against a running server. No exceptions.
  Check browser console errors after every verify cycle.

CONTEXT: Load architecture.md and the full feature list before starting work.
  Your context capacity is an asset — use it to understand the full system first.

LOOPS: You can drift from the spec during long implementations.
  Re-read the feature steps array every time you switch files.
EOF
    ;;
  *)
    echo "[HARNESS: MODEL=$MODEL — no specific profile, using defaults]"
    ;;
esac

# ── Browser automation status ─────────────────────────────────────────────────

if [ "$BROWSER_ENABLED" = "true" ]; then
  MCP_SERVER=$(python3 -c "
import json
try:
    with open('$CONFIG') as f:
        config = json.load(f)
    print(config.get('browser_automation', {}).get('mcp_server', 'puppeteer'))
except:
    print('puppeteer')
" 2>/dev/null || echo "puppeteer")

  cat << EOF

[HARNESS: BROWSER AUTOMATION ACTIVE — mcp=$MCP_SERVER]
Browser automation is enabled. For all feature verification:
  Use the $MCP_SERVER MCP tool to navigate, click, and verify behavior in a real browser.
  Do NOT use curl or manual inspection as a substitute for browser verification.
  Browser-based testing catches the failures that unit tests miss (Anthropic finding).
  Workflow: navigate → interact → assert visible state → check console errors.
EOF
else
  echo ""
  echo "[HARNESS: BROWSER AUTOMATION disabled — set browser_automation.enabled=true in .harness/config.json]"
  echo "[HARNESS: Without browser automation, manually test each feature step before marking passes=true]"
fi
