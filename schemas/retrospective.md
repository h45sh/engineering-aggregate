# Retrospective Specification Schema

This document defines the formal schema and validation rules for post-thread retrospectives authored under the `engineering-aggregate` framework.

---

## 1. Metadata Header

Every retrospective MUST begin with YAML or Markdown metadata:

```markdown
# Thread Retrospective: <Feature / Bugfix / Refactor Topic>

- **Branch / PR**: `<branch-name>` (Commit `<sha>`)
- **Primary Domain**: `[UI | Engine | Storage | Benchmarks | AI / LLM | Security | Tooling | CLI]`
- **Touched Files**:
  - `path/to/file_a.py`
  - `path/to/file_b.py`
```

---

## 2. The 4 Pillars Specification

### Pillar 1: Aggregate Intelligence Feedback
Audits techniques previously recorded in `.agents/knowledge/` or `AGENTS.md` that were utilized during the session.

```markdown
| Technique / Rule Consulted | Outcome | Assessment | Detail & Context |
| :--- | :---: | :---: | :--- |
| <Exact name of pattern> | **<Outcome>** | <Assessment> | <Empirical rationale and conditions> |
```

#### Valid Outcome Values:
- **`VALIDATED`**: The technique held true without regressions or bugs across all test runs.
- **`FAILED`**: The technique broke, threw unexpected exceptions, or created architectural friction.
- **`SITUATIONAL`**: The technique functions only under specific constraints (e.g. single-threaded, specific OS, or narrow input ranges).
- **`INSUFFICIENT DATA`**: Insufficient runs or edge cases to form a conclusive determination.

---

### Pillar 2: Novel Discoveries & Codebase Realities
Documents non-obvious runtime quirks, race conditions, hidden performance boundaries, or architectural seams uncovered during development.

Each entry MUST follow this 4-field structure:
- **Principle**: Concise, declarative name of the insight.
- **Problem Solved**: The specific bug, memory leak, race condition, or friction resolved.
- **Mechanism**: How the solution works at the system/code layer.
- **Code Reference**: Exact file pointer with line numbers (e.g. `src/database/pool.py:L45-L78`).

---

### Pillar 3: Anti-Patterns & Prohibited Techniques (What NOT to do)
Documents dead ends, failed attempts, and dangerous patterns future agents must strictly avoid.

Each entry MUST follow this 3-field structure:
- **Anti-Pattern**: Clear name of the prohibited pattern.
- **Why it Failed**: Root cause of failure (e.g. deadlocks, unhandled async exceptions, state corruption).
- **Correct Replacement**: The mandatory alternative technique.

---

### Pillar 4: Invariants & Performance Contracts to Preserve
Documents quantitative bounds, algorithmic complexities, and security guarantees verified during the thread.

```markdown
| Contract / Invariant | Threshold / Guarantee | Verification Command |
| :--- | :--- | :--- |
| <Name of invariant> | <Quantitative bound, e.g. <50ms or <=10MB> | `<exact bash test command>` |
```

---

## 3. Validation Rules
- All file references in Pillar 2 MUST point to real files in the repository.
- Verification commands in Pillar 4 MUST be executable non-interactively via bash.
- Empty or placeholder pillars are prohibited; if no novel discovery occurred, explicitly state `None identified`.
