#!/usr/bin/env python3
"""Append new records to cpp-web-archaeology/data/projects.json.

Existing records are never edited or reordered. New records go at the end.
Refuses to add anything that fails validation or whose canonical URL already exists.

Usage:
  python3 append_catalog.py merged.json [--dry-run]
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import catalog_lib as cl  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("new")
    ap.add_argument("--catalog", default=cl.CATALOG)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    data = cl.load_json(a.catalog)
    have = {cl.canon(r["url"]) for r in data}
    added, skipped = [], []
    new = cl.load_json(a.new)
    if not isinstance(new, list):
        sys.exit(f"{a.new} must be a JSON list of records (use merge_batch.py output)")
    for r in new:
        probs = cl.validate_record(r, strict=True)
        c = cl.canon(r.get("url", ""))
        if probs:
            skipped.append((r.get("url"), "; ".join(probs)))
        elif c in have:
            skipped.append((r["url"], "already in catalog"))
        else:
            have.add(c)
            added.append({k: r[k] for k in cl.FIELD_ORDER})

    for u, why in skipped:
        print(f"SKIP {u}: {why}")
    if a.dry_run:
        print(f"[dry-run] would add {len(added)}; catalog would have {len(data) + len(added)}")
        return
    if added:
        cl.write_catalog(a.catalog, data + added)
    print(f"Added {len(added)} records. Catalog now has {len(data) + len(added)}.")


if __name__ == "__main__":
    main()
