#!/usr/bin/env python3
"""
Skill Validator — Automated structural checks for Claude skills.

Based on "The Complete Guide to Building Skills for Claude" by Anthropic.

Usage:
    python validate_skill.py <path-to-skill-folder>
    python validate_skill.py <path-to-skill-folder> --json    # Machine-readable output
    python validate_skill.py <path-to-skill-folder> --fix     # Suggest auto-fixes
"""

import sys
import os
import re
import json
import argparse


def parse_yaml_frontmatter(content):
    """Extract YAML frontmatter from SKILL.md content."""
    if not content.startswith("---"):
        return None, "Missing opening --- delimiter"

    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, "Missing closing --- delimiter"

    yaml_text = parts[1].strip()
    if not yaml_text:
        return None, "Frontmatter is empty"

    # Simple YAML parser for flat key-value pairs
    frontmatter = {}
    current_key = None
    for line in yaml_text.split("\n"):
        line_stripped = line.strip()
        if not line_stripped or line_stripped.startswith("#"):
            continue

        # Check for top-level key: value
        match = re.match(r"^(\w[\w-]*):\s*(.*)", line)
        if match:
            key = match.group(1)
            value = match.group(2).strip()
            # Remove surrounding quotes if present
            if value and value[0] in ('"', "'") and value[-1] == value[0]:
                value = value[1:-1]
            frontmatter[key] = value
            current_key = key
        elif current_key and line.startswith("  "):
            # Multi-line value or nested (just append)
            frontmatter[current_key] += " " + line_stripped

    return frontmatter, None


def check_folder_naming(folder_path):
    """Validate folder naming conventions."""
    results = []
    folder_name = os.path.basename(os.path.normpath(folder_path))

    # kebab-case check
    is_kebab = bool(re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", folder_name))
    results.append({
        "check": "Folder uses kebab-case",
        "passed": is_kebab,
        "detail": f"Folder name: '{folder_name}'" + ("" if is_kebab else " — should be lowercase with hyphens only"),
        "fix": f"Rename to: '{re.sub(r'[^a-z0-9]+', '-', folder_name.lower()).strip('-')}'" if not is_kebab else None
    })

    # No spaces
    has_spaces = " " in folder_name
    results.append({
        "check": "No spaces in folder name",
        "passed": not has_spaces,
        "detail": None,
        "fix": f"Rename to: '{folder_name.replace(' ', '-')}'" if has_spaces else None
    })

    # No underscores
    has_underscores = "_" in folder_name
    results.append({
        "check": "No underscores in folder name",
        "passed": not has_underscores,
        "detail": None,
        "fix": f"Rename to: '{folder_name.replace('_', '-')}'" if has_underscores else None
    })

    # No capitals
    has_capitals = folder_name != folder_name.lower()
    results.append({
        "check": "No capital letters in folder name",
        "passed": not has_capitals,
        "detail": None,
        "fix": f"Rename to: '{folder_name.lower()}'" if has_capitals else None
    })

    # Reserved names
    reserved = "claude" in folder_name.lower() or "anthropic" in folder_name.lower()
    results.append({
        "check": "Folder name not reserved (claude/anthropic)",
        "passed": not reserved,
        "detail": "'claude' and 'anthropic' are reserved prefixes" if reserved else None,
        "fix": "Choose a different name that doesn't include 'claude' or 'anthropic'" if reserved else None
    })

    return results


def check_file_structure(folder_path, is_plugin_root=False):
    """Validate file structure."""
    results = []

    # SKILL.md exists (case-sensitive)
    skill_md_path = os.path.join(folder_path, "SKILL.md")
    has_skill_md = os.path.isfile(skill_md_path)
    results.append({
        "check": "SKILL.md exists (case-sensitive)",
        "passed": has_skill_md,
        "detail": None,
        "fix": "Create or rename the main file to exactly 'SKILL.md'" if not has_skill_md else None
    })

    # Check for common case mistakes
    if not has_skill_md:
        for f in os.listdir(folder_path):
            if f.lower() == "skill.md" and f != "SKILL.md":
                results.append({
                    "check": f"Case mismatch detected: '{f}'",
                    "passed": False,
                    "detail": f"Found '{f}' but it must be exactly 'SKILL.md'",
                    "fix": f"Rename '{f}' to 'SKILL.md'"
                })

    # No README.md inside skill folder
    has_readme = os.path.isfile(os.path.join(folder_path, "README.md"))
    results.append({
        "check": "No README.md inside skill folder",
        "passed": not has_readme,
        "detail": "All documentation should go in SKILL.md or references/" if has_readme else None,
        "fix": "Move README.md content into SKILL.md or references/, then delete README.md" if has_readme else None
    })

    # Check optional directories
    expected_dirs = {"scripts", "references", "assets"}
    if is_plugin_root:
        # Plugin roots may have these additional standard subdirectories
        expected_dirs |= {"agents", "hooks", "commands", "skills", "templates", "evals"}
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path) and item not in expected_dirs and not item.startswith(".") and item != "__pycache__" and item != "evals":
            results.append({
                "check": f"Unexpected directory: '{item}'",
                "passed": False,
                "detail": f"Expected directories are: scripts/, references/, assets/" + (", agents/, hooks/, commands/, skills/, templates/ (plugin root)" if is_plugin_root else ""),
                "fix": f"Rename or move '{item}/' to one of the standard directories, or document why it exists"
            })

    return results


