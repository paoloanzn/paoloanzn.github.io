"""Shared helpers for the C/C++ Web Archaeology skill scripts.

Standard library only. Import from sibling scripts with:
    sys.path.insert(0, os.path.dirname(__file__)); import catalog_lib as cl
"""
import json
import os
import re
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
CATALOG = os.path.join(REPO_ROOT, "cpp-web-archaeology", "data", "projects.json")
INDEX_HTML = os.path.join(REPO_ROOT, "cpp-web-archaeology", "index.html")

REQUIRED = ["title", "url", "year", "year_label", "language", "category",
            "kind", "site", "score", "evidence", "tags", "notes"]
FIELD_ORDER = REQUIRED  # order used when writing new records

YEAR_MIN, YEAR_MAX = 2000, 2010
SCORE_MIN = 85

KINDS = {"project assignment", "project sequence", "course project sequence", "lab assignment",
         "lab sequence", "tutorial", "tutorial series", "project tutorial", "source-code project",
         "source project", "course archive", "tutorial archive", "technical article"}

# Hosts that must never be the primary catalog URL.
BANNED_HOST_PATTERNS = [
    r"(^|\.)web\.archive\.org$", r"(^|\.)archive\.(org|is|ph|today)$",
    r"(^|\.)github\.com$", r"(^|\.)githubusercontent\.com$", r"(^|\.)gitlab\.com$",
    r"(^|\.)medium\.com$", r"(^|\.)dev\.to$", r"(^|\.)hashnode\.(com|dev)$",
]


def canon(url):
    """Canonical form used for de-duplication: no scheme, no www., no fragment,
    no trailing slash, lower-case."""
    u = (url if isinstance(url, str) else "").strip().split("#")[0]
    u = re.sub(r"^[a-z]+://", "", u, flags=re.I)
    u = re.sub(r"^www\.", "", u, flags=re.I)
    return u.rstrip("/").lower()


def host(url):
    m = re.match(r"^[a-z]+://([^/:?#]+)", (url if isinstance(url, str) else "").strip(), flags=re.I)
    return (m.group(1) if m else "").lower()


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def write_catalog(path, records):
    """Write the catalog the same way the site's collector does: indent=2,
    UTF-8 kept as-is, trailing newline."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(json.dumps(records, ensure_ascii=False, indent=2) + "\n")


def validate_record(r, strict=True):
    """Return a list of problems for one record (empty list = OK).
    strict=True applies the rules for NEW manual records."""
    if not isinstance(r, dict):
        return ["record must be a JSON object"]
    p = []
    for k in REQUIRED:
        if k not in r:
            p.append(f"missing field '{k}'")
    if p:
        return p
    for k in ("title", "url", "year_label", "category", "kind", "site", "notes"):
        if not isinstance(r[k], str):
            p.append(f"{k} must be a string")
    if p:
        return p
    if not isinstance(r["title"], str) or len(r["title"].strip()) < 8:
        p.append("title too short")
    if not re.match(r"^https?://", r["url"]):
        p.append("url must start with http(s)://")
    if "#" in r["url"]:
        p.append("url has a #fragment")
    h = host(r["url"])
    for pat in BANNED_HOST_PATTERNS:
        if re.search(pat, h):
            p.append(f"banned host {h}")
            break
    if isinstance(r["year"], bool) or not isinstance(r["year"], int):
        p.append("year must be an integer")
    elif strict and not (YEAR_MIN <= r["year"] <= YEAR_MAX):
        p.append(f"year {r['year']} outside {YEAR_MIN}-{YEAR_MAX}")
    if isinstance(r["score"], bool) or not isinstance(r["score"], (int, float)):
        p.append("score must be a number")
    elif strict and not (SCORE_MIN <= r["score"] <= 100):
        p.append(f"score {r['score']} outside {SCORE_MIN}-100")
    if not isinstance(r["language"], list) or not r["language"]:
        p.append("language must be a non-empty list")
    elif strict and not any(l in ("C", "C++") for l in r["language"]):
        p.append("language must include 'C' or 'C++'")
    for k in ("evidence", "tags"):
        if not isinstance(r[k], list) or not all(isinstance(x, str) and x.strip() for x in r[k]):
            p.append(f"{k} must be a list of strings")
    if strict and isinstance(r["evidence"], list) and not (3 <= len(r["evidence"]) <= 6):
        p.append("evidence should have 3-6 items")
    if strict and isinstance(r["tags"], list) and not r["tags"]:
        p.append("tags must not be empty")
    if strict and len(str(r["notes"]).strip()) < 25:
        p.append("notes too short (say what the reader builds)")
    if strict and r["site"].startswith("www."):
        p.append("site should drop the leading 'www.'")
    elif strict and h and not (h == r["site"] or h.endswith("." + r["site"]) or h == "www." + r["site"]):
        p.append(f"site '{r['site']}' does not match url host '{h}'")
    if strict and r["kind"] not in KINDS:
        p.append(f"kind '{r['kind']}' not one of: {', '.join(sorted(KINDS))}")
    return p


def load_intents(index_html=INDEX_HTML):
    """Extract the website's 'What do you want to build?' intents
    (id, label, compiled regex) from index.html so coverage can be checked."""
    try:
        src = open(index_html, encoding="utf-8").read()
    except OSError:
        return []
    out = []
    for m in re.finditer(r'\{id:"(\w+)",label:"([^"]+)",tok:"[^"]*",re:/(.+?)/\}', src):
        pat = m.group(3).replace("\\/", "/")
        try:
            out.append((m.group(1), m.group(2), re.compile(pat)))
        except re.error:
            pass
    return out


def intent_haystack(r):
    """Must mirror x._hay in index.html."""
    return " ".join([r.get("title", ""), r.get("category", ""), r.get("notes", "")] +
                    list(r.get("tags") or [])).lower()


def http_status(url, timeout=40):
    """Return final HTTP status for url via curl (honours the sandbox proxy)."""
    try:
        out = subprocess.run(
            ["curl", "-sSL", "-A", "Mozilla/5.0 (compatible; cpp-web-archaeology-check)",
             "-o", "/dev/null", "-m", str(timeout), "-w", "%{http_code}", url],
            capture_output=True, text=True, timeout=timeout + 10)
        return int(out.stdout.strip() or 0)
    except Exception:
        return 0
