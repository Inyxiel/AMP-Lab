# AMP Lab

Baldur's Gate 3 build and inventory optimizer focused on real party/inventory data, item synergies, class/subclass recommendations, and modded rulesets.

## Current release

**AMP Lab v8.0.0 — Party Forge / Archetypes / Respec Opportunities**

v8.0.0 moves AMP Lab to the Phase 8 optimizer/runtime line while keeping the verified Phase 6J physical-item allocation core intact. The Windows release reads real BG3 `.lsv` saves directly and presents the optimizer through the new BG3-inspired interface.

Current verified binary:

- File: `AMP_Lab_v8.0.0.exe`
- SHA-256: `bee3bd10c42dc0d3f5019471bf6aaecd12e9f470755f87bdb840cdf90f36d556`
- Size: `62,683,648` bytes

## v8 highlights

- **Party Forge** — optimized four-character equipment allocation using owned physical item instances.
- **Respec Opportunities** — validates legal class/subclass/multiclass alternatives against the real inventory; `KEEP CURRENT` stays compact and equipment is shown only for actual respec recommendations.
- **Archetypes** — inventory-supported archetype readiness, tiers, available mechanics, missing mechanics, supporting items, subclass fit, and best available builds.
- **Synergies** — item-to-item synergy chains with player-facing explanations of why the pieces work together.
- **Arsenal** — unused owned gear, alternative synergy directions, future Orb pieces, and human-readable compatibility guidance.
- **Shards** — canonical shard recommendations with clearer AMP recommendation presentation.
- **Data Sources** — AMP, AMP+, D&D 5.5e and compatibility source status/management.
- **Dark / Light themes** — including the v8 light-theme contrast QA pass.

## Known UI limitation

Some items may still display a generic slot symbol when a packaged/local item icon is unavailable. This is a presentation limitation only; it does not change item identity, optimizer scoring, allocation, mechanics, or recommendations.

When the current save does not expose a complete equipped-item baseline, Party Forge shows **SAVE BASELINE INCOMPLETE** rather than inventing an inaccurate `% vs save` value.

## Release model

Stable Windows builds are distributed through GitHub Releases. The repository tracks release metadata, checksums, documentation and recovery/validation tooling. Large third-party source inputs, saves and runtime snapshots are not committed.

## Free project & supporting the creators

**AMP Lab is free to download and use, and it is intended to remain free.**

AMP Lab does not currently ask for or accept donations. If you would like to financially support the ecosystem that makes this project possible, please consider supporting the original mod and community-resource creators directly through any official donation or support links they choose to provide.

## Credits & Acknowledgements

AMP Lab is an independent community project and is not an official project of the mod creators or community resources it supports.

Special thanks and full credit to:

- **Paramonov / Paramonov95** — Ancient Mega Pack (AMP)
- **Paramonov** — Ancient Mega Pack Plus (AMP+)
- **Paramonov** — Ancient Mega Pack + DnD 5.5e BEYOND compatibility patch
- **Yoonmoonsik** — DnD 5.5e All-in-One BEYOND
- **Tazliel** — AMPIS item database / reference resource

AMP Lab does not claim ownership of their mods, assets, databases, data, item designs, or ruleset implementations. See [CREDITS.md](CREDITS.md) for full attribution and links to the original projects.

## Third-party data

Large mod/data inputs are deliberately excluded from the repository, including `.pak` files, AMPIS full-detail exports, spreadsheets, save files, and runtime snapshots. These may contain third-party content and are treated as local development inputs rather than repository source.

## Security

Never commit `.env` files, API keys, local save data, runtime snapshots, machine-specific configuration, or private paths.
