# Worklog

Append-only chronology, newest entries first. Keep detailed evidence in its producing experiment or topic.

## 2026-11-28: the documentation becomes the project's, with six subject records

Wrote the records of the project itself: task and rig, demonstrations, models, training, evaluation and results, each from the website's pages, `models.yaml`, the operator's notes, the Lab notes and the generated data under `src/data/` as of commit `8065309`. No number was re-derived from logs or recordings, which are not in this repository; the results table was recomputed from `src/data/results.json` with the definition in `src/lib/score.ts` and matches the website for the two runs compared (Isaac 0.5 Expert 61%, Plain Bagel 47%). Each record lists where its sources disagree. The documentation home, the project context and `README.md` now describe the project, not the website. The documentation menu lists the records and an entry that leads back to the website; the "Lab notes" menu button is gone and the notes stay reachable from the records and the Reference list. Why: the owner pointed out on 2026-11-28 that the repository is about vial-sort and the website is only its public face.

The first run of the deploy workflow rewritten in the entry below succeeded on 2026-11-28: the documentation home, the Lab notes list, one note and one redirect answered on the live site.

The defects found while writing moved out of the website record into `docs/open/defects.md`, each with its own line in open work, because the owner found them hard to see there. Open work also states that no person has read the records and that Sari Abdan reviews them (`docs/open/human-review.md`).

Checks: `docsite.py build` and `lint --strict` with 0 warnings. The commit that contains this entry is its source identity.

## 2026-11-28: Lab notes moved into the documentation, documentation published at /vial-sort/docs/

The four dated notes left the website (`src/pages/docs/`, with `src/layouts/Doc.astro` and the notes index page) and became records under `docs/experiments/`, registered in `docs/site/site.toml` under the page names of their old addresses. Their bodies are unchanged; the YAML frontmatter became the opening of each file. The deploy workflow now builds the website and the documentation and publishes the documentation under `/vial-sort/docs/`; `public/docs/` redirects the four old addresses. The website's menu entry "Lab notes" became "Docs". Why: the owner asked for the documentation at that address and for one kind of docs instead of two (2026-11-28).

Checks run by hand on Windows: `astro build` (12 pages), `docsite.py build`, `lint --strict` with 0 warnings, `publish`, and the merged `dist/` served with `astro preview`: the 13 internal links of the documentation home answered 200, and an old note address redirected to its new page. The workflow itself has not run. What could not be verified is listed in the website record under "Not verified". The commit that contains this entry is its source identity.

## 2026-11-28: documentation kit 6.0.0 adopted

Added the documentation kit as the `.docs-kit` submodule at `v6.0.0` and wrote the project's first records: project context, reading index, capability map, the website record and the code-migration plan. The starter's placeholder guide and its two figure fragments were not kept; they remain in `.docs-kit/examples/starter/`. `AGENTS.md` is now the kit's task router and replaces the Astro template text; `README.md` describes the project. Why: the repository had no documentation of its own beyond script headers.

Checks run on the Windows development machine with `PYTHONUTF8=1`: `docsite.py build` and `docsite.py lint --strict`. The website's own `astro build` was run as well. Nothing was measured. The commit that contains this entry is its source identity.

## 2026-11-28: home page and Results rework, not yet published

Local changes after commit `8d1cea6`: the home page was shortened and its introduction fits one screen at 1024×768; rollout videos became cards with a corner full-screen icon; the Results page shows at most two videos per row and opens on the run with the highest score; the home page's "In short" band names the run with the latest test day instead of the largest π0.5 run; the site address moved to `cognitive-software-labs.github.io`. Checked by `astro build` and by looking at the pages at 1024×768, 1600×950 and 375 px wide. The commit that contains this entry is its source identity.
