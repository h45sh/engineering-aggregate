# Knowledge Condensation & Pruning Protocol

This document defines the distillation algorithms and pruning heuristics for synthesizing multi-thread retrospectives into token-efficient domain knowledge bases.

---

## 1. Storage Tiers & Token Bounds

```text
 Tier 1: Global Laws (AGENTS.md)
  └── Max 250 lines. High-leverage repository invariants, security rules, and architectural seams.

 Tier 2: Domain Knowledge Bases (.agents/knowledge/<domain>.md)
  └── 50–150 lines per domain. Specific patterns, framework quirks, performance thresholds.

 Tier 3: Historical Thread Archive (.agents/threads/*.md)
  └── Raw, unpruned thread reports. Retained for auditability; NEVER read by agents on startup.
```

---

## 2. The Promotion Rules (Rule of Three)

1. **Promotion to Global (Tier 1)**:
   - When a principle is marked `VALIDATED` across 3 distinct thread files across different subsystems, promote it to `AGENTS.md`.
2. **Promotion to Domain Knowledge (Tier 2)**:
   - When a novel discovery in Pillar 2 is confirmed in practice, add it to the corresponding `.agents/knowledge/<domain>.md` file.

---

## 3. Anti-Pattern Cataloging

- When an approach is marked `FAILED` in Pillar 3, it is immediately cataloged in `.agents/knowledge/anti-patterns.md`.
- Anti-pattern entries must always specify:
  1. The prohibited technique.
  2. The exact failure mode.
  3. The mandated replacement.

---

## 4. Situational Flagging & De-duplication

- Never append duplicate summaries. If a new thread provides nuanced context for an existing rule, update the rule with an explicit condition:
  `"[CONDITION: macOS CI runners] Set benchmark query threshold to <500ms due to multi-tenant CPU variance."`
- Prune obsolete or superseded rules when a cleaner architectural pattern replaces them.
