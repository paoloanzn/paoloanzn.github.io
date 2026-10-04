---
name: cpp-web-archaeology
description: Expand and maintain the C/C++ Web Archaeology catalog (paoloanzn.github.io/cpp-web-archaeology) — find period-authentic 2000–2010 C/C++ projects, course assignments and tutorials still live on the web, verify them, append them to projects.json, keep the website working, and commit to main. Use for "expand the catalog", "run a research batch", "add more entries", "update the archaeology site", or any change to cpp-web-archaeology/.
---

# C/C++ Web Archaeology

A curated, link-first catalog of C and C++ programming material from about **2000–2010**
that is **still live on its original site today**: OS kernels, compilers, databases,
network stacks, emulators, drivers and more. Quality beats quantity: one genuinely
period-authentic page is worth more than ten weak search hits.

- Data: `cpp-web-archaeology/data/projects.json` (a JSON list; the site reads it directly)
- Site: `cpp-web-archaeology/index.html` → https://paoloanzn.github.io/cpp-web-archaeology/
- Repo: `paoloanzn/paoloanzn.github.io`, branch `main` (pushing deploys the site)

## Files in this skill

| File | Use it for |
|---|---|
| `references/research-spec.md` | **The rules.** Period evidence, live-web rule, search methods, scoring, schema. Read it before any research. |
| `references/agent-brief.md` | Template brief for research subagents. Fill it in and copy to the scratchpad. |
| `references/leads.md` | Unfinished leads and known dead ends from earlier batches. Start here. |
| `references/website.md` | How the page works, where things live in `index.html`, how to test it. |
| `scripts/catalog_stats.py` | Gaps by area/year, over-used sites, intent-tile coverage; writes the existing-URL list. |
| `scripts/merge_batch.py` | Merge agent outputs: schema check, de-dupe vs catalog and within batch, collect leads. |
| `scripts/check_urls.py` | Confirm every URL returns 200 now; `--fix` swaps http/https when only the twin works. |
| `scripts/append_catalog.py` | Append new records to the end of `projects.json` without touching existing ones. |
| `scripts/validate_catalog.py` | Final gate on the whole catalog before committing. |
| `scripts/ui_smoke.js` | Playwright smoke test of the website with screenshots. |

All Python scripts are standard library only and find the repo from their own location,
so they work from any directory. Every script has `--help`.

## Set these first (every workflow)

```bash
REPO=$(git -C /path/to/clone rev-parse --show-toplevel)     # the paoloanzn.github.io clone
SKILL=$REPO/.claude/skills/cpp-web-archaeology
SCRATCH=<the scratchpad directory from your system prompt>   # never inside the repo
mkdir -p "$SCRATCH/batch"
git -C "$REPO" pull --ff-only origin main
```

Shell variables do not persist between Bash calls in most harnesses. Repeat these lines at the top of
each command, or write absolute paths. Paths you give to subagents must be **absolute**.

## Workflow A — research batch (expand the catalog)

Make a task list with these steps. The user is often away; keep going without asking unless something is irreversible.

1. **Sync and snapshot.**
   ```bash
   git -C "$REPO" pull --ff-only origin main
   python3 "$SKILL/scripts/catalog_stats.py" --urls-out "$SCRATCH/existing_urls.txt"
   python3 "$SKILL/scripts/catalog_stats.py" --categories     # for {{CATEGORY_LIST}}
   ```
   A weekly GitHub Action (`tools/cpp-web-archaeology/collector.py`) can also rewrite and re-sort
   `projects.json` (records with `"provenance": "automated-harvest"`). Always pull first.

2. **Pick domains from the gaps.** Read the stats (smallest areas first) and `references/leads.md`.
   Underrepresented areas get priority; graphics/Win32 only when unusually strong (see spec).
   Split the work into 4–8 non-overlapping domains. Good splits used before:
   OS kernels · filesystems/concurrency/memory · compilers · interpreters/VMs/assemblers/simulators/emulators ·
   networking/distributed · database internals · Unix tools/compression/drivers/embedded · hobbyist & community sites.
   Rotate in fresh angles too: garbage collectors, linkers/loaders, audio/DSP, text editors, version control internals,
   regex engines, game-engine internals, security/crypto course projects, parallel/MPI/OpenMP, GPU-era (2007–2010) CUDA.

