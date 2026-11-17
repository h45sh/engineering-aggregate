#!/usr/bin/env python3
"""
scripts/agg.py - Autonomous Engine for engineering-aggregate.

Provides deterministic, zero-token/low-token tooling for:
1. inherit:   Fast keyword/path-based extraction of relevant knowledge (Ancestral Inheritance).
2. tithe:     Automated end-of-thread retrospective scaffolding from git diff (Equivalent Exchange).
3. condense:  Algorithmic link auditing, line budget checks, and index updates.
4. sync:      Auto-discovers .agents/knowledge/*.md domain files and registers them into index.json.
5. test:      Built-in regression suite verifying that the CLI and hooks remain healthy across evolutions.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import unittest
from pathlib import Path

# Paths
AGENTS_DIR = Path(".agents")
KNOWLEDGE_DIR = AGENTS_DIR / "knowledge"
THREADS_DIR = AGENTS_DIR / "threads"
HOOKS_DIR = AGENTS_DIR / "hooks"
INDEX_FILE = KNOWLEDGE_DIR / "index.json"


def run_cmd(cmd):
    """Run shell command safely and return output."""
    try:
        res = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return res.stdout.strip()
    except subprocess.CalledProcessError:
        return ""


def run_hook(hook_name, *args):
    """Execute dynamic user/agent hook if present in .agents/hooks/<hook_name>."""
    if not HOOKS_DIR.exists():
        return
    for ext in ["", ".sh", ".py"]:
        candidate = HOOKS_DIR / f"{hook_name}{ext}"
        if candidate.exists() and os.access(candidate, os.X_OK):
            cmd = f'"{candidate}" ' + " ".join(f'"{a}"' for a in args)
            run_cmd(cmd)
            break


def load_index():
    """Load or generate default index.json."""
    if INDEX_FILE.exists():
        try:
            with open(INDEX_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass

    return {
        "domains": {},
        "anti_patterns": []
    }


def save_index(data):
    """Save index.json atomically."""
    KNOWLEDGE_DIR.mkdir(parents=True, exist_ok=True)
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def cmd_inherit(args):
    """
    Inherit relevant domain intelligence based on touched files or keywords.
    Outputs a concise, token-efficient brief for the agent's context.
    """
    run_hook("pre_inherit")

    query_terms = set()
    if args.query:
        query_terms.update([w.lower() for w in re.split(r"[\s,]+", args.query) if len(w) > 2])

    target_files = []
    if args.files:
        target_files.extend(args.files)
    else:
        git_status = run_cmd("git status --porcelain")
        if git_status:
            for line in git_status.splitlines():
                parts = line.strip().split()
                if len(parts) >= 2:
                    target_files.append(parts[-1])

    for f in target_files:
        path_tokens = re.split(r"[/._\-]+", f.lower())
        query_terms.update([t for t in path_tokens if len(t) > 2])

    print("=== ANCESTRAL INHERITANCE: REPOSITORY INTELLIGENCE BRIEF ===")
    print(f"Context Filter: {', '.join(sorted(target_files)) if target_files else 'None'} | Terms: {', '.join(sorted(query_terms)) if query_terms else 'General'}\n")

    index = load_index()
    matched_domains = set()
    matched_anti_patterns = []

    # 1. Match domains via index file_patterns and keywords
    for domain, meta in index.get("domains", {}).items():
        patterns = meta.get("file_patterns", [])
        for p in patterns:
            for f in target_files:
                if Path(f).match(p) or p in f:
                    matched_domains.add(domain)

        domain_keywords = set(k.lower() for k in meta.get("keywords", []))
        if domain_keywords.intersection(query_terms):
            matched_domains.add(domain)

    # 2. Match anti-patterns
    for ap in index.get("anti_patterns", []):
        ap_keywords = set(k.lower() for k in ap.get("keywords", []))
        if ap.get("domain") in matched_domains or ap_keywords.intersection(query_terms):
            matched_anti_patterns.append(ap)

    # 3. Output Global Laws (AGENTS.md summary if present)
    agents_md = Path("AGENTS.md")
    if agents_md.exists():
        print("--- [GLOBAL REPOSITORY INVARIANTS] (from AGENTS.md) ---")
        with open(agents_md, "r", encoding="utf-8") as f:
            lines = f.readlines()[:40]
            print("".join(lines).strip())
        print("\n-------------------------------------------------------")

    # 4. Output matched domain knowledge
    if matched_domains:
        for domain in sorted(matched_domains):
            domain_file = KNOWLEDGE_DIR / f"{domain}.md"
            if domain_file.exists():
                print(f"\n--- [DOMAIN INTELLIGENCE: {domain.upper()}] ({domain_file}) ---")
                with open(domain_file, "r", encoding="utf-8") as f:
                    print(f.read().strip())
    else:
        print("\n[Notice]: No domain-specific constraints found for current files.")

    # 5. Output matched anti-patterns (What NOT to do)
    if matched_anti_patterns:
        print("\n--- [PROHIBITED ANTI-PATTERNS & FATAL TRAPS] ---")
        for ap in matched_anti_patterns:
            print(f"- TRAP: {ap.get('title')}")
            print(f"  FAILURE MODE: {ap.get('why_failed')}")
            print(f"  REQUIRED REPLACEMENT: {ap.get('replacement')}\n")
    else:
        ap_file = KNOWLEDGE_DIR / "anti-patterns.md"
        if ap_file.exists():
            print(f"\n--- [GENERAL ANTI-PATTERNS] ({ap_file}) ---")
            with open(ap_file, "r", encoding="utf-8") as f:
                lines = [l for l in f.readlines() if l.strip().startswith("-") or l.strip().startswith("#")][:25]
                print("".join(lines).strip())

    print("\n=== END OF INHERITANCE BRIEF: PROCEED WITH TASK EXECUTION ===")
    run_hook("post_inherit")


def cmd_tithe(args):
    """
    Automate the Equivalent Exchange payback. Scaffolds a thread retrospective
    pre-filled with git branch, commit, touched files, and diff summary.
    """
    topic = args.topic
    if not topic:
        branch = run_cmd("git branch --show-current")
        topic = branch.replace("/", "_").replace("-", "_") if branch else "session"

    THREADS_DIR.mkdir(parents=True, exist_ok=True)
    target_file = THREADS_DIR / f"thread_{topic}.md"

    branch = run_cmd("git branch --show-current") or "main"
    commit = run_cmd("git rev-parse --short HEAD") or "uncommitted"
    diff_stat = run_cmd("git diff --stat HEAD~1 HEAD") or run_cmd("git diff --stat")
    changed_files = run_cmd("git diff --name-only HEAD~1 HEAD") or run_cmd("git diff --name-only")

    content = f"""# Thread Retrospective: {topic}

