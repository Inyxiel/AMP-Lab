# AMP Lab — Respec / Party Rebuild Development Worklog

This branch preserves the source and QA work completed for the Respec / Full Party Rebuild feature line built on the v8.0.0 Benchmark Fairness baseline.

## Implemented stages

1. Freeze fairness state and canonical baseline validation.
2. Rebase level-aware multiclass data.
3. Canonical candidate filtering and exact-equivalence/dominance refinement.
4. Compact indexed Respec Profile Catalog.
5. Existing hypothetical override / Forge hook audit.
6. Current Party Respec engine + Save91 runtime validation.
7. Full Party Rebuild candidate generation, party-aware pruning, exact prefill and frozen Forge finalist validation.
8. Multiclass breakpoint refinement using frozen progression data.
9. UI/runtime integration, deep-search worker fixes, optimized exact-equivalent solver path, subclass/class icon work, and canonical current-character state reconciliation.

## Important validated checkpoints

- Current Party Respec and Full Party Rebuild use the existing Forge allocator rather than a second independent gear optimizer.
- Save91 validated Full Party result remained 2066.485 through the Step8/Step9 regression chain before the canonical current-state reconciliation.
- Save89 exposed a current Forge vs Respec state mismatch; the v8 canonical-state patch reconciles both paths so the current baseline is identical before hypothetical changes.
- The active Forge scoring/weights were intentionally left unchanged by the canonical-state patch; the change is at the character-state input layer.

## Repository safety

Private BG3 save files (`.lsv`) are intentionally NOT tracked. The repository validation workflow explicitly rejects `.lsv` files. User screenshots and other local/private test inputs are also excluded.

Large Windows build binaries are recorded in `RESPEC_PARTY_REBUILD_ARTIFACT_SHA256SUMS.txt`. The ChatGPT GitHub connector used for this sync can write repository text/source files but cannot directly stream the ~83 MB local EXE as a binary upload, so executable history is represented by checksums rather than committed binary copies.

## Source snapshot

The `development/respec-party-rebuild/source/` directory contains the key runtime/search source snapshots used during the work:

- candidate filter v2
- current-party respec engine
- exact accelerated Forge runner
- full-party frontier/prefill tooling
- breakpoint refinement
- canonical-state build patch
- Step9 runtime payload
- app / coach / solver runtime snapshots

These files are development snapshots and are not a claim that every one is the final standalone production source tree.
