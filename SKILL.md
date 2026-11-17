---
name: engineering-aggregate
description: Autonomous collective intelligence engine and self-evolving memory system. Operates under the Laws of Ancestral Inheritance (zero-token targeted context) and Equivalent Exchange (post-task empirical payback). Compounds architectural integrity, security immunization, refactoring seams, and feature velocity over time while monotonically decreasing flaws and token friction.
---

# Engineering Aggregate Skill

> **"A perpetual engine fueled by user intent. It converts development energy and trial-and-error into permanent ancestral intelligence—ensuring flaws monotonically decrease, token costs shrink, and codebase resilience compounds."**

This skill governs a self-evolving collective memory system for AI coding agents and human engineers. It transforms every development thread into an active learning node that evaluates existing engineering techniques, records novel insights, identifies broken anti-patterns, and condenses findings into a token-efficient knowledge base.

---

## 1. The Core Philosophy

### A. The Engine of Compounding Strength
Left unattended, software systems decay through **entropy**: agents repeat old mistakes, introduce architectural layer leaks, revive patched security flaws, and bloat token context windows.

`engineering-aggregate` reverses entropy:
- **User Prompts are the Fuel**: Each user request injects energy into the repository.
- **Ancestral Inheritance**: Agents borrow past hard-earned wisdom on-demand via zero-token algorithmic routing.
- **Equivalent Exchange (The Tithe)**: Agents return verified empirical intelligence without compromising task focus.
- **The Result**: With every thread, **flaws decrease, token friction drops, and structural strength increases.**

### B. The 4 Non-Regression Streams
The system ensures that non-feature engineering disciplines never degrade:

```text
 ┌────────────────────────────────────────────────────────────────────────┐
 │                   THE COMPOUNDING STRENGTH MATRIX                      │
 │                                                                        │
 │  1. ARCHITECTURE     2. SECURITY        3. REFACTORING   4. CONSOLIDATE│
 │  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐ ┌─────────────┐│
 │  │ Boundary &   │   │ Threat &     │   │ Seam &       │ │ Pruning &   ││
 │  │ Layer Invari-│   │ Vulnerability│   │ Dead-Code    │ │ Knowledge   ││
 │  │ ants (No DAG │   │ Defense      │   │ Contracts    │ │ Condensation││
 │  │ cycles)      │   │ (IMDS, SSRF, │   │ (Deep        │ │ (Eliminate  ││
 │  │              │   │  Auth)       │   │  modules)    │ │  bloat)     ││
 │  └──────┬───────┘   └──────┬───────┘   └──────┬───────┘ └──────┬──────┘│
 │         │                  │                  │                │       │
 │         ▼                  ▼                  ▼                ▼       │
 │  ┌──────────────────────────────────────────────────────────────────┐  │
 │  │              THE ULTIMATE ANCESTRAL INHERITANCE                  │  │
 │  │       Flaws Monotonically Decrease | Strength Compounds          │  │
 │  └──────────────────────────────────────────────────────────────────┘  │
 └────────────────────────────────────────────────────────────────────────┘
```

1. **Architecture Integrity**: Enforces strict module depth, seam isolation, and layer DAG invariants (e.g. UI never imports database models directly).
2. **Security Immunization**: When a vulnerability (SSRF, injection, auth bypass) is patched, the anti-pattern and its verification command are permanently registered so future agents never reintroduce it.
3. **Refactoring Contracts**: Code cleanups and consolidations preserve functional equivalence by locking in quantitative performance thresholds.
4. **Knowledge Consolidation**: Algorithmic pruning strips obsolete rules and dead code links, keeping context token-lean.

---

## 2. Autonomous Operational Protocol for Agents (Zero-Bloat & Low-Latency)

Agents follow a streamlined, token-budgeted cycle designed to prevent context window bloat and eliminate multi-step round-trip churn:

