# engineering-aggregate

> **Self-Evolving Collective Memory & Intelligence System for AI Coding Agents**

`engineering-aggregate` is an agent skill and engineering framework that transforms software development threads into active learning nodes. It establishes a closed-loop system where agents evaluate prior engineering guidance, discover non-obvious codebase realities, catalog breaking anti-patterns, and condense multi-thread learnings into token-efficient domain knowledge bases.

---

## The Problem It Solves

Most AI coding agents begin every development thread with context amnesia. They repeatedly:
- Walk into subtle codebase traps, race conditions, and timing bugs previously solved in earlier sessions.
- Rely on naive patterns (unbounded buffers, direct DB calls from UI, brittle CI thresholds) that break under scale.
- Bloat context windows when repositories attempt to store unpruned, monolithic development logs.

`engineering-aggregate` solves this by introducing a **4-Pillar Retrospective Protocol** coupled with a **3-Tier Storage & Condensation Architecture**.

---

## The 4-Pillar Retrospective

At the conclusion of an engineering thread, the agent files a standardized retrospective evaluating:
1. **Pillar 1: Aggregate Intelligence Feedback**: Empirical audit of existing principles (`VALIDATED`, `FAILED`, `SITUATIONAL`, `INSUFFICIENT DATA`).
2. **Pillar 2: Novel Discoveries & Codebase Realities**: Precise, line-referenced solutions to subtle bugs and performance cliffs.
3. **Pillar 3: Anti-Patterns & Prohibited Techniques**: Documenting what failed, why it broke, and the mandated replacement.
4. **Pillar 4: Invariants & Performance Contracts**: Preserving quantitative benchmarks ($<X\text{ ms}$, $<Y\text{ MB RAM}$) and security boundaries.

---

## Repository Structure

```text
engineering-aggregate/
├── SKILL.md                  # Main skill definition for AI agent orchestrators
├── README.md                 # Public documentation & architecture overview
├── LICENSE                   # MIT License
├── schemas/
│   └── retrospective.md      # Detailed 4-pillar retrospective specification
├── workflows/
│   ├── thread-logging.md     # Guidelines for authoring post-thread retrospectives
│   └── condensation.md       # Knowledge distillation, pruning, and deduplication rules
└── templates/
    └── THREAD_TEMPLATE.md    # Ready-to-use markdown template for engineering threads
```

---

## Installation & Global Offline Setup

To make `engineering-aggregate` available across all projects on your local system:

```bash
# Symlink into global agent skills directory
ln -s ~/Projects/engineering-aggregate ~/.agents/skills/engineering-aggregate
```

---

## Author & License

Created by **Harshwardhan Patil ([@h45sh](https://github.com/h45sh))**.  
Released under the [MIT License](LICENSE).
