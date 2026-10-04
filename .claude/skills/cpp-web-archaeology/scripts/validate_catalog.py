#!/usr/bin/env python3
"""Validate the whole catalog before committing.

Checks: valid JSON list, required fields and types on every record, no duplicate
canonical URLs, no banned hosts (errors). The stricter rules for new manual records
(year/score range, C/C++, evidence count, ...) are reported as warnings, so older or
"automated-harvest" records (tools/cpp-web-archaeology/collector.py) never block a commit.

Usage:
  python3 validate_catalog.py [--catalog PATH]
Exit code 1 on any error.
"""
import argparse
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import catalog_lib as cl  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", default=cl.CATALOG)
    a = ap.parse_args()

    try:
        data = cl.load_json(a.catalog)
    except Exception as e:  # noqa: BLE001
        sys.exit(f"ERROR: catalog is not valid JSON: {e}")
    if not isinstance(data, list):
        sys.exit("ERROR: catalog must be a JSON list")

    hard, soft = [], []
    for i, r in enumerate(data):
        base = cl.validate_record(r, strict=False)
        hard += [f"#{i} {r.get('url', '?')}: {p}" for p in base]
        if r.get("provenance") != "automated-harvest" and not base:
            # rules for new manual records; on older records they are only warnings
            soft += [f"#{i} {r.get('url', '?')}: {p}"
                     for p in cl.validate_record(r, strict=True)
                     if p not in base and not p.startswith("kind ")]  # older kinds are free-form

    dup = collections.Counter(cl.canon(r.get("url", "")) for r in data)
    for c, n in dup.items():
        if n > 1:
            hard.append(f"duplicate URL x{n}: {c}")

    for e in soft:
        print("WARN ", e)
    for e in hard:
        print("ERROR", e)
    print(f"\n{len(data)} records checked: {len(hard)} errors, {len(soft)} warnings.")
    sys.exit(1 if hard else 0)


if __name__ == "__main__":
    main()
