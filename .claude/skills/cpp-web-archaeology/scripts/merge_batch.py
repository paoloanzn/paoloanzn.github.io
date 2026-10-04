#!/usr/bin/env python3
"""Merge research-agent batch files into one list of NEW, valid records.

Each batch file looks like:
  {"accepted": [record, ...], "rejected": [{"url","reason"}], "borderline_leads": [{"url","note"}],
   "investigated_count": N}

What this does:
  * validates every accepted record against the schema rules (catalog_lib.validate_record)
  * drops records whose canonical URL is already in the catalog or already seen in the batch
  * keeps only the schema fields, in a fixed order
  * writes merged records + a report (counts, drops, leads) for the final summary

Usage:
  python3 merge_batch.py --batch-dir DIR --out merged.json [--report report.json] [--drop URL ...]
"""
import argparse
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import catalog_lib as cl  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch-dir", required=True)
    ap.add_argument("--catalog", default=cl.CATALOG)
    ap.add_argument("--out", required=True)
    ap.add_argument("--report")
    ap.add_argument("--drop", nargs="*", default=[], help="URLs to exclude after manual review")
    a = ap.parse_args()

    existing = {cl.canon(r["url"]) for r in cl.load_json(a.catalog)}
    drops = {cl.canon(u) for u in a.drop}
    seen, merged, lead_seen = {}, [], set()
    leads_md = os.path.join(os.path.dirname(__file__), "..", "references", "leads.md")
    try:
        import re as _re
        known_leads = {cl.canon(u) for u in _re.findall(r"https?://\S+", open(leads_md, encoding="utf-8").read())}
    except OSError:
        known_leads = set()
    rep = {"files": [], "investigated": 0, "agent_rejected": 0, "accepted": 0,
           "dropped": [], "leads": []}

    files = sorted(glob.glob(os.path.join(a.batch_dir, "*.json")))
    if not files:
        sys.exit(f"No batch files in {a.batch_dir}")
    for f in files:
        name = os.path.basename(f)
        try:
            d = cl.load_json(f)
        except Exception as e:  # noqa: BLE001
            rep["dropped"].append({"file": name, "reason": f"invalid JSON: {e}"})
            continue
        if not isinstance(d, dict):
            rep["dropped"].append({"file": name, "reason": "batch file must be a JSON object with 'accepted'"})
            continue
        rep["files"].append(name)
        rep["investigated"] += int(d.get("investigated_count") or 0)
        rep["agent_rejected"] += len(d.get("rejected") or [])
        for l in d.get("borderline_leads") or []:
            lc = cl.canon(l.get("url") if isinstance(l, dict) else "")
            if lc and lc not in existing and lc not in lead_seen and lc not in known_leads:
                lead_seen.add(lc)
                rep["leads"].append({**l, "file": name})
        for r in d.get("accepted") or []:
            url = r.get("url", "") if isinstance(r, dict) else ""
            c = cl.canon(url)
            why = None
            if not isinstance(r, dict) or not c:
                why = "record is not an object or has no valid url"
            elif c in drops:
                why = "dropped on manual review"
            elif c in existing:
                why = "already in catalog"
            elif c in seen:
                why = f"duplicate of record from {seen[c]}"
            else:
                probs = cl.validate_record(r, strict=True)
                if probs:
                    why = "; ".join(probs)
            if why:
                rep["dropped"].append({"file": name, "url": url, "reason": why})
                continue
            seen[c] = name
            merged.append({k: r[k] for k in cl.FIELD_ORDER})

    rep["accepted"] = len(merged)
    with open(a.out, "w", encoding="utf-8") as fh:
        json.dump(merged, fh, ensure_ascii=False, indent=2)
    if a.report:
        with open(a.report, "w", encoding="utf-8") as fh:
            json.dump(rep, fh, ensure_ascii=False, indent=2)

    print(f"Batch files: {len(rep['files'])}   investigated: {rep['investigated']}   "
          f"rejected by agents: {rep['agent_rejected']}")
    print(f"Merged new records: {len(merged)}  ->  {a.out}")
    print(f"Dropped at merge: {len(rep['dropped'])}")
    for d in rep["dropped"]:
        print(f"  - {d.get('url', d.get('file'))}: {d['reason']}")
    print(f"New leads (not in catalog or leads.md): {len(rep['leads'])}")


if __name__ == "__main__":
    main()