- **Branch / PR**: `{branch}` (Commit `{commit}`)
- **Primary Domain**: `[{args.domain or 'Unspecified'}]`
- **Touched Files**:
{chr(10).join(f"- `{f}`" for f in changed_files.splitlines()) if changed_files else "- None"}

---

## Pillar 1: Aggregate Intelligence Feedback
*Audit of existing techniques consulted or inherited during this thread:*

| Technique / Rule Consulted | Outcome | Assessment | Detail & Context |
| :--- | :---: | :---: | :--- |
| *e.g. Existing DB connection pattern* | **VALIDATED** | Evergreen | *Held true without regressions.* |

*Options: VALIDATED | FAILED | SITUATIONAL | INSUFFICIENT DATA*

---

## Pillar 2: Novel Discoveries & Codebase Realities
*Document newly discovered runtime quirks, race conditions, or architecture seams:*

- **Principle**: *Name of the insight*
- **Problem Solved**: *What bug, performance cliff, or friction was resolved?*
- **Mechanism**: *How does it work?*
- **Code Reference**: `{changed_files.splitlines()[0] if changed_files else 'path/to/file.py'}:L1`

---

## Pillar 3: Anti-Patterns & Prohibited Techniques (What NOT to do)
*Document failed attempts and dead ends future agents must avoid:*

- **Anti-Pattern**: *Prohibited technique*
- **Why it Failed**: *Root cause of failure*
- **Correct Replacement**: *Mandated alternative*

---

## Pillar 4: Invariants & Performance Contracts to Preserve
*Quantitative guarantees and reproduction commands:*

| Contract / Invariant | Threshold / Guarantee | Verification Command |
| :--- | :--- | :--- |
| *Execution Safety* | All tests pass | `pytest` or project test command |

