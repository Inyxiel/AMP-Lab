# AMP Lab v8 BETA v7 — Save89 Full Regression QA

## Test target
- EXE: `AMP_Lab_v8.0.0_RESPEC_PARTY_REBUILD_STEP9_BETA_v7.exe`
- EXE SHA-256: `8a969aa79fea9993dd059e3da3a551624158d8915145be760e351251eb3d59d6`
- Save: `QuickSave_89.lsv`
- Save SHA-256: `8c265c3fd8412a19b006c6e2b6c504fe454ee6e0966c452ddf2e77826f7f383f`
- Parsed party: 4 characters, all Level 6
- Physical item instances: 1208 / unique UUIDs 1208

## Overall result
**QA PARTIAL PASS — core systems run, but production-readiness is blocked by cross-module consistency issues.**

### PASS — Forge runtime/invariants
- Active v7 Forge: PASS
- Direct-save party score: **654.844**
- Physical items assigned: 41 / unique 41
- Duplicate physical assignment: **none**
- Required standard slot gaps: **none**
- Restricted/non-equippable items selected: **none**
- Selected items missing from save: **none**
- Selected raw/internal names: **none**
- Deterministic rerun reproduced score **654.844** and the same four Orb families.

### PASS — Respec search executes
- Status: PASS
- Legal paths: 21231 per Level-6 slot universe / canonical search reported 21,231 legal paths
- Exact core profiles: 3,426
- Level-aware baseline: **662.344**
- Best validated individual what-if: **704.899**
- Harness runtime: ~56.5s for Current Respec on this environment (performance warning, not a crash).

Current-respec winners:
- Dark Urge: **RESPEC** — Fighter 3 · Champion / Warlock 3 · GreatOldOne · Party Δ +42.555 · Build Δ +38.213
- Karlach: **RESPEC** — Fighter 6 · Champion · Party Δ +19.526 · Build Δ +19.526
- Lae'zel: **KEEP CURRENT** — Fighter 6 · PsiWarrior · Party Δ +0.000 · Build Δ +0.000
- Shadowheart: **RESPEC** — Druid 3 · CircleOfTheLand / Gunslinger 3 · Spellslinger · Party Δ +20.024 · Build Δ -1.577

### PASS — Full Party Rebuild executes
- Status: PASS
- Canonical baseline: **662.344**
- Validated rebuild: **714.090**
- Gain: **+51.746 (+7.81%)**
- Full Forge finalists: 13
- Harness runtime: ~6.95s

### PASS — Arsenal core analysis
- Status: PASS
- Raw physical items: 1208
- Mechanics-known instances: 394
- Forge used: 41
- Unused equippable known: 146
- Near upgrades: 20
- Source conflicts: 0
- Unknown/unscored physical instances: 814 — mostly consumables/objects/keys/summon containers; **0 unknown equipped anchors**.

### PASS — AMP / AMP+ item source coverage
- Source export: 3961 / expected 3961; failures: 0
- Global AMP/AMP+ Stats IDs missing from solver: **0**
- Save89 AMP/AMP+ unique Stats IDs: 241
- Save89 AMP/AMP+ IDs missing from solver: **0**
- Save89 AMP/AMP+ bad display names in authoritative source coverage: **0**
- Save89 AMP/AMP+ missing source icons: **0**

### PASS — Benchmark structural integrity
Vanilla:
- 12 base classes + 58 subclasses = **70 identities**
- 779 progression rows
- Duplicate/malformed/non-finite/gain mismatch/regression: **0 / 0 / 0 / 0 / 0**

5.5e & Beyond:
- 16 base classes + 119 subclasses = **135 identities**
- 1392 progression rows
- Missing vs Capability Graph: **0**
- Parent mapping issues: **0**
- Duplicate/malformed/non-finite/gain mismatch/regression: **0 / 0 / 0 / 0 / 0**

Item Tier v0.7 separate audit:
- 2,391 canonical tier rows
- 16 comparison groups
- duplicate Stats IDs: 0
- non-finite scores: 0
- broken per-group rank sequences: 0

## Confirmed issues

### P1 — Forge / Respec current baseline mismatch
Normal direct-LSV Forge scores the Save89 current party at **654.844**, while Respec first applies canonical level-aware current class/subclass capabilities and scores the same current party at **662.344** (Δ **+7.500**).

