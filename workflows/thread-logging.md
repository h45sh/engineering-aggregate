# Thread Logging Workflow

Protocol for engineering threads capturing their post-implementation insights:

1. **Trigger**: When a feature, bugfix, or refactor has completed code edits and verified tests.
2. **Drafting**: Copy `templates/THREAD_TEMPLATE.md` to `.agents/threads/thread_<topic>.md`.
3. **Execution**:
   - Fill in **Pillar 1** by grading previous advice used in the thread (`VALIDATED`, `FAILED`, `SITUATIONAL`, `INSUFFICIENT DATA`).
   - Fill in **Pillar 2** with any non-obvious reality or code pattern uncovered.
   - Fill in **Pillar 3** with broken approaches, explaining why they failed.
   - Fill in **Pillar 4** with exact numerical bounds and commands to reproduce.
4. **Commit**: Commit the thread retrospective alongside your work or as a dedicated handoff commit.