def check_yaml_frontmatter(folder_path):
    """Validate YAML frontmatter content."""
    results = []
    skill_md_path = os.path.join(folder_path, "SKILL.md")

    if not os.path.isfile(skill_md_path):
        results.append({
            "check": "YAML frontmatter",
            "passed": False,
            "detail": "Cannot check — SKILL.md not found",
            "fix": "Create SKILL.md first"
        })
        return results, None, None

    with open(skill_md_path, "r", encoding="utf-8") as f:
        content = f.read()

    frontmatter, error = parse_yaml_frontmatter(content)

    if error:
        results.append({
            "check": "YAML frontmatter parseable",
            "passed": False,
            "detail": error,
            "fix": "Ensure frontmatter starts and ends with --- on their own lines"
        })
        return results, None, content

    results.append({
        "check": "YAML frontmatter parseable",
        "passed": True,
        "detail": None,
        "fix": None
    })

    # name field
    has_name = "name" in frontmatter and frontmatter["name"]
    results.append({
        "check": "'name' field present",
        "passed": has_name,
        "detail": f"name: '{frontmatter.get('name', '')}'" if has_name else None,
        "fix": "Add 'name: your-skill-name' to frontmatter" if not has_name else None
    })

    if has_name:
        name = frontmatter["name"]
        name_kebab = bool(re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", name))
        results.append({
            "check": "'name' uses kebab-case",
            "passed": name_kebab,
            "detail": f"name: '{name}'" if not name_kebab else None,
            "fix": f"Change to: '{re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')}'" if not name_kebab else None
        })

        folder_name = os.path.basename(os.path.normpath(folder_path))
        name_matches = name == folder_name
        results.append({
            "check": "'name' matches folder name",
            "passed": name_matches,
            "detail": f"name='{name}', folder='{folder_name}'" if not name_matches else None,
            "fix": f"Change name to '{folder_name}' or rename folder to '{name}/'" if not name_matches else None
        })

    # description field
    has_desc = "description" in frontmatter and frontmatter["description"]
    results.append({
        "check": "'description' field present",
        "passed": has_desc,
        "detail": None,
        "fix": "Add 'description: What it does. Use when [trigger phrases].' to frontmatter" if not has_desc else None
    })

    if has_desc:
        desc = frontmatter["description"]
        desc_len = len(desc)
        under_limit = desc_len <= 1024
        results.append({
            "check": "Description under 1024 characters",
            "passed": under_limit,
            "detail": f"{desc_len} characters" + (" — over limit!" if not under_limit else ""),
            "fix": f"Trim description by {desc_len - 1024} characters" if not under_limit else None
        })

        # Check for WHAT and WHEN
        when_indicators = ["use when", "use this", "trigger", "use for", "activate",
                          "invoke", "mention", "says", "asks", "requests"]
        has_when = any(ind in desc.lower() for ind in when_indicators)
        results.append({
            "check": "Description includes WHEN to use (trigger conditions)",
            "passed": has_when,
            "detail": None if has_when else "No trigger conditions found — description only says WHAT, not WHEN",
            "fix": "Add trigger phrases like: 'Use when user says \"...\", \"...\", or mentions ...''" if not has_when else None
        })

        # Check for specific trigger phrases (quoted or listed)
        has_quotes = '"' in desc or "'" in desc
        results.append({
            "check": "Description includes specific trigger phrases",
            "passed": has_quotes,
            "detail": None if has_quotes else "No quoted trigger phrases found",
            "fix": "Add specific phrases users would say, in quotes" if not has_quotes else None
        })

    # XML angle brackets check
    yaml_section = content.split("---")[1] if "---" in content else ""
    has_xml = "<" in yaml_section or ">" in yaml_section
    results.append({
        "check": "No XML angle brackets in frontmatter",
        "passed": not has_xml,
        "detail": "Security restriction: < and > are forbidden in frontmatter" if has_xml else None,
        "fix": "Remove all < and > characters from the YAML frontmatter section" if has_xml else None
    })

    return results, frontmatter, content


def check_content_quality(content, folder_path):
    """Check instruction quality and progressive disclosure."""
    results = []

    if not content:
        return results

    # Remove frontmatter for body analysis
    parts = content.split("---", 2)
    body = parts[2] if len(parts) >= 3 else content

    # Line count
    lines = body.strip().split("\n")
    line_count = len(lines)
    under_500 = line_count <= 500
    results.append({
        "check": f"SKILL.md body under 500 lines ({line_count} lines)",
        "passed": under_500,
        "detail": f"{line_count} lines" + (" — consider moving content to references/" if not under_500 else ""),
        "fix": "Move detailed documentation to references/ and link from SKILL.md" if not under_500 else None
    })

    # Has examples
    has_examples = bool(re.search(r"(?i)(example|e\.g\.|for instance|sample)", body))
    results.append({
        "check": "Includes examples",
        "passed": has_examples,
        "detail": None,
        "fix": "Add at least one concrete example showing input → expected output" if not has_examples else None
    })

    # Has error handling
    has_errors = bool(re.search(r"(?i)(error|troubleshoot|fail|issue|problem|common issue|if .+ fails)", body))
    results.append({
        "check": "Includes error handling / troubleshooting",
        "passed": has_errors,
        "detail": None,
        "fix": "Add a Troubleshooting section covering common errors and their solutions" if not has_errors else None
    })

    # References external files
    has_refs = bool(re.search(r"(references/|scripts/|assets/)", body))
    has_ref_dir = os.path.isdir(os.path.join(folder_path, "references"))
    has_scripts_dir = os.path.isdir(os.path.join(folder_path, "scripts"))

    if has_ref_dir or has_scripts_dir:
        results.append({
            "check": "SKILL.md references bundled resources",
            "passed": has_refs,
            "detail": None if has_refs else "Has scripts/ or references/ dirs but SKILL.md doesn't reference them",
            "fix": "Add clear references to when Claude should read each bundled file" if not has_refs else None
        })

    # Check for excessive ALWAYS/NEVER/MUST caps
    caps_commands = len(re.findall(r"\b(ALWAYS|NEVER|MUST|CRITICAL|IMPORTANT)\b", body))
    reasonable_caps = caps_commands <= 5
    results.append({
        "check": f"Reasonable use of CAPS directives ({caps_commands} found)",
        "passed": reasonable_caps,
        "detail": f"{caps_commands} ALL-CAPS directives found" + (" — consider explaining WHY instead" if not reasonable_caps else ""),
        "fix": "Replace some ALWAYS/NEVER/MUST with reasoning that explains WHY the behavior matters" if not reasonable_caps else None
    })

    # Uses imperative form (spot check)
    imperative_indicators = ["run ", "check ", "create ", "use ", "call ", "fetch ", "verify ", "generate ", "save "]
    passive_indicators = ["should be ", "might want to ", "could consider ", "it is recommended "]
    imperative_count = sum(1 for ind in imperative_indicators if ind.lower() in body.lower())
    passive_count = sum(1 for ind in passive_indicators if ind.lower() in body.lower())
    mostly_imperative = imperative_count >= passive_count
    results.append({
        "check": "Uses imperative form in instructions",
        "passed": mostly_imperative,
        "detail": f"Imperative signals: {imperative_count}, Passive signals: {passive_count}",
        "fix": "Rewrite passive instructions as direct commands (e.g., 'You might want to check...' → 'Check...')" if not mostly_imperative else None
    })

    return results


def compute_scores(all_results):
    """Compute dimension scores from check results."""
    total_checks = len(all_results)
    passed = sum(1 for r in all_results if r["passed"])
    failed = total_checks - passed

    # Map checks to dimensions
    dimensions = {
        "Structure": [],
        "Description": [],
        "Progressive Disclosure": [],
        "Instruction Clarity": [],
        "Error Handling": [],
    }

    for r in all_results:
        check = r["check"].lower()
        if any(k in check for k in ["folder", "skill.md exists", "readme", "directory", "unexpected", "yaml", "name", "delimit"]):
            dimensions["Structure"].append(r)
        elif any(k in check for k in ["description", "trigger", "when to use"]):
            dimensions["Description"].append(r)
        elif any(k in check for k in ["500 lines", "references", "bundled"]):
            dimensions["Progressive Disclosure"].append(r)
        elif any(k in check for k in ["example", "imperative", "caps"]):
            dimensions["Instruction Clarity"].append(r)
        elif any(k in check for k in ["error", "troubleshoot"]):
            dimensions["Error Handling"].append(r)

    scores = {}
    for dim, checks in dimensions.items():
        if not checks:
            scores[dim] = {"score": 3, "total_checks": 0, "passed": 0}
            continue
        p = sum(1 for c in checks if c["passed"])
        t = len(checks)
        ratio = p / t if t > 0 else 0
        score = max(1, min(5, round(ratio * 4 + 1)))
        scores[dim] = {"score": score, "total_checks": t, "passed": p}

    return scores, passed, failed, total_checks


def format_report(folder_path, all_results, scores, passed, failed, total):
    """Format the human-readable report."""
    folder_name = os.path.basename(os.path.normpath(folder_path))
    total_score = sum(s["score"] for s in scores.values())
    max_score = len(scores) * 5

    if total_score >= 22:
        rating = "Production-ready" if total_score >= 25 else "Good foundation"
    elif total_score >= 15:
        rating = "Needs work"
    else:
        rating = "Fundamental rework needed"

    report = []
    report.append(f"# Skill Review: {folder_name}")
    report.append(f"\n## Overall: {total_score}/{max_score} — {rating}")
    report.append(f"Checks: {passed}/{total} passed\n")

    report.append("## Structural Checks")
    for r in all_results:
        icon = "✅" if r["passed"] else "❌"
        line = f"  {icon} {r['check']}"
        if r.get("detail"):
            line += f" — {r['detail']}"
        report.append(line)

    report.append("\n## Dimension Scores")
    for dim, data in scores.items():
        report.append(f"  {dim}: {data['score']}/5 ({data['passed']}/{data['total_checks']} checks passed)")

    # Collect fixes
    fixes = [(r["check"], r["fix"]) for r in all_results if r.get("fix")]
    if fixes:
        report.append("\n## Top Fixes")
        for i, (check, fix) in enumerate(fixes[:5], 1):
            report.append(f"  {i}. [{check}] {fix}")

    return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(description="Validate a Claude skill folder")
    parser.add_argument("path", help="Path to the skill folder")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--fix", action="store_true", help="Include auto-fix suggestions")
    parser.add_argument("--plugin-root", action="store_true", help="Treat as plugin root (allows agents/, hooks/, commands/, skills/, templates/ dirs)")
    args = parser.parse_args()

    folder_path = os.path.abspath(args.path)

    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a directory", file=sys.stderr)
        sys.exit(1)

    # Run all checks
    all_results = []
    all_results.extend(check_folder_naming(folder_path))
    all_results.extend(check_file_structure(folder_path, is_plugin_root=args.plugin_root))

    yaml_results, frontmatter, content = check_yaml_frontmatter(folder_path)
    all_results.extend(yaml_results)

    if content:
        all_results.extend(check_content_quality(content, folder_path))

    scores, passed, failed, total = compute_scores(all_results)

    if args.json:
        output = {
            "skill_path": folder_path,
            "skill_name": os.path.basename(os.path.normpath(folder_path)),
            "total_checks": total,
            "passed": passed,
            "failed": failed,
            "scores": scores,
            "total_score": sum(s["score"] for s in scores.values()),
            "max_score": len(scores) * 5,
            "checks": all_results if args.fix else [
                {k: v for k, v in r.items() if k != "fix"} for r in all_results
            ]
        }
        print(json.dumps(output, indent=2))
    else:
        report = format_report(folder_path, all_results, scores, passed, failed, total)
        print(report)
        if args.fix:
            print("\n## All Fix Suggestions")
            for r in all_results:
                if r.get("fix"):
                    print(f"  • [{r['check']}] {r['fix']}")


if __name__ == "__main__":
    main()
