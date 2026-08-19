# AMP Lab — Respec Rebuild Step 1 + Step 2

**Status: PASS — 9/9 checks.**

## Step 1 — Freeze Fairness State

Canonical base is `AMP_Lab_v8.0.0_BENCHMARK_FAIRNESS_FIX.exe` with SHA-256 `4f6ccd0abd9068f35ec6b621caa9c2db703a53d0be362d0626de18e238d9edcf`. The normal Forge, benchmark fairness state, solver allocation path and opt-in-only respec override contract are frozen.

Frozen canonical source graph: **16 classes · 119 subclasses · 135 identities**.

## Step 2 — Multiclass Rebase

The multiclass source layer has been rebased directly from the frozen executable's canonical capability graph and Phase 8B.3 spellcasting closure. The dataset preserves the current `expandProfile()` / subclass-unlock / primary-vs-multiclass entry semantics, but does **not** carry over the old top-3 component heuristic or six-candidate shortlist.

This is deliberate: Step 2 is structural/source-canonical only. Step 3 will own the new pipeline:

`LEGAL → RELEVANT → EFFICIENT → INVENTORY-SUPPORTED`

### Structural ordered two-class candidates at level 12

**99,952** before Step 3 filtering.

## Safety

No executable bytes were modified. No fairness weights were changed. No normal Forge code was changed. This package is a frozen input/rebase artifact for the next Respec steps.