3. **Fan out research subagents in parallel** (one Agent call per domain, all in the same message,
   `subagent_type: general-purpose`). Before that:
   - Copy `references/agent-brief.md` to `$SCRATCH/AGENT_BRIEF.md` and fill in every `{{...}}`:
     `{{SKILL_DIR}}` = absolute `$SKILL`, `{{EXISTING_URLS_FILE}}` = absolute `$SCRATCH/existing_urls.txt`,
     `{{TARGET}}` = 8–15, `{{CATEGORY_LIST}}` = output of `catalog_stats.py --categories`.
     Then `grep -n '{{' "$SCRATCH/AGENT_BRIEF.md"` must print nothing.
   - Each prompt: "Read and follow $SCRATCH/AGENT_BRIEF.md. Assigned domain: … Already covered (skip): …
     courses/sites from the catalog in that domain. Output file: $SCRATCH/batch/<nn>_<domain>.json".
   - Name the already-covered course offerings in each prompt so agents look at **other schools and semesters**.
   - Agents must not touch the repo. Only you commit.

4. **Merge and review.**
   ```bash
   python3 "$SKILL/scripts/merge_batch.py" --batch-dir "$SCRATCH/batch" --out "$SCRATCH/merged.json" --report "$SCRATCH/report.json"
   python3 -c "import json;[print(r['score'],r['year'],r['site'],'|',r['title'][:70]) for r in sorted(json.load(open('$SCRATCH/merged.json')),key=lambda r:r['site'])]"
   ```
   Then read the merged list yourself (title, year, score, site, URL per line). Drop with `--drop URL ...` and re-run when:
   - the evidence is weak (copyright footer only, "rebuilt" sites, no date on page),
   - it is a near-duplicate (third sibling semester of the same course, same article on two hosts),
   - the score is 85–88 and the scope is small.
   Spot-check 4–6 records for their key evidence string, e.g.
   `curl -sSL URL | grep -o -i -m3 -E 'due[^<]{0,30}|(fall|spring|winter) 20[01][0-9]|\.dsw|gcc[ -]?[23]\.[0-9]'`.
   Finish **all** `--drop` re-runs before step 5: re-running the merge regenerates `merged.json` and
   loses the URL fixes from step 5.

5. **Verify live.**
   ```bash
   python3 "$SKILL/scripts/check_urls.py" "$SCRATCH/merged.json" --fix
   ```
   Any URL still failing: retry once later; if still failing, drop it and list it in leads.

6. **Append, validate, test.**
   ```bash
   python3 "$SKILL/scripts/append_catalog.py" "$SCRATCH/merged.json"
   python3 "$SKILL/scripts/validate_catalog.py"     # must exit 0
   python3 "$SKILL/scripts/catalog_stats.py"        # check "Records matching NO intent tile"
   ```
   If new records match no intent tile, improve their tags/notes, or extend the site (Workflow B).
   Run the UI smoke test (see `references/website.md`).

7. **Update leads.** Remove leads that were added or proved dead. Add the new leads from `report.json`
   (`leads`; already filtered against the catalog and the current `leads.md`) and notable dead ends to
   `references/leads.md`, grouped by domain. Optionally check them first:
   `python3 -c "import json;print('\n'.join(l['url'] for l in json.load(open('$SCRATCH/report.json'))['leads']))" > "$SCRATCH/leads.txt" && python3 "$SKILL/scripts/check_urls.py" "$SCRATCH/leads.txt"`.

8. **Commit and push to `main`.** Only `projects.json`, `references/leads.md` and (if step 6 needed it)
   `cpp-web-archaeology/index.html` should change. Check with `git -C "$REPO" status --short`.
   ```bash
   cd "$REPO"
   git add cpp-web-archaeology/data/projects.json .claude/skills/cpp-web-archaeology/references/leads.md
   git commit -m "Add N manually curated <areas> archive entries"   # plus the session's attribution lines
   git fetch origin main && git rebase origin/main && git push origin HEAD:main
   ```
   If the rebase stops on a `projects.json` conflict (the weekly collector pushed meanwhile), keep the
   remote file and re-append your records. During a rebase **"ours" is origin/main**:
   ```bash
   git checkout --ours cpp-web-archaeology/data/projects.json
   python3 "$SKILL/scripts/append_catalog.py" "$SCRATCH/merged.json"
   python3 "$SKILL/scripts/validate_catalog.py"
   git add cpp-web-archaeology/data/projects.json && GIT_EDITOR=true git rebase --continue
   git push origin HEAD:main
   ```

