# AMP Lab v8.0.0 — CP07 About & Help R3 Public Test

Release date: 2026-08-20  
Status: **Public Test — current checkpoint**

## Release summary

CP07 builds on the v8 public-test line with a new in-app **About / Help** surface and the expanded **Benchmark Tier List** work. The optimizer, Party Forge, save reader, and physical-item allocation remain separate from the guide/presentation layer.

## About / Help

- Adds a dedicated **About AMP Lab** page and Help entry point.
- Explains the end-to-end flow from ruleset selection and save reading through Build Recommendations, Synergies, progression, Respec Suggestions, and Full Party Rebuild.
- Documents key safety guarantees: **owned items only**, **one item / one owner**, **ruleset isolation**, and **fail-closed unknown mechanics**.
- Adds plain-language explanations for labels such as **FORGE VALIDATED**, **BENCHMARK**, **RECOMMENDED PICK**, and **TRADE-OFF / ALTERNATIVE**.
- Includes troubleshooting guidance for ruleset mismatches, missing items, slow rebuilds, and unexpected scores.

## Benchmark Tier List

### Rulesets

- Restores a clear split between **Pure Vanilla** and **D&D 5.5e Mod** subclass benchmarking.
- The D&D 5.5e Mod benchmark remains explicitly marked **WIP / not finalized**.
- Vanilla uses the isolated BG3 Vanilla + GustavX progression model without D&D Beyond progression.

### Vanilla scoring modes

The Vanilla subclass benchmark supports separate states rather than locking every comparison to one equipment mode:

- **Naked**
- **Orb Only**
- **Ring Only**
- **Orb + Ring**

The Vanilla matrix covers **58 subclasses**, Levels **1–12**, all **14 AMP Orb families with dedicated matching Rings**, and the fixed Orb/Ring benchmark states used by AMP Lab.

### Ranking views

- **Selected Family**
- **Overall Across Families**
- **Best Compatibility**

Compatibility is based on source-proven subclass ↔ AMP cross-activation rather than name/theme matching.

### Rarity labels

The player-facing benchmark UI now uses the actual rarity names:

- **Uncommon**
- **Rare**
- **Epic**
- **Legendary**

Internal numeric tier indices remain implementation details and are no longer the primary UI labels.

## Safety / optimizer integrity

CP07 presentation and benchmark work does not replace the underlying Party Forge / optimizer decision engines. The application remains read-only with respect to BG3 saves.

## Windows binary

- **Asset:** `AMP_Lab_v8.0.0_CP07_ABOUT_HELP_R3.exe`
- **Size:** `87,361,536` bytes
- **SHA-256:** `8210e950bc218b8dc9afbe5f4d2dd8d303c5fa531d498080b4810594b20c308a`
