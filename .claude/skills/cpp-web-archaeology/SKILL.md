---
name: cpp-web-archaeology
description: Expands and maintains the C/C++ Web Archaeology catalog (paoloanzn.github.io/cpp-web-archaeology), a list of 2000–2010 C, C++ and Lisp material that teaches the reader to build something and is still live. Runs multi-agent research batches, reviews outside agents' catalog pull requests, audits existing entries, and changes the catalog website. Use when asked to expand the catalog, run a research batch, add or remove entries, review a catalog PR, or update the archaeology site.
---

# C/C++ Web Archaeology

## Owner rules (always)

- **Never merge a PR and never push catalog changes to `main` without the owner's explicit
  OK in this conversation.** Open a PR, report, and wait.
- **The bar is the inclusion test** in `cpp-web-archaeology/agents.txt` section 1: the page
  must teach the reader to build something (an assignment, lab or step-by-step build-along).
  Manuals, project pages, own-project blog posts, benchmarks, papers and slides fail it,
  however good they are. The owner rejected 16 of 25 entries in batch 5 for this reason.
- Report to the owner in plain, short English. For every accepted entry, give one line:
  title, what the reader builds, URL. The owner judges from that list.

## Where the rules live

`cpp-web-archaeology/agents.txt` is the single source of truth for the inclusion test,
hard requirements, entry format, scores, scripts and PR description. It is the file the
owner points outside agents (ChatGPT, other sessions) to. Read its sections 1, 2, 5 and 6
before any batch. Do not restate those rules elsewhere; change them there.

## Files

| File | Use |
|---|---|
| `cpp-web-archaeology/agents.txt` | Rules and the step-by-step workflow for any agent. |
| `references/agent-brief.md` | Template brief for research sub-agents. |
| `references/leads.md` | Open leads by domain, and known dead ends. Check before researching. |
| `references/website.md` | How `index.html` works and how to test it. Read before changing the site. |
| `scripts/*.py` | Run them; do not read them unless one fails. Each has `--help`. Usage is in agents.txt section 4. |
| `scripts/ui_smoke.js` | Browser test of the site (setup in `references/website.md`). |

## Workflow A — multi-agent research batch

Copy and tick:

```
- [ ] 1. Sync main, branch, read gaps and leads
- [ ] 2. Plan 6–8 non-overlapping domains
- [ ] 3. Fill the brief, launch all research agents in one message (background)
- [ ] 4. Merge, then review every entry as the owner would
- [ ] 5. Verify live, append, validate (loop until 0 errors), smoke test
- [ ] 6. Update leads.md, commit, push branch, open PR
- [ ] 7. Report the link list and wait for the owner's OK before merging
```

1. **Sync and branch.** `git pull --ff-only origin main`, then
   `git checkout -b catalog/YYYY-MM-DD-<topic>`. Run `catalog_stats.py --urls-out
   $SCRATCH/existing_urls.txt` and `--categories`. Read `leads.md` for the focus area.
2. **Plan domains.** Split the focus into 6–8 domains with no overlap. Always include one
   agent for "leads in `leads.md` for this focus". Name, per domain, which kinds of pages to
   look for (assignments, labs, build-along tutorials) and which entries already exist
   (`grep` the catalog for the topic) so agents look at new schools and sites.
3. **Launch.** Copy `references/agent-brief.md` to the scratchpad, fill every `{{...}}` from
   Python or a quoted heredoc (unquoted heredocs run the backticks), and check
   `grep -c '{{' brief` prints 0. The session's web-search budget (~200 calls) is shared:
   give each agent `200 / number of agents` searches. Launch all agents in one message with
   `run_in_background: true`, `subagent_type: general-purpose`.
4. **Merge and review.** Run `merge_batch.py`. Then list every entry
   (`score | year | title | url`) and decide each one with the three questions of the
   inclusion test. Be stricter than the agents: they over-accept project pages, blog posts
   and manuals. Re-run with `--drop` until only real assignments and build-alongs remain.
   Re-open 5+ pages to confirm the quoted date proof.
5. **Verify and append.** Run `check_urls.py --fix`; check curl failures with WebFetch;
   drop pages that are really gone. Run `append_catalog.py`, then `validate_catalog.py`;
   fix and repeat until it prints 0 errors. Read the "matching NO intent tile" list. Run
   `ui_smoke.js` and look at one screenshot.
6. **Commit and PR.** Commit `projects.json` and `leads.md` (plus site files only if
   Workflow D was needed). Push the branch. Open the PR with the agents.txt section 8
   description through the GitHub REST API (`gh api repos/OWNER/REPO/pulls -f ...`;
   GraphQL is blocked in this environment).
7. **Report and wait.** Send the owner the PR link and the one-line-per-entry list. Merge
   only after the owner says so (`gh api -X PUT repos/OWNER/REPO/pulls/N/merge`).

## Workflow B — review an outside agent's PR

1. Read it: `gh api repos/OWNER/REPO/pulls/N` (body) and `.../pulls/N/files` (diff).
2. Check it touches only `projects.json` and `leads.md`.
3. For each added entry, open the page and apply the inclusion test and agents.txt
   section 2. Spot-check every date quote.
4. Tell the owner which entries pass and which fail, with one reason each. Do not merge or
   push to the PR branch unless the owner asks you to take it over.

## Workflow C — audit existing entries

Split the catalog into chunks of ~70, give each chunk to a sub-agent with the inclusion
test and the owner's calibration examples (agents.txt section 1), and ask for one verdict
per entry: keep / remove / unsure, type, confidence, one-line reason. Merge the verdicts
into a list for the owner. Remove nothing until the owner approves the list.

## Workflow D — website changes

Read `references/website.md` first. Keep the dig-site design, the "What do you want to
build?" tiles, the sticky search and visible filters. The page must stay one
self-contained file that fetches `./data/projects.json`. Run `ui_smoke.js`, look at the
screenshots, and update `website.md` in the same commit.

## Environment notes

- Outbound traffic goes through a proxy. Some hosts reset curl but load in WebFetch
  (gnu.org, people.cs.vt.edu, intel.com, grinnell.edu); some send incomplete TLS chains
  (web.eecs.umich.edu). Never disable TLS verification.
- `gh` GraphQL commands (`gh pr list`, `gh pr view`) fail here; use `gh api` REST routes.
  Draft/ready: `POST /repos/OWNER/REPO/pulls/N/ccr/ready_for_review`.
- Sub-agents cannot see this conversation. Everything they need goes in the brief.