9. **Report** (the spec requires it): entries investigated, accepted, rejected; domains covered;
   strongest finds; new catalog size; commit SHA; interesting rejected/borderline sources for next time.

## Workflow B — website changes

1. Read `references/website.md` and the relevant part of `index.html`.
2. Keep the concept: dig-site metaphor, intent tiles first, sticky search, visible removable filters,
   shareable URL state, dark mode, phone layout, reduced motion. Bold and playful, never generic.
3. The page must stay one self-contained file that fetches `./data/projects.json`. No build step, no framework.
4. Run `scripts/ui_smoke.js` (setup in `references/website.md`), then **look at the screenshots**
   with the Read tool. Fix anything that looks off and re-run.
5. Commit only `cpp-web-archaeology/index.html` (and docs if you changed behavior), push to `main`,
   wait ~2 minutes, confirm the live page with the curl checks in `references/website.md`.
6. If the change alters how the page works, update `references/website.md` in the same commit.

## Record schema (summary — full rules in the spec)

```json
{
  "title": "Cornell CS414 — User-level threads and semaphores",
  "url": "https://www.cs.cornell.edu/courses/cs414/2003su/projects/project1/project1.html",
  "year": 2003, "year_label": "June 2003",
  "language": ["C"], "category": "Operating Systems / Concurrency",
  "kind": "project assignment", "site": "cs.cornell.edu", "score": 99,
  "evidence": ["Original 2003 assignment", "C source skeleton", "Windows NT Minithreads environment"],
  "tags": ["threads", "semaphores", "scheduler", "Minithreads"],
  "notes": "Build a non-preemptive user-level thread package with queues, TCBs, a scheduler and semaphores."
}
```

Score: 98–100 museum grade · 95–97 prime · 90–94 solid · 85–89 borderline (add sparingly) · below 85 never.

## Hard rules

- The catalog URL must load live **now**, on the original or long-running domain. Never web.archive.org.
- The material itself must be from 2000–2010, proven by evidence **on the page** (dates, semester paths, period toolchains).
- C or C++ must be what the reader writes. Courses where students use Java/ML/Python are out.
- No GitHub/GitLab-only sources, Medium, Dev.to, modern reposts or retrospectives.
- Never rewrite or reorder existing records. Append only. De-duplicate by canonical URL.
- Do not modify unrelated files in the repo (it is also Paolo's personal Jekyll blog).
- When in doubt, reject. A borderline page goes to `leads.md`, not the catalog.

## Lessons from earlier batches

- Following directories beats searching. CMU, Princeton, Cornell, Wisconsin, UChicago, UT Austin, MIT PDOS,
  Stanford SCS and USF (Cruse) keep whole year-coded trees live.
- The web-search budget (about 200 calls) is shared by the WHOLE session, not per agent. In batch 2 the
  first agents used it up and later agents could not search. Give each agent a search allowance
  (about 200 ÷ number of agents) in its prompt, and give the leads agent none (it only needs curl).
- One agent dedicated to `leads.md` is high-yield: in batch 2 it resolved all 71 leads and added 20 records.
- When filling the brief, drop the template's header (everything above the first `---`) and write the
  file from Python or a quoted heredoc (`<<'EOF'`): an unquoted heredoc runs the backticks in the brief.
- WebFetch may need permission and time out in subagents; `curl` from Bash works for most hosts.
- Some old servers reset connections or return 503 on http but 200 on https (`check_urls.py --fix` handles it).
- Hosts often blocked: UMD `/class/`, UNSW, UW and Berkeley inst (logins). See `leads.md`.
- Agents tend to over-deliver near-duplicates (many sibling semesters). Cap at two per course unless content differs.
