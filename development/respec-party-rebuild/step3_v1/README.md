# AMP Lab — Respec Rebuild Step 3

**Canonical Candidate Filter v1 — PASS 11/11**

Pipeline: `LEGAL → RELEVANT → EFFICIENT → INVENTORY-SUPPORTED`.

This layer is deliberately separate from Forge. It consumes the Step 2 canonical multiclass structures plus runtime owned-item/orb context and returns an auditable candidate set for later expensive `allocate()` validation.

## Key change from Phase 8B.3

The old `top 3 components → max 6 candidates` shortcut is **not present**. Step 3 filters by source legality and actual owned inventory/orb support. The current build remains a control candidate even when contextual support is zero.

## Static L12 input

- 16 classes
- 119 subclasses
- 2,640 ordered class/split rows
- 99,952 structural ordered two-class candidates before contextual filtering

## Runtime boundary

The final `RELEVANT` and `INVENTORY-SUPPORTED` counts depend on the player's actual save inventory. This package does not fabricate a sample inventory to claim a fake reduction ratio. Step 6 will feed the real snapshot into this filter.

No EXE bytes, fairness weights, Forge scoring, or solver allocation code were modified.
