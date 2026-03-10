#!/usr/bin/env bash
# =============================================================================
# HARNESS ENGINEER — Layer Constraint Checker
# Validates that no file imports from a higher architectural layer
# Run by watchdog.sh on every N tool calls
# =============================================================================

LAYERS_FILE="layers.json"
VIOLATIONS=0

if [ ! -f "$LAYERS_FILE" ]; then
  echo "No layers.json found — skipping layer check"
  exit 0
fi

# Build layer order map from layers.json
python3 << 'PYEOF'
import json
import os
import re
import sys

with open('layers.json') as f:
    data = json.load(f)

layers = data.get('layers', [])
# Build path → order mapping
path_order = {}
for layer in layers:
    order = layer['order']
    for path in layer.get('paths', []):
        path_order[path.rstrip('/')] = (order, layer['name'])

violations = []

# Walk all source files
for root, dirs, files in os.walk('.'):
    # Skip noise
    dirs[:] = [d for d in dirs if d not in ('node_modules', '.git', '.harness', 'dist', 'build', '__pycache__')]
    
    for filename in files:
        if not (filename.endswith(('.ts', '.tsx', '.js', '.jsx', '.py'))):
            continue
        if 'test' in filename.lower() or 'spec' in filename.lower():
            continue  # Tests are exempt
            
        filepath = os.path.join(root, filename)
        rel_path = filepath.lstrip('./')
        
        # Determine this file's layer
        file_layer_order = None
        file_layer_name = None
        for path_prefix, (order, name) in path_order.items():
            if rel_path.startswith(path_prefix):
                file_layer_order = order
                file_layer_name = name
                break
        
        if file_layer_order is None:
            continue  # Not in a declared layer
        
        # Read imports
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except:
            continue
        
        # Find imports (JS/TS style)
        imports = re.findall(r'''(?:import|from)\s+['"]([^'"]+)['"]''', content)
        # Python style
        imports += re.findall(r'''(?:^|\n)(?:from|import)\s+([\w.]+)''', content)
        
        for imp in imports:
            # Normalize to path-like
            imp_path = imp.replace('.', '/') if '/' not in imp else imp
            imp_path = imp_path.lstrip('/')
            
            # Find imported file's layer
            for path_prefix, (imp_order, imp_name) in path_order.items():
                if imp_path.startswith(path_prefix.rstrip('/')):
                    if imp_order > file_layer_order:
                        violations.append(
                            f"LAYER VIOLATION: {rel_path} (layer={file_layer_name}, order={file_layer_order}) "
                            f"imports from {imp_path} (layer={imp_name}, order={imp_order})"
                        )
                    break

if violations:
    print(f"\n🔴 {len(violations)} layer violation(s) detected:\n")
    for v in violations:
        print(f"  ✗ {v}")
    print()
    sys.exit(1)
else:
    print(f"✓ Layer constraints satisfied ({len(path_order)} paths checked)")
    sys.exit(0)
PYEOF
