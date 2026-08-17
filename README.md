# AMP Lab

Baldur's Gate 3 build and inventory optimizer focused on real party/inventory data, item synergies, class/subclass recommendations, and modded rulesets.

## Current baseline

**AMP Lab v7.4.8 — Raw Arsenal / Direct Shards**

This repository is intentionally based only on the current v7.4.8 Windows executable. Older source snapshots are not being mixed into this codebase.

Current verified binary:

- File: `AMP20Lab_v7.4.8_Raw-Arsenal-Direct-Shards.exe`
- SHA-256: `b4367fc3ab6c46123c31b19d2f795e5b765e079179d618b954dcc19ca1ccd571`
- Size: `36,457,984` bytes

## Recovery status

The v7.4.8 executable contains recoverable embedded frontend resources. The recovery tooling in this repository extracts the exact embedded HTML and gzip/base64 JavaScript payload from that binary.

The original Go source code is **not** embedded as source text in the compiled executable, so a reproducible automatic Windows build is not enabled yet. We will not substitute older source code just to make the build appear reproducible.

## Releases

Stable Windows builds are published through GitHub Releases. The repository baseline is now **v7.4.8 — Raw Arsenal / Direct Shards**.

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
