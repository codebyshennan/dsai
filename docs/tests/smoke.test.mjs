import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";

const docsRoot = path.resolve(import.meta.dirname, "..");

function read(relPath) {
  return fs.readFileSync(path.join(docsRoot, relPath), "utf8");
}

test("pnpm build scripts use the supported make targets", () => {
  const pkg = JSON.parse(read("package.json"));

  assert.equal(pkg.scripts["build:jekyll"], "make jekyll-build");
  assert.equal(pkg.scripts["build:jekyll-with-search"], "make jekyll-build-with-search");
});

test("search modal copy references working build commands", () => {
  const header = read("_includes/site-header.html");

  assert.match(header, /pnpm run build:jekyll-with-search/);
  assert.match(header, /make search/);
});

test("maintainer docs keep the supported local build flow", () => {
  const claude = read("CLAUDE.md");

  assert.match(claude, /make bundle-install/);
  assert.match(claude, /make dev/);
  assert.match(claude, /make search/);
  assert.match(claude, /pnpm run build:jekyll-with-search/);
});

test("search UI traps focus and prefers the search input", () => {
  const script = read("assets/js/search-ui.js");

  assert.match(script, /function focusSearchInput\(/);
  assert.match(script, /function setOpenState\(/);
  assert.match(script, /if \(window\.PagefindUI\)[\s\S]*focusSearchInput\(\)/);
  assert.match(script, /if \(e\.key !== 'Tab'\) return;/);
  assert.match(script, /lastFocused = document\.activeElement/);
  assert.match(script, /el\.inert = true/);
});

test("lesson nav dropdown supports keyboard access", () => {
  const script = read("assets/js/lesson-nav.js");
  const template = read("_includes/lesson-nav.html");
  const styles = read("assets/css/style.css");

  assert.match(script, /function focusItem\(/);
  assert.match(script, /e\.key === 'ArrowDown'/);
  assert.match(script, /e\.key === 'Home'/);
  assert.match(template, /aria-haspopup="menu"/);
  assert.match(template, /aria-current="page"/);
  assert.match(styles, /\.lesson-nav__dropdown-item a:focus-visible/);
});
