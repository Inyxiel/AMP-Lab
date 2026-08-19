# AMP Lab BETA v8 — Canonical Current-State Fix QA

## Goal
Fix the Forge ↔ Respec current-party baseline mismatch without changing the Forge solver/scoring engine.

## Patch
1. Before normal Forge allocation, each source-known current character is reconstructed through the existing canonical Coach `currentCandidate()` + `cloneWithChoices()` path.
2. Arsenal and Shards receive that exact same canonical current snapshot as Forge.
3. `currentCandidate()` now respects `SaveInfo.identity.classes` when the current character is already multiclassed; it reconstructs each class component with `primary` for the first class and `multiclass` for subsequent classes.
4. Unknown/unresolved identities still fall back safely because `cloneWithChoices()` skips null candidates.

## Forge safety guardrails
- Active `v8_solver.js`: **BYTE-FOR-BYTE UNCHANGED** from BETA v7.
- `capability_graph.json`: **BYTE-FOR-BYTE UNCHANGED** from BETA v7.
- Solver data / item scoring / Orb weights: unchanged.
- Respec search algorithm: unchanged.
- Full Party Rebuild search algorithm: unchanged.
- Only `v8_app.js` and `v8_coach.js` are patched.

## Save89 regression
- v7 raw Forge baseline: **654.844**
- v8 canonical normal Forge baseline: **662.344**
- Respec canonical baseline: **662.344**
- Baseline equality: **PASS**
- Search universe remains: **21,231 structural → 3,819 Step3 → 3,426 exact core**
- Forge allocation: **PASS**, 41 used / 41 unique, no duplicate gear, no required slot gaps, no restricted items.
- Arsenal on the same canonical snapshot: **PASS**, 0 source conflicts.

The +7.500 score change is intentional: normal Forge now sees the same level-aware current class/subclass mechanics that Respec already used.

## Save91 guardrail
- v7 base-DB raw Forge baseline: **1852.069**
- v8 canonical base-DB Forge baseline in this harness: **1847.454**
- Allocation invariants: **PASS**, 41/41 unique, no gaps, no restricted items.

This small score movement is from changing the *current character representation*, not from changing the Forge solver. It is expected when raw direct-save inference and canonical class progression disagree.

## Multiclass-current regression
For all 8 real single-class characters in Save89 + Save91, old and new `currentCandidate()` outputs are byte-equivalent.

Synthetic current multiclass test:
- Old: `Fighter 6 · Champion` (incorrectly collapsed to one class)
- New: `Fighter 3 · Champion / Warlock 3 · GreatOldOne`
- Result: **PASS**

## Conclusion
PASS for the requested surgical consistency fix. The Forge engine itself is preserved; normal Forge, Respec baseline, Arsenal and Shards now share the same canonical current character state.
