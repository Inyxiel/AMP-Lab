# AMP Lab — Respec Rebuild Step 3 v2

**Concrete-Demand + Safe Dominance Filter — PASS**

This replaces Step 3 v1 after the real QuickSave 91 QA showed that `any owned support` retained all 100,071 candidates.

## Save 91 result

`100,071 LEGAL → 100,071 RELEVANT → 56,332 exact-state representatives → 43,063 EFFICIENT / INVENTORY-SUPPORTED`

That is **57,008 candidates removed (56.968%)** without a Top-N, percentile cutoff, random sample, or score quota.

Breakdown:
- **43,739** exact frozen-solver-state equivalents removed.
- **13,269** candidates removed only when projected demanded mechanics, proficiencies, Dual Wielder state, and matrix **path structure are identical**, while another candidate is no worse on every corresponding frozen row-weight term.
- **119 single-class profiles are all preserved.**

The runtime demand universe on Save 91 is **314 requirement keys**, **38 proficiency groups**, and all **14 owned Orb families**. Raw class capabilities that no owned item/orb path can query do not create fake candidate distinctions.

## Important safety correction

An earlier experimental dominance rule could reduce the set to about 22k by treating capability supersets as always better. That rule is **not used**. The frozen Forge awards a completion-item bonus when gear closes missing path requirements, so “more guaranteed capabilities” is not strictly monotonic in the present solver. v2 deliberately keeps the larger 43,063 frontier rather than risk a false prune.

## What this means for #6B

Step 3 is now genuinely selective, but **43k full `allocate()` calls are still not acceptable**. The next gate should be inside Current Party Respec: cache the unchanged three party members / producer index / inventory work, run a cheap exact candidate-core screen, and invoke the full frozen Forge only on the resulting finalists. That is an engine/runtime optimization, not another arbitrary candidate shortlist.

No bytes in the Benchmark Fairness EXE, fairness weights, normal Forge scoring, or allocation semantics were modified.
