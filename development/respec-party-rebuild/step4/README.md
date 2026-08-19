# AMP Lab — Respec Rebuild Step 4

**Respec Profile Catalog v1 — PASS 12/12**

This is the compact/indexed structural catalog consumed after Step 3 and before expensive hypothetical Forge validation.

## Frozen inputs
- Step 2 canonical multiclass rebase SHA-256: `baf069cf6a62cb9d272c00a1b2d65064678b17604abc5e8ff6de2dde0e58d33e`
- Step 3 filter policy SHA-256: `f6628c6f675ce403af08c07b1a2f03b586de83b8e0cd981f7970787520afe4c8`

## Catalog
- 16 classes
- 133 class/subclass identities
- 384 reusable component buckets
- 436,882 profiles across levels 2–12
- **99,952 exact Level-12 profiles**
- 15,840 O(1) split-range indexes

Each profile is seven integers. Capabilities, proficiencies, resources and spell metadata are not duplicated; component IDs point back to the frozen Step 2 source. This keeps candidate identity stable and lets Step 6 resolve only finalists selected by the Step 3 runtime inventory filter.

No EXE, Forge, fairness weights, solver, or allocation code was modified.
