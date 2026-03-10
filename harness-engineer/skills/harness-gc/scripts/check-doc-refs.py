#!/usr/bin/env python3
"""
HARNESS ENGINEER — Documentation Reference Checker
Scans docs/ and AGENTS.md for references to files/paths that no longer exist.
Run by harness-gc skill.
"""

import os
import re
import sys
from pathlib import Path

DOCS_TO_CHECK = ['AGENTS.md', 'docs/architecture.md', 'docs/quality.md', 'docs/beliefs.md']
DEAD_REFS = []
STALE_DOCS = []

def find_path_refs(content):
    """Extract file path references from markdown content."""
    patterns = [
        r'`([^`]+\.[a-zA-Z]{2,5})`',           # backtick code paths
        r'\[.*?\]\(([^)]+)\)',                    # markdown links
        r'(?:src|lib|app|docs)/[\w/\-\.]+',      # bare paths
        r'→\s*([\w/\-\.]+\.(?:md|ts|js|py|sh|json))',  # → references
    ]
    refs = []
    for pattern in patterns:
        refs.extend(re.findall(pattern, content))
    return refs

def check_doc(filepath):
    if not os.path.exists(filepath):
        return
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    refs = find_path_refs(content)
    
    for ref in refs:
        # Skip URLs, anchors, and obvious non-paths
        if ref.startswith(('http', '#', 'localhost', 'npm', 'git')):
            continue
        if len(ref) < 4 or ' ' in ref:
            continue
        
        # Check if file exists
        if not os.path.exists(ref) and not os.path.exists(ref.lstrip('/')):
            DEAD_REFS.append({
                'doc': filepath,
                'ref': ref,
                'severity': 'P0' if filepath == 'AGENTS.md' else 'P1'
            })

def check_feature_list():
    """Check features.json for integrity issues."""
    import json
    
    if not os.path.exists('features.json'):
        return
    
    with open('features.json') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"P0 CRITICAL: features.json has JSON syntax error: {e}")
            return
    
    features = data if isinstance(data, list) else data.get('features', [])
    
    issues = []
    seen_ids = set()
    
    for feature in features:
        fid = feature.get('id', 'UNKNOWN')
        
        # Duplicate IDs
        if fid in seen_ids:
            issues.append(f"P1 DUPLICATE_ID: {fid}")
        seen_ids.add(fid)
        
        # Inconsistent state
        if feature.get('passes') and feature.get('circuit_broken'):
            issues.append(f"P1 INCONSISTENT: {fid} is both passes=true and circuit_broken=true")
        
        if feature.get('passes') and feature.get('in_progress'):
            issues.append(f"P1 INCONSISTENT: {fid} is both passes=true and in_progress=true")
        
        # Empty required fields
        if not feature.get('description'):
            issues.append(f"P1 MISSING_DESCRIPTION: {fid} has no description")
        
        if not feature.get('steps'):
            issues.append(f"P2 MISSING_STEPS: {fid} has no test steps")
    
    return issues

def main():
    print("=== Harness GC: Documentation Reference Check ===\n")
    
    # Check all docs
    for doc in DOCS_TO_CHECK:
        check_doc(doc)
    
    # Also check all files in docs/
    if os.path.isdir('docs'):
        for root, dirs, files in os.walk('docs'):
            for f in files:
                if f.endswith('.md'):
                    check_doc(os.path.join(root, f))
    
    # Report dead references
    if DEAD_REFS:
        p0 = [r for r in DEAD_REFS if r['severity'] == 'P0']
        p1 = [r for r in DEAD_REFS if r['severity'] == 'P1']
        
        if p0:
            print(f"P0 — CRITICAL dead references in AGENTS.md ({len(p0)}):")
            for r in p0:
                print(f"  ✗ '{r['ref']}' referenced in {r['doc']} does not exist")
        
        if p1:
            print(f"\nP1 — Dead references in docs ({len(p1)}):")
            for r in p1:
                print(f"  ✗ '{r['ref']}' referenced in {r['doc']} does not exist")
    else:
        print("✓ No dead documentation references found")
    
    # Check feature list
    print("\n=== Feature List Integrity ===\n")
    feature_issues = check_feature_list()
    if feature_issues:
        for issue in feature_issues:
            print(f"  ✗ {issue}")
    else:
        print("✓ features.json integrity check passed")
    
    total_issues = len(DEAD_REFS) + len(feature_issues or [])
    print(f"\nTotal issues found: {total_issues}")
    
    return 1 if total_issues > 0 else 0

if __name__ == '__main__':
    sys.exit(main())
