# Worklog

Append-only chronology, newest entries first. Keep detailed evidence in its producing experiment or topic.

## 2026-11-28: Demonstrations gets a page for people

`docs/topics/demonstrations/index.md` explains the [demonstrations record](topics/demonstrations/demonstrations.md) in eight chapters, in the Task and rig pattern: the two sets, why the 220 were recorded the way they were, which moves they cover, how the commands are worded, the batches, the training copies, where the sets are published, and the disagreements. Its figures draw only what the record states: what the two sets are made of, one destination per sitting against one layout with three destinations, which moves each set covers (in tabs, drawn from the record's held-out rules and move counts, not from per-move counts), the wording pools and the wordings they multiply to, the wrist pitch at release by batch, and the frames of each training copy. The page prints no Hugging Face address, because the account carries a person's user name.

The menu entry "Demonstrations" opens the page and the record moves to the slug `demonstrations-record`. The 19 anchors of the old `demonstrations.html` resolve on the page, among them the two that the Task and rig page links.

Points the page author found in the record and left to it: the record names the Hugging Face account by a person's user name, which a page may not print. Figure 3 relies on the record's statement that L1 → L6 and L4 → L3 are the only moves between trained slots without a demonstration; with 32 and 48 moves that statement fixes every cell, but the record does not say so in one place.

Checks: `docsite.py build`, `lint --strict` with 0 warnings and `build --check-reader`. In the browser in One chapter view at 375 × 812, 1024 × 768 and 1600 × 1000, both tabs of Figure 3 included: no sideways overflow; no text below 11 px; no figure label cut off or overlapping another; smallest figure label, font size times scale, 11.7 px at 375, 11.9 px at 1024 and 22.9 px at 1600. The commit that contains this entry is its source identity.

## 2026-11-28: Training gets a page for people

`docs/topics/training/index.md` explains the [training record](topics/training/training.md) in eight chapters, in the Task and rig pattern: why the first models read the destination off the picture, Mango Rice's offline gate, the scaling mismatch and its fix, the cluster retrains, their probes, the runs and their losses, the data changes training depends on, and the disagreements. Its figures draw only what the record states: the destination probe of 21 October, the offline gate checkpoint by checkpoint, the gripper commands before and after the wider scale, the grasp of the three 4 Nov versions, the two cluster runs on a time line, `probe_shortcut` on both retrains, and the start and end loss of the eight runs with a curve.

The menu entry "Training" opens the page and the record moves to the slug `training-record`. The 24 anchors of the old `training.html` resolve on the page.

Points the page author found in the record and left to it: none beyond the record's own lists of disagreements and unverified points; the offline gate's insertion and gripper errors are stated only at the first and last checkpoint, so the page cannot draw their fall.

Checks: `docsite.py build`, `lint --strict` with 0 warnings and `build --check-reader`. In the browser in One chapter view at 375 × 812, 1024 × 768 and 1600 × 1000: no sideways overflow; no text below 11 px; no figure label cut off or overlapping another; smallest figure label, font size times scale, 11.7 px at 375, 11.9 px at 1024 and 22.9 px at 1600. The commit that contains this entry is its source identity.

## 2026-11-28: Models gets a page for people

`docs/topics/models/index.md` explains the [models record](topics/models/models.md) in eight chapters, in the Task and rig pattern: the family tree, the shared π0.5 recipe, the October runs, the November retrains, Isaac 0.5 Expert, FLUX 3 Action, the August and planned models, and the disagreements. Its figures draw only what the record states: what each model started from and was trained on, with its scored rollouts as read at commit 8065309; the October runs from Spicy Chicken's freeze to Mango Rice; the gripper and wrist ranges behind the 4 Nov grasp failures; Isaac 0.5 Expert by destination and offline; and FLUX's 8 by 8 picture grid against one rack. The page prints no Hugging Face address, because those addresses carry a person's user name.

The menu entry "Models" opens the page and the record moves to the slug `models-record`. The 24 anchors of the old `models.html` resolve on the page; the chapter on the shared recipe has the ASCII id `the-shared-pi05-recipe` and keeps the old anchor with "π" as a span inside it.

Points the page author found in the record and left to it: Mango Chutney's story says the wrist pitch range changed by 8%, while the q99 patch it describes goes from 31.5 to 43.2; the record does not say how the two figures relate. The table of all models gives Hugging Face addresses under a person's user name, which a page may not print.

Checks: `docsite.py build`, `lint --strict` with 0 warnings and `build --check-reader`. In the browser in One chapter view at 375 × 812, 1024 × 768 and 1600 × 1000: no sideways overflow; no text below 11 px; no figure label cut off or overlapping another; smallest figure label, font size times scale, 11.7 px at 375, 11.9 px at 1024 and 22.9 px at 1600. The commit that contains this entry is its source identity.

## 2026-11-28: Evaluation gets a page for people

`docs/topics/evaluation/index.md` explains the [evaluation record](topics/evaluation/evaluation.md) in nine chapters, in the Task and rig pattern: the score, why it is built this way, the three outcome stages, scoring from notes or from the arm, what is left out, how a rollout is run, the 12-move gate, what the numbers cannot say, and the disagreements. Its figures draw only what the record states: the score worked out on Isaac 0.5 Expert slot by slot, the mean against the median and the binomial argument for a bar on the mean, the outcome kinds and their stages, the eye checks, what is left out, the actions a second on the arm, and the 12-move gate of 8 and 9 Nov.

The menu entry "Evaluation" opens the page and the record moves to the slug `evaluation-record`. The 28 anchors of the old `evaluation.html` resolve on the page, as chapter ids or as spans inside the chapter that explains them.

Points the page author found in the record and left to it: the glossary's rollout ends "until it stops or the session ends", while how a rollout is run says it ends when a person stops it or a camera drops off the bus; π0.5's rate is stated only for sync mode.

Checks: `docsite.py build`, `lint --strict` with 0 warnings and `build --check-reader`. In the browser in One chapter view at 375 × 812, 1024 × 768 and 1600 × 1000: no sideways overflow; no text below 11 px; no figure label cut off or overlapping another; smallest figure label, font size times scale, 11.7 px at 375, 11.9 px at 1024 and 22.9 px at 1600. The commit that contains this entry is its source identity.

## 2026-11-28: Results gets a page for people

`docs/topics/results/index.md` explains the [results record](topics/results/results.md) in six chapters, in the Task and rig pattern: no run passed, 100 against 220 demonstrations, on the robot, not solved, disagreements, and where the numbers live. Its figures draw only what the record states: the most rollouts at one slot against the 10 needed and the split of the 335 takes, the three runs the home page compares, Plain Bagel against Mango Pudding on the same 31 moves, and where the vial ended when a far or held-out slot was asked for, all as readings at commit 8065309. The page copies no run table; it links the website's Results page for the live numbers.

The menu entry "Results" opens the page and the record moves to the slug `results-record`. The 9 anchors of the old `results.html` resolve on the page. The chapter that compares the 100 and the 220 demonstrations has the ASCII id `the-100-against-the-220`, and the old anchor, which contains "π", is a span inside it: the kit's reader did not route to a chapter whose own id holds a non-ASCII character, and moved that chapter to the end.

Points the page author found in the record and left to it: the reading of Isaac 0.5 Expert's far slots does not say which rack; the reading "asked R2, it went to R1 three times" gives no count of tries; the record does not say what Mango Rice was trained from, only on what.

Checks: `docsite.py build`, `lint --strict` with 0 warnings and `build --check-reader`. In the browser in One chapter view at 375 × 812, 1024 × 768 and 1600 × 1000: no sideways overflow; no text below 11 px; smallest figure label, font size times scale, 12.2 px at 375, 12.4 px at 1024 and 23.8 px at 1600. The commit that contains this entry is its source identity.

## 2026-11-28: Task and rig gets a page for people, the first with the chapter reader

The owner asked for pages for people so the documentation uses the kit's chapter reader. Until now every menu entry was a record shown whole, which never gets the reader, so the reader was on in `docs/site/site.toml` and used by no page. `docs/topics/task-and-rig/index.md` is the first such page: seven chapters (the task, the arm, the five cameras, who sees what, commands, earlier rigs, not verified), with a rack schematic, a demonstrate-train-run flow, the rig photograph, the camera stills in tabs, a camera-by-model matrix and a command diagram, all drawn from the [task and rig record](topics/task-and-rig/task-and-rig.md). It says that the record was written by AI and not yet reviewed by a person.

The menu entry "Task and rig" opens the page. The record stays a registered source page under the new slug `task-and-rig-record`, because one slug belongs to one page; the comment in `site.toml` states the pattern for the other topics. The 14 anchors of the old `task-and-rig.html` still resolve on the page. Figures 1 and 5 carry a second, narrower drawing that the page shows below 360 px of figure width, so that their labels stay at 11 px or more on a phone.

Points the page author found in the record and left to it: the record does not say where the racks and the bin sit on the table, and the overhead still shows the bin beyond one rack, not between them; the rig photograph's "Rack 1" and "Rack 2" are not mapped to left and right; "mode" is used in the definition of a session without being defined; no table lists what the figures' colours mean. Whether the page gets slide faces is the owner's question; it has none.

Checks: `docsite.py build`, `lint --strict` with 0 warnings and `build --check-reader`. In the browser at 375 × 812, 1024 × 768 and 1600 × 1000 in the reader's dark theme: no sideways overflow; smallest figure label, font size times scale, Figure 1 16, 28.5 and 41.4 px, Figure 5 13, 13.6 and 24.6 px. The commit that contains this entry is its source identity.

## 2026-11-28: the demonstrations, models and training records point at the data instead of copying it

The [demonstrations](topics/demonstrations/demonstrations.md), [models](topics/models/models.md) and [training](topics/training/training.md) records copied generated data row by row as a snapshot of commit 8065309, as the results record did before. A copy goes stale with every rebuild of the data, and the kit's documentation rules give every fact one home. Each copied table is now a map: which file and key hold the values, what the fields mean, and which page or script shows or produces them. Section headings are unchanged, so their anchors still resolve.

- Demonstrations: the two coverage matrices (`coverage.demos` in `src/data/october.json`, `demos` in `src/data/ws220.json`), the word pools and recorded wordings, the held-out table, the batch sizes and the tables of published and earlier datasets (`src/data/datasets.json`). Kept: the two sets compared, the batch names of the data, the Data page and the Lab notes, the camera differences, the known problems, the training copies, "Where the sources disagree" and "Not verified".
- Models: "Per-model facts at a glance" (`src/data/registry.json`), the settings tables of the π0.5 runs, Isaac 0.5 Expert and Crispy Falafel (`hyper` in `src/data/experiments.json`), the FLUX camera table (`camera_choice` in `models.yaml`), the August policies and the planned and considered models (`src/data/models.json`). Kept: "All models", each model's facts and story, the settings each model does not share with the others, "Where sources disagree" and "Not verified".
- Training: "The runs" and its gradient norms (`src/data/training.json`), "Training logs per run" (`logs` in `models.yaml`), "Learning-rate schedules and lengths" (`hyper`) and the offline gate table (`src/data/gate.json`). Kept: the hardware and dates of each run, which are not in the data, the loss-curve readings, the Lab notes' tables, the 21 Oct probe from `src/lib/probe.ts`, "Where sources disagree" and "Not verified".

Each record now has a dated list of the readings it argues from, at commit 8065309. All were rechecked against `src/data/` and `models.yaml` at this commit, unchanged since 8065309, by a one-off script outside the repository. Demonstrations: the 100 have 32 moves, 75 rack to rack, 25 to the bin, none inside a rack; the 220 have 48 moves, 41 to the bin, 51 inside a rack, 128 rack to rack; the only gaps between trained slots in the 220 are L1 → L6 and L4 → L3; batches 70, 51 and 99 add up to 220 and 141,735 frames; 100 wordings across 32 moves, at most 4 for one move; pools 6, 4, 5, 4, 5 and 4, multiplying to 38,400 and 9,600. Models: the seven π0.5 runs with a config differ only in starting weights, peak learning rate, warm-up, decay, steps and passes; rollouts and left-out rollouts per model. Training: eight runs with a loss curve and their start and end losses; resumes at 8,000 (Plain Bagel, Mango Pudding), 7,000 and 8,000 (Spicy Chicken) and 10,000 (Crispy Falafel); the gate leaves home 9 of 9 at every checkpoint, follows the source at 2k and from 5k, never binds roles, reads 0 of 7 destination frames, errors 4.8° → 1.4° and 7.1° → 1.7°.

Checks: `docsite.py build` and `lint --strict` with 0 warnings, in a clean worktree with only this change. The commit that contains this entry is its source identity.

## 2026-11-28: the results record points at the data instead of copying it

The [results record](topics/results/results.md) copied the generated data: four tables of 22 runs, the confusion matrices, the accounts of each model and the home page's "What is not solved" values, as a snapshot of commit 8065309. A copy goes stale with every rebuild of the data, and the kit's documentation rules give every fact one home. The record now says where each kind of result lives (`src/data/results.json` keys, `src/data/rollouts.json`, `src/data/experiments.json`, `scoreRun` and `weakSlots` in `src/lib/score.ts`, the sort in `src/pages/results.astro`) and that the website build is the reproduction of the scores. Its readings of the data are kept as a dated list at commit 8065309; the comparison, the Lab notes' findings, "Where sources disagree" and "Not verified" are kept. The scores computed by a one-off script outside the repository are no longer stated as current; the record says so.

Rechecked against `src/data/` at this commit, unchanged since 8065309: 22 runs, 287 scored rollouts, at most 9 rollouts at one rack slot, 5 runs tried at a held-out destination, 61 sessions and 335 takes.

Checks: `docsite.py build` and `lint --strict` with 0 warnings, in a clean worktree with only this change. The commit that contains this entry is its source identity.

## 2026-11-28: known defects back in their owning record, terms list in the development conventions

`docs/open/defects.md` was a second list of owed work beside open work, which the kit's documentation rules do not allow ("Do not create a generic archive, review collection or second status system"). Its defects of the website, the scripts and the documentation site are now a section of the [website record](topics/website/website.md#known-defects), with their wording unchanged. Every defect keeps its own line in [open work](open/OPEN.md), now linking that section, so they stay as easy to see as the owner asked. The file was removed at the owner's request to fix it.

The kit's records rule asks for one list of renamed terms in the development conventions. [`docs/development/conventions.md`](development/conventions.md) now holds it: the terms with several names and the record that defines each, and the three names that need a decision ("held out", the page name of the camera `left_bottom`, the third vial colour), which were defects before. Open work routes each of those three to the conventions.

Checks: `docsite.py build` and `lint --strict`. The commit that contains this entry is its source identity.

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
