#!/usr/bin/env python3
"""
Brand Guard Hook
Runs before Write/Edit/Bash tool use.
If a branded file type is being created AND brand-config.md is configured,
injects a reminder to apply brand identity.
"""

import sys
import os
import json

# File types that should trigger brand enforcement
BRANDED_EXTENSIONS = {'.pptx', '.docx', '.html', '.svg', '.png', '.pdf', '.htm'}

# Keywords in tool input that suggest file creation
CREATION_KEYWORDS = ['write', 'create', 'generate', 'output', 'save', 'export']

def main():
    # Read tool input from stdin (Claude Code passes it as JSON)
    try:
        tool_input = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # Don't block if we can't parse

    # Get the tool name and input content
    tool_name = tool_input.get('tool_name', '')
    tool_params = str(tool_input.get('tool_input', ''))

    # Check if any branded file extension is mentioned
    has_branded_file = any(ext in tool_params.lower() for ext in BRANDED_EXTENSIONS)
    
    if not has_branded_file:
        sys.exit(0)  # Not a branded file operation, pass through

    # Check if brand config exists and is configured
    config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'brand-config.md')
    config_path = os.path.normpath(config_path)

    try:
        with open(config_path, 'r') as f:
            config_content = f.read()
    except FileNotFoundError:
        sys.exit(0)  # No config file, pass through

    # If config is unconfigured placeholder, skip
    if 'STATUS: Not configured' in config_content:
        sys.exit(0)

    # Extract brand name for the message
    brand_name = "your brand"
    for line in config_content.split('\n'):
        if '**Brand Name:**' in line:
            brand_name = line.split('**Brand Name:**')[-1].strip()
            break

    # Output a reminder message to Claude via stdout
    # Claude Code surfaces hook stdout as context
    print(f"[Brand Guard] Branded file detected. Applying {brand_name} brand identity.")
    print(f"[Brand Guard] Key brand values from brand-config.md:")
    
    # Print the first ~400 chars of config as a quick reference
    config_preview = config_content[:600].strip()
    print(config_preview)
    print("...")
    print("[Brand Guard] Ensure all colors, fonts, and tone match brand-config.md exactly.")

    sys.exit(0)  # Always exit 0 — never block the operation

if __name__ == '__main__':
    main()
