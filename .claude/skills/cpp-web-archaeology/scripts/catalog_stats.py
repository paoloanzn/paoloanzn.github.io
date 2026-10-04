#!/usr/bin/env python3
"""Snapshot of the catalog: size, gaps, intent coverage, and the list of
existing URLs that research agents must not re-add.

Usage:
  python3 catalog_stats.py                      # human report
  python3 catalog_stats.py --urls-out FILE      # also write existing URLs, one per line
  python3 catalog_stats.py --json               # machine-readable summary
"""
import argparse
import signal
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import catalog_lib as cl  # noqa: E402


def main():
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # quiet when piped to head
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", default=cl.CATALOG)
    ap.add_argument("--urls-out")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--categories", action="store_true",
                    help="print the full category list, comma separated (for the agent brief)")
    a = ap.parse_args()

    data = cl.load_json(a.catalog)
    cats = collections.Counter(r.get("category", "?") for r in data)
    tops = collections.Counter(r.get("category", "?").split(" / ")[0] for r in data)
    years = collections.Counter(r.get("year") for r in data)
    sites = collections.Counter(r.get("site", "?") for r in data)
    auto = sum(1 for r in data if r.get("provenance") == "automated-harvest")

    intents = cl.load_intents()
    icount = {i[0]: 0 for i in intents}
    unmatched = []
    for r in data:
        hay = cl.intent_haystack(r)
        hit = False
        for iid, _, rx in intents:
            if rx.search(hay):
                icount[iid] += 1
                hit = True
        if not hit:
            unmatched.append(r)

    if a.categories:
        print(", ".join(sorted(cats)))
        return

    if a.urls_out:
        with open(a.urls_out, "w", encoding="utf-8") as f:
            f.write("\n".join(r["url"] for r in data) + "\n")

    if a.json:
        print(json.dumps({"total": len(data), "categories": cats, "top_level": tops,
                          "years": {str(k): v for k, v in sorted(years.items(), key=lambda x: str(x[0]))},
                          "sites": len(sites), "automated": auto, "intents": icount,
                          "unmatched_intent": [r["url"] for r in unmatched]}, indent=2))
        return

    print(f"Catalog: {a.catalog}")
    print(f"Records: {len(data)}   distinct sites: {len(sites)}   categories: {len(cats)}   automated-harvest: {auto}")
    print("\nBy top-level area (smallest first = biggest gaps):")
    for k, v in sorted(tops.items(), key=lambda x: (x[1], x[0])):
        print(f"  {v:4d}  {k}")
    print("\nBy year:")
    for y in sorted(years, key=lambda x: str(x)):
        print(f"  {y}: {'#' * years[y]} {years[y]}")
    print("\nMost-used sites (avoid over-representing these):")
    for s, n in sites.most_common(12):
        print(f"  {n:3d}  {s}")
    if intents:
        print("\nWebsite intent tiles (records per tile):")
        for iid, label, _ in intents:
            print(f"  {icount[iid]:4d}  {label} [{iid}]")
        print(f"\nRecords matching NO intent tile: {len(unmatched)}")
        for r in unmatched[:25]:
            print(f"  - [{r.get('category')}] {r.get('title')}")
        if unmatched:
            print("  -> add tags/notes wording, or extend an intent regex in index.html (see references/website.md)")
    if a.urls_out:
        print(f"\nWrote {len(data)} existing URLs to {a.urls_out}")


if __name__ == "__main__":
    main()
