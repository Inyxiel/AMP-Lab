#!/usr/bin/env python3
"""Extract the exact embedded frontend resources from AMP Lab v7.4.8.

This tool intentionally accepts only the verified v7.4.8 Raw Arsenal / Direct
Shards binary so older builds cannot be mixed into the repository by accident.
"""

from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
import re
from pathlib import Path

EXPECTED_SHA256 = "b4367fc3ab6c46123c31b19d2f795e5b765e079179d618b954dcc19ca1ccd571"
EXPECTED_SIZE = 36_457_984
HTML_START = b"<!doctype html>"
HTML_END = b"</html>"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("exe", type=Path, help="AMP Lab v7.4.8 Raw Arsenal / Direct Shards executable")
    parser.add_argument("--out", type=Path, default=Path("recovered/v7.4.8"))
    args = parser.parse_args()

    if not args.exe.is_file():
        raise SystemExit(f"EXE not found: {args.exe}")

    size = args.exe.stat().st_size
    digest = sha256(args.exe)
    if size != EXPECTED_SIZE or digest.lower() != EXPECTED_SHA256:
        raise SystemExit(
            "Refusing to extract: this is not the verified AMP Lab v7.4.8 baseline.\n"
            f"size={size} sha256={digest}"
        )

    blob = args.exe.read_bytes()
    start = blob.find(HTML_START)
    if start < 0:
        raise SystemExit("Embedded HTML start marker not found")

    end = blob.find(HTML_END, start)
    if end < 0:
        raise SystemExit("Embedded HTML end marker not found")
    end += len(HTML_END)

    html_bytes = blob[start:end]
    html = html_bytes.decode("utf-8")

    if "v7.4.8" not in html:
        raise SystemExit("Embedded frontend does not identify itself as v7.4.8")

    matches = re.findall(r'atob\("([A-Za-z0-9+/=]+)"\)', html)
    if len(matches) != 1:
        raise SystemExit(f"Expected exactly one embedded JS payload, found {len(matches)}")

    js_gzip = base64.b64decode(matches[0])
    js_bytes = gzip.decompress(js_gzip)

    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "index.html").write_bytes(html_bytes)
    (args.out / "app.js").write_bytes(js_bytes)

    manifest = (
        "AMP Lab v7.4.8 — Raw Arsenal / Direct Shards\n"
        f"source_exe_sha256={digest}\n"
        f"source_exe_size={size}\n"
        f"embedded_html_offset={start}\n"
        f"embedded_html_size={len(html_bytes)}\n"
        f"embedded_js_size={len(js_bytes)}\n"
    )
    (args.out / "EXTRACTION.txt").write_text(manifest, encoding="utf-8")

    print(manifest, end="")
    print(f"wrote={args.out / 'index.html'}")
    print(f"wrote={args.out / 'app.js'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
