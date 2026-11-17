# Thread Logging & Equivalent Exchange Workflow

This workflow guides agents in paying their knowledge debt (the Tithe) at the conclusion of every implementation thread.

---

## The Zero-Distraction Principle
Agents must NEVER spend attention or context worrying about retrospective logging while in the middle of code writing, debugging, or test verification. 

1. **Phase 1: Code & Verify**: Deliver clean, working code. Run tests. Ensure build succeeds.
2. **Phase 2: The Tithe**: Only after Phase 1 succeeds, execute the tithe protocol below.

---

## Step-by-Step Tithe Execution

### 1. Scaffold Retrospective
Run the zero-token scaffold command:
```bash
python3 scripts/agg.py tithe --topic <feature_name> --domain <DomainName>
```
This reads the git status and diff automatically, creating `.agents/threads/thread_<topic>.md`.

### 2. Fill the 4 Pillars
Open the scaffolded file and record the empirical observations:
- **Pillar 1 (Aggregate Feedback)**: Did the rules you borrowed hold up? Mark as `VALIDATED`, `FAILED`, `SITUATIONAL`, or `INSUFFICIENT DATA`.
- **Pillar 2 (Novel Discoveries)**: What hidden behavior or runtime quirk did you discover? Include exact line pointers: `src/foo.py:L45-L60`.
- **Pillar 3 (Anti-Patterns / Prohibited)**: What attempt failed? What is the mandated alternative?
- **Pillar 4 (Invariants & Benchmarks)**: What latency/memory/security boundary was maintained? Provide the exact bash reproduction command.

### 3. Commit
Commit the thread retrospective alongside your implementation commit or as a dedicated handoff commit:
```bash
git add .agents/threads/thread_<topic>.md
git commit -m "docs(aggregate): record thread retrospective for <topic>"
```
