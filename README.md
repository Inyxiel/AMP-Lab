# AMP Lab

Baldur's Gate 3 build and inventory optimizer focused on real party/inventory data, item synergies, class/subclass recommendations, and modded rulesets.

## Current public-test checkpoint

**AMP Lab v8.0.0 — CP07 About & Help R3**

CP07 is the current public-test checkpoint. It builds on the v8 optimizer baseline with a new in-app About / Help guide and the expanded Benchmark Tier List for Pure Vanilla and D&D 5.5e Mod subclass comparisons.

The Windows application reads real BG3 `.lsv` saves directly, detects the active party and owned physical item instances, and presents its results through a BG3-inspired interface. It is read-only and does not modify the save or the game.

Current public-test binary:

- File: `AMP_Lab_v8.0.0_CP07_ABOUT_HELP_R3.exe`
- SHA-256: `8210e950bc218b8dc9afbe5f4d2dd8d303c5fa531d498080b4810594b20c308a`
- Size: `87,361,536` bytes
- Status: **Public Test — current checkpoint**

Windows builds are distributed through [GitHub Releases](https://github.com/Inyxiel/AMP-Lab/releases).

See [CP07 release notes](docs/RELEASE_NOTES_CP07_PUBLIC_TEST.md) for the current checkpoint details.

## Current features

- **Party Forge** — optimized four-character equipment allocation using the physical item instances actually owned by the party; unique items are not duplicated across characters.
- **Unified Respec Suggestions** — combines the source-aware v8 Coach shortlist, deep structural search, and final whole-party Forge validation into one surface.
- **Recommended / Single-Class / Alternative** — presents one validated recommendation, one single-class reference, and one alternative trade-off per character while suppressing component-identical duplicate cards.
- **Level Progression** — displays class/subclass level splits and canonical Level 1–12 feature progression for Vanilla and D&D 5.5e & Beyond rulesets.
- **Benchmark Tier List** — separates **Pure Vanilla** from the **D&D 5.5e Mod** WIP benchmark. Vanilla supports **Naked**, **Orb Only**, **Ring Only**, and **Orb + Ring** scoring, plus Selected Family, Overall Across Families, and Best Compatibility views.
- **AMP rarity labels** — benchmark Orb/Ring controls use **Uncommon / Rare / Epic / Legendary** instead of internal T1–T4 labels.
- **About / Help** — plain-language guide to the app flow, each major result type, benchmark labels, safety guarantees, and troubleshooting.
- **Archetypes** — shows inventory-supported archetype readiness, tiers, available and missing mechanics, supporting items, subclass fit, and best available builds.
- **Synergies** — identifies item-to-item synergy chains and explains why the pieces work together.
- **Arsenal** — analyzes unused owned gear, alternative synergy directions, future Orb pieces, and compatibility.
- **Shards** — canonical shard recommendations with clearer AMP-facing presentation.
- **Data Sources** — AMP, AMP+, D&D 5.5e & Beyond, and compatibility-source status and management.
- **Responsive deep search** — the heavy structural search runs in a background Worker with progress stages, live counters, cache controls, and real cancellation that discards partial results.
- **Dark / Light themes** — including the v8 light-theme contrast QA pass.

## Benchmark Tier List notes

The Pure Vanilla subclass benchmark uses the isolated BG3 Vanilla + GustavX progression model without D&D Beyond progression.

Vanilla benchmark modes:

- **Naked**
- **Orb Only**
- **Ring Only**
- **Orb + Ring**

The Vanilla matrix covers **58 subclasses**, Levels **1–12**, and all **14 AMP Orb families with dedicated matching Rings**. Compatibility scoring is based on source-proven subclass ↔ AMP cross-activation rather than name/theme matching.

The **D&D 5.5e Mod** subclass benchmark remains explicitly marked **WIP / not finalized**.

## Public-test validation notes

The previous CP05 Unified Respec R3 checkpoint established the verified optimizer/runtime baseline, including:

- Vanilla real-browser regression: **12/12 PASS**
- D&D 5.5e & Beyond real-browser regression with Artificer data: **12/12 PASS**
- Core Node optimizer regression: **14/14 PASS**
- Global ruleset router regression: **20/20 PASS**
- Icon pipeline browser regression: **10/10 PASS**
- Level Progression browser regression: **13/13 PASS**
- Deep Worker cancellation: **PASS**
- Console errors, page errors, failed requests, and 404s: **0**

CP07 adds the current About / Help and Benchmark Tier List presentation/data work on top of the v8 public-test line. See [CP05 QA](docs/CP05_UNIFIED_RESPEC_R3_QA.md) for the historical baseline and [CP07 release notes](docs/RELEASE_NOTES_CP07_PUBLIC_TEST.md) for current changes.

## Current public-test limitations

- The **D&D 5.5e Mod Benchmark Tier List** is still WIP and should not be treated as a frozen final ranking.
- Named Feat/ASI and Eldritch Invocation selection remains ongoing work where the source does not support a validated named pick.
- Some items may display a generic slot symbol when a packaged/local item icon is unavailable. This is a presentation limitation only; it does not change item identity, scoring, allocation, mechanics, or recommendations.
- When the current save does not expose a complete equipped-item baseline, Party Forge shows **SAVE BASELINE INCOMPLETE** instead of inventing an inaccurate `% vs save` value.
- Full Party Rebuild remains intentionally heavy and is separate from the normal lightweight recommendation flow.

## Reporting public-test feedback

When reporting an issue, please include:

1. The selected ruleset.
2. The character/build involved.
3. The tab or benchmark mode involved.
4. A screenshot of the result or error.
5. What you expected to happen.
6. Any error message shown by the application.

Useful reports include incorrect item or mechanic interpretations, unreasonable equipment/build choices, missing icons, class/subclass/multiclass recommendations, benchmark/ruleset accuracy, crashes, performance problems, and confusing UI explanations.

## Release model

Public-test and stable Windows binaries are distributed through GitHub Releases. The repository tracks release metadata, checksums, documentation, and recovery/validation tooling. Large third-party source inputs, saves, and runtime snapshots are not committed.

## Free project & supporting the creators

**AMP Lab is free to download and use, and it is intended to remain free.**

AMP Lab does not ask for or accept donations. If you would like to financially support the ecosystem that makes this project possible, please donate **only to the original mod and community-resource creators** through official support links they choose to provide.

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
