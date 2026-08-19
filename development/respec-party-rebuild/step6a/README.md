# AMP Lab — Respec Rebuild Step 6A

**Current Party Respec Engine Wiring v1**

This is the first consumer of Steps 1–5. It deliberately does not patch the EXE yet.

Flow per current party member:

`canonical candidates → Step 3 filter → hypothetical override clone → existing solver.allocate() → delta vs frozen current-party baseline`

Safety properties:
- normal snapshot is never mutated;
- current build is retained as control candidate;
- no second gear optimizer exists;
- every expensive candidate is validated by the existing global Forge allocator;
- Step 3 rejection audit is preserved in output;
- no arbitrary `top 3 components / max 6` shortlist is used by this engine.

## Runtime boundary

A real Current Party result cannot be claimed from the Benchmark Fairness EXE alone: Step 3 inventory support and Step 6 Forge deltas require a parsed save/runtime snapshot. This package therefore completes the engine wiring and static QA. Runtime validation is Step 6B and must use a real snapshot from AMP Lab.
