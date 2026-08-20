# AMP Lab v8.0.0 — CP05 Unified Respec R3 Public Test

Release date: 2026-08-20  
Status: **Public Test — verified checkpoint**

## Release summary

CP05 replaces the two competing Respec presentations with one **Unified Respec Suggestions** surface. It combines the source-aware v8 Coach shortlist with the frozen Step9 structural search and final whole-party Forge validation.

This checkpoint is being published for real-player and real-save testing while development continues separately on later choice-selection and Full Party Rebuild work.

## Unified Respec Suggestions

- Shows one **Recommended Result**, one **Single-Class Option**, and one **Alternative Trade-off** per character.
- Suppresses component-identical duplicate cards instead of repeating the same recommendation.
- Shows class/subclass level splits, party and character impact, confidence/source coverage, and canonical Feat/ASI opportunities.
- Recommended equipment comes only from validated physical Forge allocation.
- Item hover details include Game Effects, Passives, Tags, AMP Analysis, and Why Recommended.
- Feat/ASI opportunities remain fail-closed at this checkpoint: no named feat, ASI distribution, or Eldritch Invocation is silently invented. Source-aware named-choice recommendations continue after CP05.

## Performance and cancellation

- Added four-stage progress, live counters, per-party/ruleset cache, character selector, Clear Cache, and Cancel.
- The complete deep Step9 search now runs in a dedicated background Worker.
- Cancel terminates the Worker immediately and discards partial results.
- The UI remains responsive during the structural search.

## Frozen optimizer boundaries

Only the reserved embedded `static/index.html` payload changed from the working CP04 R3 baseline. The following optimizer assets are byte-identical:

- `v8_solver.js`: `f4b00e752e18fc00d7822891be737b32ae7fa936e0255800ce4f9ee11444ce39`
- `solver_data.json`: `1f7fcdad2ee8eb4314b5091c33b5870ca5f761d4d95fcfcaa62bb5519a344e12`
- `capability_graph.json`: `9ecd226f1a4a38078e210fee9f90a01e10833aec0abba0926b1a2ecfb2641996`

The existing Full Party Rebuild engine is preserved unchanged and is not invoked by the CP05 presentation.

## Verification summary

- Vanilla real-browser regression: **12/12 PASS**
- D&D 5.5e & Beyond real-browser regression with Artificer: **12/12 PASS**
- Deep Worker cancellation: **PASS** (`deepActive=false`, no cached or partial result)
- Core Node optimizer regression: **14/14 PASS**
- Global ruleset router regression: **20/20 PASS**
- Icon pipeline browser regression: **10/10 PASS**
- Level Progression browser regression: **13/13 PASS**
- CP05 semantic/frozen-boundary regression: **6/6 PASS**
- Console errors, page errors, failed requests, and 404s: **0**
- Extracted executable payload identity: **848/848 files identical** to the tested build

## Known limitations

- Named Feat/ASI and Eldritch Invocation selection is not part of CP05 and remains ongoing work.
- Some items can still show a generic slot symbol if a packaged/local item icon is unavailable. This is visual only.
- Incomplete equipped-item baselines are shown as **SAVE BASELINE INCOMPLETE** rather than an unreliable `% vs save` value.
- Full Party Rebuild with complete level progression and global inventory allocation belongs to a later checkpoint.

## Windows binary

- **Asset:** `AMP_Lab_v8.0.0_CP05_UNIFIED_RESPEC_R3.exe`
- **Size:** `87,361,536` bytes
- **SHA-256:** `a060656d0875534602a16bb80722a2cf32c971e59d6a6cb0863278113ff35116`
- **Source baseline SHA-256:** `86b0446b64e744401e955660d5bbda330fd95f0d3e83ea1e427900075240775a`