```text
 ┌────────────────────────────────────────────────────────────────────────┐
 │                   THE ZERO-BLOAT AGENT LIFECYCLE                       │
 │                                                                        │
 │   1. PRE-FLIGHT (Compact)        2. EXECUTE TASK      3. ONE-SHOT TITHE│
 │  ┌─────────────────────────┐    ┌──────────────┐    ┌────────────────┐ │
 │  │ python3 scripts/agg.py  │───►│ Write Code   │───►│ python3 scripts│ │
 │  │ inherit --compact ...   │    │ & Run Tests  │    │ /agg.py        │ │
 │  │ (<150 tokens, 1 round)  │    │              │    │ quick-tithe ...│ │
 │  └─────────────────────────┘    └──────────────┘    └────────────────┘ │
 │                                                     (Atomic <50ms,     │
 │                                                      Zero round-trips) │
 └────────────────────────────────────────────────────────────────────────┘
```

### Step 1: Pre-Flight Inheritance (Task Startup)
When touching architectural components, core models, or security boundaries, claim a high-density, token-budgeted brief:
```bash
python3 scripts/agg.py inherit --compact --files <paths_to_touch> --query "<task_keywords>"
```
- **Context Protection**: `--compact` emits single-line bullet invariants ($\le 150$ tokens) rather than raw file dumps.
- **Gated Execution**: For trivial questions, documentation reads, or typo fixes, **skip inheritance** to preserve context.

### Step 2: Implementation (Pure Focus)
Execute the requested feature, bugfix, security patch, or refactor. Focus 100% on delivering clean code and passing tests. **Do not let documentation or retrospective debt distract you during coding.**

### Step 3: Paying the Tithe (Post-Implementation — One-Shot Atomic)
Once tests pass, pay the tithe in **one single command** without conversational round-trip churn:
```bash
python3 scripts/agg.py quick-tithe --summary "<1-line summary>" --domain <UI|Storage|Engine|Auth|Security|Refactor> --validated "<rules_confirmed>" --trap "<what_failed_if_any>"
```
- **What happens automatically in $<50$ms:**
  1. Scaffolds and populates `.agents/threads/thread_<topic>.md` with all 4 Pillars.
  2. Registers any real anti-pattern into `.agents/knowledge/anti-patterns.md`.
  3. Synchronizes domain files into `index.json`.
  4. Runs budget checks and link audits silently.
- **For Background Execution / Subagents**:
  If running via an async subagent or git hook, run:
  ```bash
  python3 scripts/agg.py auto-tithe
  ```
  This extracts the summary and modified files directly from `git log`/`git diff`, keeping the main conversational context 100% clean!

---

## 3. The 3-Tier Storage Hierarchy

| Tier | Directory / File | Budget Limit | Reading Cadence | Purpose |
| :--- | :--- | :---: | :--- | :--- |
| **Tier 1: Global Laws** | `AGENTS.md` | $\le 250$ lines | At startup (top summary) | Universal repository laws, security policies, and architectural seams. |
| **Tier 2: Domain Knowledge** | `.agents/knowledge/<domain>.md` | 50–150 lines | On-demand via `inherit` | Compressed, domain-specific rules, edge cases, and anti-patterns. |
| **Tier 3: Historical Logs** | `.agents/threads/*.md` | Unlimited | Never read on startup | Audit trail and raw narrative history of completed threads. |

---

## 4. The Human's Role (Effortless Ownership)
The human user is the **Architect / Product Director**:
- You provide goals, priorities, and creative intent in plain chat.
- You never write retrospectives, calculate token budgets, or run scripts manually.
- The engine ensures that every conversation leaves the codebase stronger, cleaner, and cheaper to modify than before.

---

## 5. Integrating with Other Agent Skills
`engineering-aggregate` acts as the central collective memory across all specialized skills:
- **`code-guard` / `code-review`**: Before running commit or PR reviews, inherit active laws (`agg.py inherit`). Deposit findings into Pillar 1 & 3 during the tithe.
- **`security-audit`**: Inherit known threat models. Any patched vulnerability automatically generates a new entry in `anti-patterns.md` and an executable verification command in Pillar 4.
- **`tdd` / Feature Dev**: Inherits architectural boundaries and fatal traps so new code is written test-first without violating established invariants.

