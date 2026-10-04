#!/usr/bin/env python3
"""Check that every record URL loads live right now (HTTP 200 after redirects).

Input: a JSON list of records (e.g. merged.json) or a text file with one URL per line.
If an http:// URL fails but its https:// twin returns 200 (or the reverse), --fix rewrites
the URL in the JSON file in place.

Usage:
  python3 check_urls.py merged.json [--fix] [--workers 12]
Exit code 1 if any URL is still not 200.
"""
import argparse
import concurrent.futures as cf
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import catalog_lib as cl  # noqa: E402


def twin(url):
    if url.startswith("http://"):
        return "https://" + url[7:]
    if url.startswith("https://"):
        return "http://" + url[8:]
    return None


def check(url):
    code = cl.http_status(url)
    if code == 200:
        return url, code, None
    t = twin(url)
    if t and cl.http_status(t) == 200:
        return url, code, t
    if code in (0, 429, 500, 502, 503, 504):  # flaky old servers: one retry
        code = cl.http_status(url, timeout=60)
    return url, code, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--fix", action="store_true")
    ap.add_argument("--workers", type=int, default=12)
    a = ap.parse_args()

    is_json = a.path.endswith(".json")
    if is_json:
        recs = cl.load_json(a.path)
        urls = [r["url"] for r in recs]
    else:
        urls = [l.strip() for l in open(a.path, encoding="utf-8") if l.strip()]

    bad, fixes = [], {}
    with cf.ThreadPoolExecutor(a.workers) as ex:
        for url, code, alt in ex.map(check, urls):
            if code == 200:
                continue
            if alt:
                fixes[url] = alt
                print(f"FIXABLE {code} {url} -> {alt} (200)")
            else:
                bad.append((url, code))
                print(f"FAIL    {code} {url}")

    if fixes and a.fix and is_json:
        for r in recs:
            if r["url"] in fixes:
                r["url"] = fixes[r["url"]]
        with open(a.path, "w", encoding="utf-8") as fh:
            json.dump(recs, fh, ensure_ascii=False, indent=2)
        print(f"Rewrote {len(fixes)} URL(s) in {a.path}")
    elif fixes:
        bad.extend((u, "fixable") for u in fixes)

    ok = len(urls) - len(bad)
    print(f"\n{ok}/{len(urls)} URLs load live (HTTP 200).")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