This is a correctness/interface consistency issue: normal Forge and Respec do not start from the same representation of the current spec on mid-level direct `.lsv` saves. The direct parser supplies identity/level reliably, but not the optimizer capability override fields; Respec reconstructs them from the Capability Graph.

**Recommended fix:** create one shared `canonicalCurrentSnapshot()` step and use it for normal Forge, Current Respec baseline, Full Party baseline, Arsenal fit and Shards. Do not run deep search at startup; only canonicalize the four current identities.

### P1/P2 — Proficiency authority mismatch between Forge data and Respec Capability Graph
- Identities checked: 135
- Identities with different proficiency sets: **83**
- All differences are extra proficiencies in the Forge `profs` table; canonical graph had no extra proficiencies absent from Forge in this audit.

Examples include Death Domain / Cleric, Ranger subclasses, Warlock subclasses, Wizard subclasses, etc. Because `applyCandidate()` sets `optimizer_override_proficiencies` from the Capability Graph, hypothetical respecs can have a narrower legal-equipment set than the same identity receives through normal Forge defaults.

**Recommended fix:** define one authoritative proficiency resolver with primary-vs-multiclass entry semantics. Preserve subclass-granted/legacy-specific proficiencies from the Forge source rather than blindly replacing them with the compact capability list.

### P1/P2 — Soul Orb scope mismatch
Benchmark families: **15**; live Forge matrix families: **14**.
Benchmark-only family: **Soul / Orb of the First Soul**.

The item exists in the source/solver item profile, and the Tier Viewer explicitly treats First Soul as an Orb-only family, but live Forge does not have a Soul matrix/bridge family and its normal Orb ID matcher does not recognize `AMP_Koy_Orb_Soul_T*` as an Orb anchor.

**Consequence:** if First Soul is meant to participate in Forge, Respec or Full Party Rebuild, those systems can never choose it. If the intended canonical search truly has only 14 ringed families, then the Benchmark should not include Soul in Best Orb Set normalization/ranking. This needs one explicit canonical decision.

### P2 — Arsenal still exposes internal Stats IDs
User-facing raw names found in Save89 Arsenal output:
- `MAG_Voltedge`
- `SCL_SpidersLyre`
- `WPN_Longbow_2`
- `WPN_Whip_2`

This includes `MAG_Voltedge`, which was already visible in earlier Alternative Build Directions QA. The presentation fallback is therefore not complete.

### P2 UI — requested “subclass icons” are not actual subclass icons
The current Party Forge decorator uses **class glyphs** (⚔, ✚, ✦, etc.) with level badges for multiclass. The Benchmark uses the same class glyph plus a two-letter subclass code. These are clean badges, but they are **not unique subclass image/icon assets**. If the requirement is actual subclass icons, the previous icon task is not fully satisfied.

### P3 — Current Respec runtime is still heavy
The Current Respec harness took ~56.5s on Save89; Full Party Rebuild took ~6.95s. It completes and is not the old startup hang, but Current Respec is still a performance target.

## Watchlist, not confirmed bugs
- `Eldritch Knight` is the Level-12 5.5e naked-score leader at 192.6 (~2.38σ above the subclass mean). Data integrity checks pass; this is a scoring-model outlier, not evidence of corruption. Audit its contribution breakdown separately before changing weights.
- Save-direct equipment fidelity remains partial by design. Owned physical inventory is authoritative; exact current slot/swap instructions should use Runtime Sync when needed.
- One unknown Save89 Stats ID looks equipment-like (`Sailor_Alchemist_Gloves_VSENC`), but it is not equipped and is not selected by Forge. Keep it on mapping watchlist rather than treating it as a confirmed missing player item.

## Recommended patch order
1. **Unify current-party canonical baseline** across Forge/Respec/Full Party/Arsenal.
2. **Reconcile proficiency authority** for current and hypothetical profiles.
3. Decide **Soul Orb** canonical policy and make Benchmark + Forge agree.
4. Resolve/fallback the four Arsenal raw names.
5. Replace generated glyph badges with real subclass icons if actual artwork/icons are required.
6. Optimize Current Respec runtime after correctness is frozen.