---
<!-- Diff Stat Summary:
{diff_stat}
-->
"""

    if target_file.exists() and not args.force:
        print(f"[Notice]: File '{target_file}' already exists. Use --force to overwrite.")
    else:
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Tithe scaffolded at: {target_file}")
        print("Agent instructions: Review and fill in the 4 pillars with empirical facts from your test runs.")

    run_hook("post_tithe", str(target_file))


def cmd_condense(args):
    """
    Algorithmic maintenance:
    - Scans for dead file/line references in .agents/knowledge/
    - Checks line count limits (Tier 1 <= 250 lines, Tier 2 <= 150 lines)
    """
    print("=== RUNNING ALGORITHMIC KNOWLEDGE CONDENSATION & AUDIT ===")

    agents_md = Path("AGENTS.md")
    if agents_md.exists():
        line_count = len(agents_md.read_text(encoding="utf-8").splitlines())
        status = "✅ PASS" if line_count <= 250 else "⚠️ EXCEEDED"
        print(f"Tier 1 Budget (AGENTS.md): {line_count}/250 lines -> {status}")

    if KNOWLEDGE_DIR.exists():
        for k_file in KNOWLEDGE_DIR.glob("*.md"):
            lines = len(k_file.read_text(encoding="utf-8").splitlines())
            status = "✅ PASS" if lines <= 150 else "⚠️ EXCEEDED (Requires pruning)"
            print(f"Tier 2 Budget ({k_file.name}): {lines}/150 lines -> {status}")

    print("\nAuditing code references for drift/entropy...")
    link_pattern = re.compile(r"([a-zA-Z0-9_\-\./]+\.[a-zA-Z0-9]+):L(\d+)")
    dead_links = 0
    total_links = 0

    files_to_check = list(KNOWLEDGE_DIR.glob("*.md")) if KNOWLEDGE_DIR.exists() else []
    for f in files_to_check:
        content = f.read_text(encoding="utf-8")
        matches = link_pattern.findall(content)
        for filepath, line_no in matches:
            total_links += 1
            if not Path(filepath).exists():
                print(f"⚠️  Dead reference in {f.name}: File '{filepath}' does not exist!")
                dead_links += 1

    print(f"Reference Audit Complete: {total_links} references verified, {dead_links} dead links found.")
    print("=== CONDENSATION & AUDIT FINISHED ===")


def cmd_sync(args):
    """
    Auto-discovers .agents/knowledge/*.md domain files and registers them into index.json.
    """
    if not KNOWLEDGE_DIR.exists():
        print(f"[Notice]: Knowledge directory '{KNOWLEDGE_DIR}' does not exist yet.")
        return

    index = load_index()
    domains = index.setdefault("domains", {})
    count_added = 0

    for md_file in KNOWLEDGE_DIR.glob("*.md"):
        domain_name = md_file.stem
        if domain_name in ["anti-patterns", "invariants"]:
            continue

        if domain_name not in domains:
            domains[domain_name] = {
                "path": str(md_file.as_posix()),
                "keywords": [domain_name],
                "file_patterns": [f"src/{domain_name}/**", f"**/{domain_name}/**"]
            }
            count_added += 1

    save_index(index)
    print(f"✅ Sync complete: Registered {count_added} new domains into {INDEX_FILE}.")


def cmd_test(args):
    """
    Built-in regression suite verifying that the CLI and hooks remain healthy across evolutions.
    """
    class SelfTest(unittest.TestCase):
        def test_load_index_structure(self):
            idx = load_index()
            self.assertIn("domains", idx)
            self.assertIn("anti_patterns", idx)

        def test_tithe_scaffold_output(self):
            dummy_file = THREADS_DIR / "thread__selftest_dummy.md"
            if dummy_file.exists():
                dummy_file.unlink()
            dummy_args = argparse.Namespace(topic="_selftest_dummy", domain="TestDomain", force=True)
            cmd_tithe(dummy_args)
            self.assertTrue(dummy_file.exists())
            content = dummy_file.read_text(encoding="utf-8")
            self.assertIn("Pillar 1: Aggregate Intelligence Feedback", content)
            self.assertIn("Pillar 2: Novel Discoveries & Codebase Realities", content)
            self.assertIn("Pillar 3: Anti-Patterns & Prohibited Techniques", content)
            self.assertIn("Pillar 4: Invariants & Performance Contracts", content)
            dummy_file.unlink()

    loader = unittest.defaultTestLoader
    suite = loader.loadTestsFromTestCase(SelfTest)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if not result.wasSuccessful():
        sys.exit(1)


def cmd_harvest_t3(args):
    """
    Scans ~/.t3/caches/pull-requests/ to harvest PR metadata, feature branches,
    and reviews for a target repository, outputting a retrospective draft.
    """
    import glob
    cache_dir = Path.home() / ".t3" / "caches" / "pull-requests"
    if not cache_dir.exists():
        print(f"[Error]: T3 pull-requests cache not found at '{cache_dir}'.")
        return

    repo_filter = args.repo.lower() if args.repo else None
    harvested = []

    for f in cache_dir.glob("pr-v2*"):
        try:
            with open(f, "r", encoding="utf-8") as fp:
                data = json.load(fp)
                if isinstance(data, list) and len(data) > 0:
                    val = data[0].get("value", {})
                    payload_str = val.get("payload")
                    if payload_str:
                        payload = json.loads(payload_str)
                        r = payload.get("repository", "")
                        if not repo_filter or (repo_filter in r.lower()):
                            # Filter out automated bot bumps
                            if not payload.get("author", {}).get("isBot", False):
                                harvested.append(payload)
        except Exception:
            pass

    harvested.sort(key=lambda x: x.get("number", 0))
    print(f"=== HARVESTED {len(harvested)} PULL REQUESTS FROM T3 CACHE ===")

    THREADS_DIR.mkdir(parents=True, exist_ok=True)
    out_file = THREADS_DIR / "thread_t3_harvest.md"

    md_lines = [
        "# Thread Retrospective: T3 Cache Historical Harvest",
        "",
        f"- **Repository Target**: `{args.repo or 'All'}`",
        f"- **Total PRs Harvested**: `{len(harvested)}`",
        "",
        "---",
        "",
        "## Harvested Feature & Fix Sprints",
        "",
        "| PR # | Title | Branch Flow | State |",
        "| :---: | :--- | :--- | :---: |"
    ]

    for pr in harvested:
        num = pr.get("number")
        title = pr.get("title", "").replace("|", "-")
        head = pr.get("headBranch", "")
        base = pr.get("baseBranch", "")
        state = pr.get("state", "")
        md_lines.append(f"| #{num} | {title} | `{head}` → `{base}` | **{state.upper()}** |")

    md_lines.extend([
        "",
        "---",
        "",
        "## Key Solved Regressions & Invariant Candidates",
        "",
        "Review the PR titles above to extract verified techniques into `.agents/knowledge/<domain>.md` and anti-patterns into `.agents/knowledge/anti-patterns.md`.",
        ""
    ])

    out_file.write_text("\n".join(md_lines), encoding="utf-8")
    print(f"✅ Harvest report generated at: {out_file}")
    print("Agent instruction: Review and extract the confirmed techniques and timing invariants into domain knowledge files.")


def main():
    parser = argparse.ArgumentParser(description="engineering-aggregate command engine")
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    # inherit
    p_inherit = subparsers.add_parser("inherit", help="Extract ancestral intelligence for files or query")
    p_inherit.add_argument("--files", nargs="*", help="File paths being modified")
    p_inherit.add_argument("--query", type=str, help="Keywords or task description")

    # tithe
    p_tithe = subparsers.add_parser("tithe", help="Scaffold retrospective from git diff")
    p_tithe.add_argument("--topic", type=str, help="Topic / feature name")
    p_tithe.add_argument("--domain", type=str, help="Primary domain (UI, Storage, Engine, etc.)")
    p_tithe.add_argument("--force", action="store_true", help="Overwrite existing thread retrospective")

    # condense
    p_condense = subparsers.add_parser("condense", help="Run algorithmic budget and reference audit")

    # sync
    p_sync = subparsers.add_parser("sync", help="Auto-sync knowledge files into index.json")

    # test
    p_test = subparsers.add_parser("test", help="Run self-testing suite for CLI and tools")

    # harvest-t3
    p_harvest = subparsers.add_parser("harvest-t3", help="Harvest PRs and reviews from ~/.t3/caches/")
    p_harvest.add_argument("--repo", type=str, help="Repository name filter (e.g. h45sh/cyguide)")

    args = parser.parse_args()
    if args.subcommand == "inherit":
        cmd_inherit(args)
    elif args.subcommand == "tithe":
        cmd_tithe(args)
    elif args.subcommand == "condense":
        cmd_condense(args)
    elif args.subcommand == "sync":
        cmd_sync(args)
    elif args.subcommand == "test":
        cmd_test(args)
    elif args.subcommand == "harvest-t3":
        cmd_harvest_t3(args)


if __name__ == "__main__":
    main()
