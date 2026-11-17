# engineering-aggregate

> **Self-Evolving Collective Memory & Intelligence System for AI Coding Agents**  
> *A perpetual engine fueled by user intent: flaws monotonically decrease, token friction drops, and structural strength compounds.*

`engineering-aggregate` turns any codebase into an evolving intelligence system. It eliminates AI context amnesia by routing past discoveries and fatal traps on-demand, while requiring agents to pay back their knowledge debt (the Tithe) at the end of each task without distracting from coding.

---

## The Human Experience: Zero Friction

As a developer, you do **not** need to write retrospectives, inspect token budgets, or run scripts manually.
1. You chat with your AI agent as usual: *"Add user authentication"*, *"Refactor the database pool"*, *"Audit for SSRF vulnerabilities"*.
2. The agent autonomously borrows intelligence at the start via `scripts/agg.py inherit`.
3. The agent implements the task, runs benchmarks, and verifies tests.
4. The agent autonomously files its retrospective tithe via `scripts/agg.py tithe` before finishing.

---

## The 4 Non-Regression Streams

Engineering progress is not just about writing new features—it is about ensuring existing foundations never degrade:

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

1. **Architecture Integrity**: Prevents layer leaks and enforces clean seams (e.g., UI never makes raw disk queries).
2. **Security Immunization**: When a vulnerability (SSRF, auth bypass, injection) is patched, its anti-pattern and automated test are registered so future agents never reintroduce it.
3. **Refactoring Contracts**: Code consolidations lock in quantitative performance thresholds ($<X\text{ ms}$, $<Y\text{ MB RAM}$) so refactors never cause silent regressions.
4. **Knowledge Consolidation**: Algorithmic pruning strips obsolete rules and dead code links, keeping context token-lean.

---

## Core Pillars & Concepts

### 1. The Law of Ancestral Inheritance
Agents never enter a codebase blind. Using a fast, keyword- and path-based index, agents extract only the relevant 20–40 lines of high-leverage invariants and anti-patterns for the exact files they are touching.

### 2. The Law of Equivalent Exchange (The Tithe)
To prevent the knowledge base from decaying into entropy, agents pay back empirical learnings via the **4-Pillar Retrospective**:
1. **Pillar 1: Aggregate Feedback**: Audit of prior rules (`VALIDATED`, `FAILED`, `SITUATIONAL`).
2. **Pillar 2: Novel Discoveries**: Non-obvious runtime realities and line-referenced solutions.
3. **Pillar 3: Anti-Patterns**: Dead ends, failure modes, and required replacements.
4. **Pillar 4: Invariants & Contracts**: Quantitative thresholds and reproduction commands.

### 3. Algorithms Over Token Waste
Instead of wasting context reading hundreds of lines of historical markdown:
- `scripts/agg.py inherit`: Deterministically filters domain rules and prohibited anti-patterns based on touched files or query terms.
- `scripts/agg.py tithe`: Automatically inspects `git diff` to scaffold retrospectives pre-populated with commit SHAs and changed files.
- `scripts/agg.py condense`: Audits dead code pointers and verifies line-budget limits.
- `scripts/agg.py sync`: Auto-discovers and registers new domain knowledge files into the index.
- `scripts/agg.py test`: Regression test suite ensuring the engine remains functional across agent modifications.

---

## Repository Structure

```text
engineering-aggregate/
├── SKILL.md                  # Main skill definition governing agent behavior
├── README.md                 # Public documentation & architecture overview
├── LICENSE                   # MIT License
├── scripts/
│   └── agg.py                # Zero-dependency Python engine (inherit/tithe/condense/sync/test)
├── schemas/
│   ├── index.json            # Schema for knowledge routing index
│   └── retrospective.md      # Detailed 4-pillar retrospective specification
├── workflows/
│   ├── thread-logging.md     # Protocol for paying the tithe post-implementation
│   └── condensation.md       # Distillation, pruning, and entropy prevention rules
└── templates/
    ├── THREAD_TEMPLATE.md    # Standard 4-pillar retrospective template
    └── index.json            # Starter routing dictionary for adopting repos
```

---

## Author & License

Created by **Harshwardhan Patil ([@h45sh](https://github.com/h45sh))**.  
Released under the [MIT License](LICENSE).
