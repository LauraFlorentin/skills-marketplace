#!/usr/bin/env bash
# Check resolvable source imports against project-defined layer ordering.

set -eu

LAYERS_FILE="${1:-layers.json}"
if [ ! -f "$LAYERS_FILE" ]; then
  printf 'No %s found; layer check skipped.\n' "$LAYERS_FILE"
  exit 0
fi

python3 - "$LAYERS_FILE" <<'PY'
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

root = Path.cwd().resolve()
config_path = Path(sys.argv[1])
data = json.loads(config_path.read_text(encoding="utf-8"))
layers = data.get("layers", [])
if not isinstance(layers, list):
    raise SystemExit("layers must be an array")

path_layers: list[tuple[Path, int, str]] = []
for layer in layers:
    order = int(layer["order"])
    name = str(layer["name"])
    for raw_path in layer.get("paths", []):
        if "[" in raw_path:
            continue
        path_layers.append(((root / raw_path).resolve(), order, name))
path_layers.sort(key=lambda item: len(item[0].parts), reverse=True)


def layer_for(path: Path) -> tuple[int, str] | None:
    resolved = path.resolve()
    for prefix, order, name in path_layers:
        if resolved == prefix or prefix in resolved.parents:
            return order, name
    return None


def resolve_import(source: Path, specifier: str) -> Path | None:
    if specifier.startswith("."):
        return (source.parent / specifier).resolve()
    candidate = (root / specifier).resolve()
    return candidate if layer_for(candidate) else None


js_patterns = [
    re.compile(r"(?:import|export)\s+(?:type\s+)?(?:[^;]*?\s+from\s+)?['\"]([^'\"]+)['\"]"),
    re.compile(r"require\(\s*['\"]([^'\"]+)['\"]\s*\)"),
]
py_pattern = re.compile(r"^\s*from\s+([.\w]+)\s+import\s+|^\s*import\s+([\w.]+)", re.MULTILINE)
skip = {".git", ".harness", "node_modules", "dist", "build", ".venv", "venv", "__pycache__"}
violations: list[str] = []
checked = 0

for source in root.rglob("*"):
    if not source.is_file() or source.suffix not in {".js", ".jsx", ".ts", ".tsx", ".py"}:
        continue
    if any(part in skip for part in source.relative_to(root).parts):
        continue
    source_layer = layer_for(source)
    if source_layer is None:
        continue
    checked += 1
    content = source.read_text(encoding="utf-8", errors="replace")
    specs: list[str] = []
    if source.suffix == ".py":
        for match in py_pattern.finditer(content):
            spec = match.group(1) or match.group(2)
            leading = len(spec) - len(spec.lstrip("."))
            module = spec.lstrip(".").replace(".", "/")
            base = source.parent
            for _ in range(max(0, leading - 1)):
                base = base.parent
            target = (base / module).resolve() if leading else (root / module).resolve()
            target_layer = layer_for(target)
            if target_layer and target_layer[0] > source_layer[0]:
                violations.append(
                    f"{source.relative_to(root)} ({source_layer[1]}) imports {spec} ({target_layer[1]})"
                )
    else:
        for pattern in js_patterns:
            specs.extend(pattern.findall(content))
        for spec in specs:
            target = resolve_import(source, spec)
            target_layer = layer_for(target) if target else None
            if target_layer and target_layer[0] > source_layer[0]:
                violations.append(
                    f"{source.relative_to(root)} ({source_layer[1]}) imports {spec} ({target_layer[1]})"
                )

if violations:
    print(f"{len(violations)} layer violation(s):")
    for violation in violations:
        print(f"- {violation}")
    raise SystemExit(1)

print(f"Layer constraints satisfied for {checked} classified source file(s).")
PY
