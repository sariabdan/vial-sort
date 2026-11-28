# Worklog

Append-only chronology, newest entries first. Keep detailed evidence in its producing experiment or topic.

## 2026-11-28: Lab notes moved into the documentation, documentation published at /vial-sort/docs/

The four dated notes left the website (`src/pages/docs/`, with `src/layouts/Doc.astro` and the notes index page) and became records under `docs/experiments/`, registered in `docs/site/site.toml` under the page names of their old addresses. Their bodies are unchanged; the YAML frontmatter became the opening of each file. The deploy workflow now builds the website and the documentation and publishes the documentation under `/vial-sort/docs/`; `public/docs/` redirects the four old addresses. The website's menu entry "Lab notes" became "Docs". Why: the owner asked for the documentation at that address and for one kind of docs instead of two (2026-11-28).

Checks run by hand on Windows: `astro build` (12 pages), `docsite.py build`, `lint --strict` with 0 warnings, `publish`, and the merged `dist/` served with `astro preview`: the 13 internal links of the documentation home answered 200, and an old note address redirected to its new page. The workflow itself has not run. What could not be verified is listed in the website record under "Not verified". The commit that contains this entry is its source identity.

## 2026-11-28: documentation kit 6.0.0 adopted

Added the documentation kit as the `.docs-kit` submodule at `v6.0.0` and wrote the project's first records: project context, reading index, capability map, the website record and the code-migration plan. The starter's placeholder guide and its two figure fragments were not kept; they remain in `.docs-kit/examples/starter/`. `AGENTS.md` is now the kit's task router and replaces the Astro template text; `README.md` describes the project. Why: the repository had no documentation of its own beyond script headers.

Checks run on the Windows development machine with `PYTHONUTF8=1`: `docsite.py build` and `docsite.py lint --strict`. The website's own `astro build` was run as well. Nothing was measured. The commit that contains this entry is its source identity.

## 2026-11-28: home page and Results rework, not yet published

Local changes after commit `8d1cea6`: the home page was shortened and its introduction fits one screen at 1024×768; rollout videos became cards with a corner full-screen icon; the Results page shows at most two videos per row and opens on the run with the highest score; the home page's "In short" band names the run with the latest test day instead of the largest π0.5 run; the site address moved to `cognitive-software-labs.github.io`. Checked by `astro build` and by looking at the pages at 1024×768, 1600×950 and 375 px wide. The commit that contains this entry is its source identity.
