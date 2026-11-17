# Knowledge Condensation & Entropy Prevention Protocol

This document defines the distillation algorithms, pruning heuristics, and maintenance checks for synthesizing multi-thread retrospectives into token-efficient domain knowledge bases.

---

## 1. Storage Tiers & Token Bounds

```text
 Tier 1: Global Laws (AGENTS.md)
  └── Max 250 lines. Universal repository invariants, security rules, and architectural seams.

 Tier 2: Domain Knowledge Bases (.agents/knowledge/<domain>.md)
  └── 50–150 lines per domain. Filtered and delivered on-demand via scripts/agg.py inherit.

 Tier 3: Historical Thread Archive (.agents/threads/*.md)
  └── Raw, unpruned thread reports. Retained for auditability; NEVER read by agents on startup.
```

---

## 2. Automated Condensation via `scripts/agg.py`

Run the condensation audit:
```bash
python3 scripts/agg.py condense
```

The script automatically executes:
1. **Line Budget Verification**: Checks that `AGENTS.md` remains $\le 250$ lines and domain files remain $\le 150$ lines.
2. **Dead Reference Detection**: Scans all `path/to/file.py:L12` pointers in knowledge bases. If a file was renamed or deleted, it flags the stale entry.

---

## 3. The Promotion Rules (Rule of Three)

1. **Promotion to Global (Tier 1)**:
   - When a principle is marked `VALIDATED` across 3 distinct thread files across different subsystems $\rightarrow$ Promote it to `AGENTS.md`.
2. **Promotion to Domain Knowledge (Tier 2)**:
   - When a novel discovery in Pillar 2 is confirmed in practice $\rightarrow$ Add it to the corresponding `.agents/knowledge/<domain>.md` file and register its keywords in `index.json`.

---

## 4. Anti-Pattern Immediate Cataloging

- When an approach is marked `FAILED` in Pillar 3, it is immediately cataloged in `.agents/knowledge/anti-patterns.md` and added to `index.json` under `anti_patterns`.
- Anti-pattern entries must always specify:
  1. The prohibited technique.
  2. The exact failure mode.
  3. The mandated replacement.

---

## 5. Situational Flagging & De-duplication

- Never append duplicate summaries. If a new thread provides nuanced context for an existing rule, update the rule with an explicit condition:
  `"[CONDITION: macOS CI runners] Set benchmark query threshold to <500ms due to multi-tenant CPU variance."`
- Prune obsolete or superseded rules when a cleaner architectural pattern replaces them.
