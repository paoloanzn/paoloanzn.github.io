# Website guide: cpp-web-archaeology/index.html

The public page is one self-contained file: `cpp-web-archaeology/index.html`.
It fetches `./data/projects.json` at load time, so **adding records needs no HTML change**.
Live URL: https://paoloanzn.github.io/cpp-web-archaeology/ (GitHub Pages, deployed by
`.github/workflows/jekyll-gh-pages.yml` on every push to `main`, usually within 1–3 minutes).

## Design concept (keep it)

"Dig site". Each year 2000–2010 is a colored soil layer, every record is a "find".
Bold, playful, warm. The user's intent comes first:

1. **"What do you want to build?"** intent tiles are the first question, with live counts.
2. **The year column** (hero, right side) is both a histogram and a year filter. Click a layer = only that year.
3. **Sticky `grep -i` search bar**: multi-word AND search over title, site, category, kind, notes, tags, evidence, year. Matches are highlighted.
4. **Filter pills** with × show every active filter. "Clear all" appears with 2+ filters. The empty state offers one button per filter to remove.
5. **Results** grouped by year layer (default) or flat by sort. Cards = specimen labels: score stamp, tags (click = search for tag), "Why it's authentic" evidence toggle, "Open original ↗".
6. **Random dig** (button or `R`) opens a random find from the current filters.
7. Keys: `/` search, `R` random dig, `Esc` clear search / close. All state is in the URL (`?q=&intent=&year=&lang=&cat=&sort=`) so views can be shared.

Fonts: Bricolage Grotesque (display/body) and Martian Mono (labels) from Google Fonts.
Colors are CSS variables on `:root`, redefined for dark mode under `prefers-color-scheme: dark`.

## Where things live in the file

| What | Where (search for) |
|---|---|
| Color tokens, light + dark | `:root{` and `@media (prefers-color-scheme:dark)` |
| Year layer colors | `var LAYERS={2010:[...` — `[background, text color]` per year |
| Intent tiles | `var INTENTS=[` — `{id, label, tok, re}` |
| Search fields | `x._all=` in the load block |
| Intent match fields | `x._hay=` (title + category + notes + tags) |
| Card markup | `function card(x,i)` |
| Score grades | `function grade(s)` — 98+ Museum grade, 95+ Prime find, 90+ Solid find, else Rough find |
| URL state | `syncUrl` / `readUrl` |
| Method section text | `<section class="method"` |

## Common maintenance tasks

**New records don't show under any intent tile.**
Run `scripts/catalog_stats.py`. It lists records that match no tile.
Fix the record first (better tags/notes with the words readers use). If a whole new area is
growing (e.g. 5+ "Audio / DSP" records), add a tile or widen a regex in `INTENTS`.
Keep `catalog_lib.intent_haystack()` in sync with `x._hay` if you change which fields are matched.
The intent regex must stay on one line in the form `{id:"x",label:"...",tok:"...",re:/.../}`
so `catalog_lib.load_intents()` can parse it.

**Records outside 2000–2010.** The layer column only draws `LAYERS` years. If the catalog
ever accepts 1999 or 2011, add a color for that year to `LAYERS` and update the hero copy.

**New top-level category.** Nothing to do; the category dropdown is built from the data.

**Changing copy or layout.** Keep the intent tiles above the results, keep search sticky,
keep every filter visible and removable. Test at 390px wide. Respect `prefers-reduced-motion`.

## Testing

Always run the smoke test after any change to `index.html` (and it is cheap to run after
catalog changes too):

```bash
SCRATCH=<your scratchpad dir>
cd "$SCRATCH" && npm i playwright@1 >/dev/null 2>&1   # once per session
node "$SKILL/scripts/ui_smoke.js" --out "$SCRATCH/shots"
```

It serves the folder locally, checks the core flows on desktop, dark mode and phone,
and writes screenshots. Open the screenshots with the Read tool and look at them.
After pushing, confirm the live page:

```bash
curl -s https://paoloanzn.github.io/cpp-web-archaeology/ | grep -c "What do you want to build"
curl -s https://paoloanzn.github.io/cpp-web-archaeology/data/projects.json | python3 -c "import json,sys;print(len(json.load(sys.stdin)))"
```
