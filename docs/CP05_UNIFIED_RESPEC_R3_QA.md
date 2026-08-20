# AMP Lab v8 — CP05 Unified Respec R3 QA

Status: **PASS — checkpoint ready for public testing**

## What changed

- Replaced the two competing Respec presentations with one **Unified Respec Suggestions** surface.
- Combines the source-aware v8 Coach shortlist with the frozen Step9 structural search and final whole-party Forge validation.
- Shows one **Recommended Result**, one **Single-Class Option**, and one **Alternative Trade-off** per character.
- Suppresses component-identical duplicate cards instead of repeating the same recommendation.
- Shows class/subclass level splits, party and character impact, confidence/source coverage, and canonical Feat/ASI opportunities.
- Feats remain fail-closed: **+10 benchmark value per canonical opportunity** and **CHOICE_REQUIRED**; no specific feat is silently selected.
- Recommended equipment comes only from the validated physical Forge allocation.
- Item hover details include game effects, passives, tags, AMP Analysis, and Why Recommended.
- Added four-stage progress, live counters, per-party/ruleset cache, character selector, Clear Cache, and Cancel.
- The complete deep Step9 search now runs in a dedicated background Worker. Cancel terminates it immediately and discards all partial results.

## Frozen boundaries

Only the reserved embedded `static/index.html` payload changed. The following optimizer assets are byte-identical to the working CP04 R3 baseline:

- `v8_solver.js`: `f4b00e752e18fc00d7822891be737b32ae7fa936e0255800ce4f9ee11444ce39`
- `solver_data.json`: `1f7fcdad2ee8eb4314b5091c33b5870ca5f761d4d95fcfcaa62bb5519a344e12`
- `capability_graph.json`: `9ecd226f1a4a38078e210fee9f90a01e10833aec0abba0926b1a2ecfb2641996`

The existing Full Party Rebuild engine is preserved unchanged for a later checkpoint and is not invoked by the CP05 presentation.

## Test results

- CP05 Vanilla real-browser regression: **12/12 PASS**
- CP05 5.5e & Beyond real-browser regression with Artificer: **12/12 PASS**
- Deep Worker cancellation: **PASS** (`deepActive=false`, no cached/partial result)
- Core Node optimizer regression: **14/14 PASS**
- Global ruleset router regression: **20/20 PASS**
- Icon pipeline browser regression: **10/10 PASS**
- Level Progression browser regression: **13/13 PASS**
- CP05 semantic/frozen-boundary regression: **6/6 PASS**
- Console errors, page errors, failed requests, and 404s: **0**
- Extracted executable payload identity: **848/848 files identical** to the tested build

The older CP01 browser script still stops when it tries to manipulate the intentionally disabled local Benchmark ruleset selector. This is the same inherited result as CP04 R3; the newer global-router CP02 suite supersedes it and passes 20/20.

## Executable

- File: `AMP_Lab_v8.0.0_CP05_UNIFIED_RESPEC_R3.exe`
- Size: `87,361,536` bytes
- SHA-256: `a060656d0875534602a16bb80722a2cf32c971e59d6a6cb0863278113ff35116`
- Source baseline SHA-256: `86b0446b64e744401e955660d5bbda330fd95f0d3e83ea1e427900075240775a`
- Embedded index: `261,679 / 268,224` reserved bytes (`6,545` bytes free)

## Suggested manual test

1. Open a known working save and run **Build Recommendations**.
2. Open **Respec Opportunities** and choose **Build Unified Suggestions**.
3. Confirm that progress keeps moving and the rest of the UI remains responsive.
4. Switch all four character selectors and inspect Recommended, Single-Class, and Alternative cards.
5. Hover recommended items and verify the full tooltip.
6. Run again to verify the cache, then Clear Cache and test Cancel during the Deep Search stage.
7. Repeat once in Vanilla and once in 5.5e & Beyond.

## Ongoing development excluded from CP05

- Source-aware named Feat/ASI and Eldritch Invocation selection continues after this checkpoint.
- Full Party Rebuild with complete level progression and global inventory allocation belongs to a later checkpoint.
