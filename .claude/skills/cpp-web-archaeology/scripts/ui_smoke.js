#!/usr/bin/env node
/*
 * Browser smoke test for cpp-web-archaeology/index.html.
 *
 * Serves the site folder on a local port, loads it in Chromium (desktop light,
 * desktop dark, phone), runs the core user flows and saves screenshots.
 *
 * Setup (once per session, in a scratch dir, NOT in the repo):
 *   cd "$SCRATCH" && npm i playwright@1
 * Run (from that scratch dir so `playwright` resolves):
 *   node <repo>/.claude/skills/cpp-web-archaeology/scripts/ui_smoke.js --out "$SCRATCH/shots"
 *
 * Exit code 1 if any check fails. Look at the screenshots after it passes.
 */
const path = require("path");
const fs = require("fs");
const { spawn } = require("child_process");
const { chromium } = require(require.resolve("playwright", { paths: [process.cwd(), __dirname] }));

const args = Object.fromEntries(process.argv.slice(2).reduce((a, v, i, arr) => {
  if (v.startsWith("--")) a.push([v.slice(2), arr[i + 1] && !arr[i + 1].startsWith("--") ? arr[i + 1] : true]);
  return a;
}, []));
const SITE = path.resolve(__dirname, "../../../../cpp-web-archaeology");
const OUT = path.resolve(args.out || "shots");
const PORT = Number(args.port || 8765);
fs.mkdirSync(OUT, { recursive: true });

const catalog = JSON.parse(fs.readFileSync(path.join(SITE, "data/projects.json"), "utf8"));
const failures = [];
const check = (ok, msg) => { console.log((ok ? "PASS " : "FAIL ") + msg); if (!ok) failures.push(msg); };
const finds = async (p) => parseInt((await p.textContent("#status")).trim(), 10);

(async () => {
  const server = spawn("python3", ["-m", "http.server", String(PORT), "--bind", "127.0.0.1"], { cwd: SITE, stdio: "ignore" });
  await new Promise((r) => setTimeout(r, 900));
  const base = `http://127.0.0.1:${PORT}/`;
  let browser;
  try {
    browser = await chromium.launch({ executablePath: fs.existsSync("/opt/pw-browsers/chromium") ? "/opt/pw-browsers/chromium" : undefined })
      .catch(() => chromium.launch());
    for (const [name, w, h, scheme] of [["desktop", 1400, 900, "light"], ["dark", 1400, 900, "dark"], ["phone", 390, 844, "light"]]) {
      const page = await browser.newPage({ viewport: { width: w, height: h }, colorScheme: scheme });
      const errs = [];
      page.on("pageerror", (e) => errs.push(e.message));
      page.on("console", (m) => { if (m.type() === "error" && !/favicon|404/.test(m.text())) errs.push(m.text()); });
      await page.goto(base, { waitUntil: "networkidle" });
      await page.waitForTimeout(1200);
      await page.screenshot({ path: path.join(OUT, `${name}-top.png`) });

      check((await finds(page)) === catalog.length, `[${name}] shows all ${catalog.length} records on load`);
      check((await page.$$(".tile")).length >= 6, `[${name}] intent tiles rendered`);
      check((await page.$$(".layer")).length === 11, `[${name}] 11 year layers rendered`);

      if (name === "desktop") {
        const empty = await page.$$eval(".tile .cnt", (els) => els.filter((e) => e.textContent.trim() === "0").length);
        check(empty === 0, "every intent tile has at least one record");
        await page.click(".tile >> nth=1");
        await page.waitForTimeout(600);
        const n1 = await finds(page);
        check(n1 > 0 && n1 < catalog.length, `intent tile filters results (${n1})`);
        check(page.url().includes("intent="), "intent is kept in the URL");
        await page.screenshot({ path: path.join(OUT, "desktop-intent.png") });
        await page.fill("#q", "zzzz-no-match");
        await page.waitForTimeout(400);
        check((await finds(page)) === 0 && !!(await page.$(".empty")), "empty state appears for no matches");
        await page.click(".empty [data-clear='all']");
        await page.waitForTimeout(400);
        check((await finds(page)) === catalog.length, "'Start over' clears every filter");
        const y = String(catalog[0].year);
        await page.click(`.layer[data-year='${y}']`);
        await page.waitForTimeout(400);
        const ny = await finds(page);
        check(ny === catalog.filter((r) => String(r.year) === y).length, `year layer ${y} filters to ${ny}`);
        await page.keyboard.press("Escape");
        await page.click(`.layer[data-year='${y}']`);
        await page.keyboard.press("r");
        await page.waitForTimeout(800);
        check(await page.isVisible("#modal"), "R opens the random dig");
        await page.screenshot({ path: path.join(OUT, "desktop-random.png") });
        await page.keyboard.press("Escape");
        check(!(await page.isVisible("#modal")), "Esc closes the random dig");
        const badLinks = await page.$$eval("a.open", (as) => as.filter((a) => !/^https?:\/\//.test(a.getAttribute("href"))).length);
        check(badLinks === 0, "every 'Open original' link is absolute http(s)");
      }
      if (name === "phone") {
        const sw = await page.evaluate(() => document.documentElement.scrollWidth);
        check(sw <= w, `[phone] no horizontal scroll (scrollWidth ${sw})`);
        await page.evaluate(() => window.scrollTo(0, 1600));
        await page.waitForTimeout(600);
        await page.screenshot({ path: path.join(OUT, "phone-results.png") });
      }
      check(errs.length === 0, `[${name}] no page errors${errs.length ? ": " + errs.join(" | ") : ""}`);
      await page.close();
    }
  } catch (e) {
    failures.push("crash: " + e.message);
    console.error(e);
  } finally {
    if (browser) await browser.close();
    server.kill();
  }
  console.log(`\nScreenshots in ${OUT}`);
  console.log(failures.length ? `${failures.length} check(s) failed.` : "All checks passed.");
  process.exit(failures.length ? 1 : 0);
})();
