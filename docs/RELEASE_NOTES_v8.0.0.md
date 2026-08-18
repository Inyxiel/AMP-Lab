# AMP Lab v8.0.0

## Release summary

AMP Lab v8.0.0 is the first public v8 release built around the Phase 8 save/runtime pipeline and the verified Phase 6J physical-item party allocator.

### New UI structure

- **Party Forge** replaces the previous Party naming and presents the optimized four-character loadout in a BG3-inspired equipment layout.
- **Respec Opportunities** replaces Party Coach. `KEEP CURRENT` results are compact; full equipment is shown only when AMP Lab finds a stronger validated respec.
- **Archetypes** replaces the old Builds view and adds **Available Archetypes** with inventory readiness %, S/A/B/C/D/F tier, mechanics available, missing mechanics, supporting items, best subclass fit and best available build.
- Existing optimized build packages remain available under **Best Available Builds**, with additional build directions discovered in unused owned gear.
- **Combos** is now **Synergies**, with player-facing explanations of why linked items work together.
- Arsenal wording and technical explanations were cleaned up for normal players.

### Data and recommendations

- Direct `.lsv` save reading.
- AMP / AMP+ / D&D 5.5e / Compatibility data-source status and management.
- Data-source status colors: `FINISHED` and `ACTIVE` green; `GITHUB SYNC` blue.
- Shard recommendations remain driven by the canonical Shards engine and now have clearer recommendation presentation.
- Dark and Light themes, including the final Light-theme Shards contrast pass.

### Safety / optimizer integrity

The v8 UI work does not replace the optimizer decision engines. The Phase 6J solver, Party Coach/Respec engine, Arsenal engine, Shards engine, save reader and data-source engine remain the source of the underlying results.

### Known limitations

- Some items can still show a generic slot symbol if a packaged/local item icon is unavailable. This is visual only and does not affect item identity or optimization.
- If the loaded save does not provide a complete equipped-item baseline, the UI displays **SAVE BASELINE INCOMPLETE** instead of showing an unreliable `% vs save` value.

## Windows binary

- **Asset:** `AMP_Lab_v8.0.0.exe`
- **Size:** `62,683,648` bytes
- **SHA-256:** `bee3bd10c42dc0d3f5019471bf6aaecd12e9f470755f87bdb840cdf90f36d556`
