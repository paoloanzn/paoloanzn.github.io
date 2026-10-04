# Research agent brief (template)

Copy this file to the scratchpad, fill in the `{{...}}` parts, and give each research
subagent a short prompt that points to the copy plus its own domain and output path.
Subagents cannot see your conversation, so everything they need must be in here.

---

You are a research agent for the **C/C++ Web Archaeology** catalog.

**Read first, and follow exactly:** `{{SKILL_DIR}}/references/research-spec.md`
(the authoritative research criteria: period evidence, live-web rule, scoring, schema).

**Existing catalog URLs (never re-add these or near-duplicates of the same page):**
`{{EXISTING_URLS_FILE}}`

**Leads from earlier batches (check these first if they are in your domain):**
`{{SKILL_DIR}}/references/leads.md`

## Your job
- Research ONLY your assigned domain (given in your prompt). Other agents cover other domains in parallel.
- Tools you need: WebSearch, Bash (curl) and, if allowed, WebFetch. If WebFetch is denied or times out,
  use curl for everything; do not stop.
- Find candidates with WebSearch, then load EVERY candidate URL to confirm it is live today and to read it.
  Use WebFetch, or `curl -sSL -o /dev/null -w '%{http_code}' URL` from Bash. Some hosts block one or the other.
  Save tokens on PDFs by grepping them: `curl -sSL URL | pdftotext - - | head -80` (if pdftotext exists).
- **Follow directories.** When a page is strong, open its course index, sibling projects, sibling
  semesters and the instructor's other course archives. One good page often leads to ten.
- Never use web.archive.org as the catalog URL. Reject GitHub/GitLab-only, Medium, Dev.to and modern reposts.
- Every accepted record needs concrete period evidence seen ON THE PAGE (a date, a semester in the URL,
  a period toolchain such as gcc 3.x, Fedora Core, VC6 `.dsw`, CVS, Bochs or Solaris machines).
- C or C++ must be the language students or readers write. Check it.
- Quality over quantity. Target about {{TARGET}} accepted records, score 85 or higher only.
- Avoid adding more than 2 sibling semesters of the same course. Pick the strongest.
- Web search has a budget. Spend it on discovery, then switch to following directories on hosts you found.
- Do NOT edit, commit or push anything in the git repository. Only write your output file.

## Output
Write valid JSON to the path given in your prompt:

```json
{
  "accepted": [ { "title": "...", "url": "...", "year": 2004, "year_label": "Fall 2004",
                  "language": ["C"], "category": "...", "kind": "project assignment",
                  "site": "cs.example.edu", "score": 95,
                  "evidence": ["...", "...", "..."], "tags": ["...", "..."],
                  "notes": "..." } ],
  "rejected": [ { "url": "...", "reason": "short reason" } ],
  "borderline_leads": [ { "url": "...", "note": "why it is worth a later look" } ],
  "investigated_count": 0
}
```

Record rules:
- `url`: the exact live URL you loaded. https if it works over https. No tracking params, no `#fragment`.
- `title`: "Institution COURSE — What you build" or "Author — Article title". Put the term in the title when it helps tell semesters apart.
- `year`: integer 2000–2010. `year_label`: the most precise date the page shows ("Due 4 Nov 2003", "Spring 2005").
- `site`: host without "www." (e.g. "cs.cornell.edu").
- `category`: reuse one of the current categories when it fits:
  {{CATEGORY_LIST}}
  A new category is fine only if it will hold several records.
- `kind`: exactly one of: project assignment, project sequence, course project sequence, lab assignment, lab sequence,
  tutorial, tutorial series, project tutorial, source-code project, source project, course archive, tutorial archive,
  technical article.
- `site`: must be the URL's host without "www." (the merge script rejects a mismatch).
- `evidence`: 3–6 short strings, each a concrete fact you saw on the page.
- `tags`: 3–7 lower-noise keywords readers would search for (system names, techniques, toolchains).
  Include the words a reader would use for the project type (e.g. "kernel", "compiler", "filesystem",
  "sockets", "B+ tree") — the website's "What do you want to build?" tiles match on title, category, notes and tags.
- `notes`: one or two plain sentences saying what the reader builds.
- Validate before finishing: `python3 -m json.tool <file> >/dev/null && echo ok`.

Your final message: counts (investigated / accepted / rejected / leads) and your 3 strongest finds. Keep it short.
