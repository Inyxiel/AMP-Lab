# AMP Lab

Baldur's Gate 3 build and inventory optimizer focused on real party/inventory data, item synergies, class/subclass recommendations, and modded rulesets.

## Current baseline

**AMP Lab v7.3.5 — Tooltip Restore Fix**

This repository is intentionally based only on the v7.3.5 Windows executable. Older source snapshots are not being mixed into this codebase.

Current verified binary:

- File: `AMP20Lab_v7.3.5_Tooltip-Restore-Fix.exe`
- SHA-256: `2b7f75480c27072c9447624aa6356c9cc217f922cc818b95a20766e188c2ae5c`
- Size: `36,457,984` bytes

## Recovery status

The v7.3.5 executable contains recoverable embedded frontend resources. The recovery tooling in this repository extracts the exact embedded HTML and gzip/base64 JavaScript payload from that binary.

The original Go source code is **not** embedded as source text in the compiled executable, so a reproducible automatic Windows build is not enabled yet. We will not substitute older source code just to make the build appear reproducible.

## Releases

GitHub Release automation will be enabled only after the v7.3.5 backend/build path is reproducible. Until then, release publishing remains intentionally manual/safe.

## Third-party data

Large mod/data inputs are deliberately excluded from the repository, including `.pak` files, AMPIS full-detail exports, spreadsheets, save files, and runtime snapshots. These may contain third-party content and are treated as local development inputs rather than repository source.

## Security

Never commit `.env` files, API keys, local save data, runtime snapshots, machine-specific configuration, or private paths.
