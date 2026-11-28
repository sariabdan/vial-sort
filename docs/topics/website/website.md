# The website

## Scope

This record owns how the public site is built, where its numbers come from, the conventions its pages follow, and how it is published. It also owns the [known defects](#known-defects) of the website, of the scripts that feed it and of the documentation site published beside it. Terms that are named in more than one way are in the [development conventions](../../development/conventions.md#terms). It does not own the experiments themselves: what was trained and tested is reported on the site's pages and in the [Lab notes](../../experiments/experiments.md).

## How the site is built

The site is static. Astro 7 turns the `.astro` pages under `src/pages/` into HTML at build time; there is no server at runtime. `astro build` wrote 12 pages on 2026-11-28, after the Lab notes moved to the documentation. The base path is `/vial-sort`, set in `astro.config.mjs`, so every internal address goes through `url()` in `src/lib/site.ts`.

There is no theme and no UI library. The look comes from `src/styles/global.css` and the scoped styles of each component. The only visual dependencies are the Archivo font, Observable Plot and D3 for charts, and KaTeX for formulas.

Astro 7 processes Markdown with its own processor: `markdown.rehypePlugins` in the configuration is rejected unless `@astrojs/markdown-remark` is installed. The site has no Markdown pages since 2026-11-28, so this matters only if one is added again.

## Where the numbers come from

Every number on the site is computed when the data is built, from the project's evaluation sheet, training logs and robot recordings. None is typed into a page.

1. The operator writes one line per move at the robot into `notes/<name>.txt`.
2. `scripts/notes_to_yaml.py` turns each notes file into the yaml a model is scored from.
3. `scripts/build_data.py` reads those, the training logs and the rollout reports from the `~/lerobot` checkout and writes `src/data/*.json`.
4. `scripts/make_clips.py` cuts the videos and posters named in `curation.yaml` into `public/media/` and writes `src/data/media.json`.
5. The pages import the JSON and render it.

`scripts/update_site.py` runs these steps in order with checks between them and, unless told otherwise, pushes to `main`. `src/data/*.json` and `public/media/` are tracked, because the deploy builds from what is in Git and regenerates nothing.

A change to a number is therefore made in the notes, the yaml or a script, never in `src/data/`. The Windows development machine has no `~/lerobot` checkout, so the data cannot be rebuilt there; layout and text work can be.

The score of a run is defined once, in `src/lib/score.ts` (`scoreRun`): the mean over the 12 rack slots of the share of rollouts that ended in the asked slot. The Testing page (`src/pages/method.astro`) explains it for readers.

## Page conventions

The site is read in a browser pane of about 1024×768. A page is judged by what fits on one screen there, so the pages prefer tabs, rows and folded detail to stacked sections. Layout changes are checked at 1024×768, at a wide width and at phone width.

- **Panel pages** (Results, Data, Models, Training, Testing): a list or picker on the left and a tabbed view on the right. Classes `.panel-page`, `.panel-head`, `.tabstrip`, `.panel-split` in `global.css`.
- **Tabs**: any element with `data-tabset` holds buttons with `data-t` and panels with `data-p`; the script in `src/layouts/Base.astro` switches them and keeps the tab in the address. `data-tabset="quiet"` leaves the address alone.
- **Points and steps**: `.points` for parallel statements (`pass`, `fail`, `quiet` set the top edge) and `.flow` for a sequence. A long paragraph becomes one of these or a figure, without dropping content; where no structure fits, sentences stay.
- **Vials**: `src/components/SlotVials.astro` draws one glass tube per rack slot, filled to the share of rollouts that got through, on a rack tray. Its size comes from the page through `--vw`, `--vh`, `--vgap` and `--vbin`. Runs are rows, never columns.
- **Rollout videos**: `src/components/Clip.astro` is a card with the outcome and the asked move on one line, the video, the rack diagram and the note. The full-screen control is a corner icon, styled as `.fs` in `global.css` and added to every video by the script in `Base.astro`. The Results page shows at most two cards per row.
- **First paint**: the document gets the class `js` in the head. Elements a script will hide carry `data-init-off`, and a view that a script fills carries `data-await`; the script removes both once it has drawn. Without this a page first shows every row.
- **The home page** keeps its hero and tells the story in numbered chapters (`src/components/Chapter.astro`). The hero fits one screen at 1024×768.
- **Starting state**: the Results page opens on the run with the highest score (`topRunKey` in `src/lib/score.ts`). The home page's "In short" band describes the run with the latest test day.

## Publishing

`.github/workflows/deploy.yml` runs on every push to `main`. It builds the website with Node 24 into `dist/`, builds and strictly lints this documentation with Python 3.12, exports it with `docsite.py publish`, copies the export into `dist/docs/` and publishes `dist/` to GitHub Pages.

| Address | What is there |
|---|---|
| `https://cognitive-software-labs.github.io/vial-sort/` | The website |
| `…/vial-sort/docs/` | This documentation; every file under `docs/` is public, by the owner's decision of 2026-11-28 ("its public is fine") |
| `…/vial-sort/docs/lab-notes.html` | The Lab notes |
| `…/vial-sort/docs/<old name>/` | Redirects from the four Lab-note addresses used until 2026-11-28, kept in `public/docs/` |

A failing documentation lint therefore stops the publication of the website too.

The local dev server (`npm run dev`) serves only the website: `/vial-sort/docs/` exists only in a built and merged `dist/`. The [project context](../../PROJECT_CONTEXT.md#the-combined-site) has the commands.

## Hero video

The video at the top of the home page is too low in resolution and needs replacing. Decided by the project owner on 2026-11-28, in their words: "the res of the hero video si terrible and need to be replaced".

What the current file is, read from `src/data/media.json`, `curation.yaml` and `scripts/make_clips.py` on 2026-11-28:

| Property | Value |
|---|---|
| File | `public/media/hero.mp4`, 789,816 bytes, 27.53 s |
| Frame size | 422 × 344 px |
| Source | take `012000_20261021_152757_t2`, camera `right`, a 640 × 480 recording |
| Crop | 66% of the width and 72% of the height, set in `curation.yaml` to keep the operator out of the frame |
| Encoding | H.264 at CRF 23 |

The page shows it about 540 px wide at 1024×768 and wider on a large screen, so the browser enlarges it. The crop of a 640 × 480 recording is the limit: re-encoding the same take cannot add detail.

Options, none chosen yet:

- Another take or camera where the arm fills more of the frame, so less is cropped away.
- A new recording made for the purpose at a higher camera resolution.
- The five-camera mosaic the rollout cards already use, which is sharper per pixel shown but busier.

Whichever is chosen, the change is made in `curation.yaml` (the `hero` entry) and `scripts/make_clips.py`, then rebuilt on the workstation. The hero's rack animation needs the grasp and release times of the new take, which `make_clips.py` reads from `src/data/rollouts.json`.

## Known defects

Things that are wrong in the website, the scripts or the documentation site and are not fixed yet. Each has its own line in [open work](../../open/OPEN.md). A fixed defect is removed here and from open work, and the worklog records the fix. Terms that are named in more than one way are not listed here; they are in the [development conventions](../../development/conventions.md#terms).

All were found on 2026-11-28, while the documentation was written. "Fixable here" means the data in this repository settles what is right.

### Wrong or stale statements on the website

#### Hero text names π0.5 as the latest work

`src/components/Hero.astro` says "The latest work trains π0.5 on 220 demonstrations". The newest run on the site is Isaac 0.5 Expert, by the test days in `src/data/results.json`. Fixable here; the wording is the owner's.

#### Data page names one missing move, the data has two

`src/pages/datasets.astro` names L1→L6 as the one move missing from the 220 demonstrations. `src/data/ws220.json` also has no L4→L3. Fixable here. Detail: [demonstrations, where the sources disagree](../demonstrations/demonstrations.md#where-the-sources-disagree).

#### "Destination only from the command" is said of all 220 demonstrations

The Data page and the hero say of the 220 that the destination can only come from the command. 70 of the 220 come from the first set, which was recorded one destination per sitting. Fixable here; the wording is the owner's. Detail: [demonstrations, where the sources disagree](../demonstrations/demonstrations.md#where-the-sources-disagree).

#### Testing page counts one logged FLUX rate, the data has two

`src/pages/method.astro` says one FLUX session had its rate logged. `src/data/experiments.json` logs two. Fixable here. Detail: [evaluation, where sources disagree](../evaluation/evaluation.md#where-sources-disagree).

#### "Code on GitHub" leads to a repository without the current code

The link in `src/lib/site.ts` points to `Cognitive-Software-Labs/lerebot`, whose last commit is from 2026-09-22 and which lacks the October and November work the site reports. The [code migration plan](../code-migration/code-migration.md#step-5-repoint-and-retire) owns the fix.

### The model accounts and the generated data disagree

The Models page shows the accounts in `models.yaml`. Several state counts that differ from the generated data the Results page shows, and from the Lab notes. Examples: Crispy Falafel at 30k grasped "4 of 4" in `models.yaml` and picked up the right vial in 2 of 4 rollouts in the data; the 4 November Lab note counts 35, 10 and 4 rollouts where the data has 37, 11 and 7.

Every case is in a table under "Where sources disagree" in the records for [models](../models/models.md#where-sources-disagree), [training](../training/training.md#where-sources-disagree), [evaluation](../evaluation/evaluation.md#where-sources-disagree) and [results](../results/results.md#where-sources-disagree). Which side is right needs the logs and recordings on the workstation.

### Scripts and repository

#### A compiled Python file is tracked in Git

`scripts/__pycache__/upload_hf.cpython-312.pyc` is compiled output, not source. Removing it from Git needs the owner's go.

#### `scripts/shoot.mjs` lists a page that does not exist

Its default pages include `paper/`; `src/pages/` has no such page. Fixable here.

#### `scripts/upload_hf.py` describes itself wrongly

Its docstring says it publishes 3 model repositories; the code defines 5. Fixable here.

### Documentation site

#### Wide tables scroll sideways in the reader

A page with wide tables scrolls sideways by about 100 px at a pane 1,000 px wide. Seen on `a16000-arm-test-9nov.html` and `results.html`. The reader comes from the documentation kit, so the fix belongs there or in narrower tables.

## Not verified

What could not be done or checked on the Windows development machine, because the `~/lerobot` checkout, the recordings, ffmpeg and the workstation's Python environment are not there. Each item stays open until someone with those files checks it.

- **The data pipeline was never run here.** `scripts/build_data.py`, `build_ws220.py`, `notes_to_yaml.py`, `make_clips.py`, `make_cams.py`, `annotate_setup.py`, `update_site.py` and `upload_hf.py` were read, not executed. That `src/data/*.json` and `public/media/` match what the scripts would write today is assumed.
- **`scripts/check_text.py` was not run** on any build made here. The pages changed on 2026-11-27 and 2026-11-28 were checked by eye for glued words, not by the script.
- **The hero video's properties** come from `src/data/media.json`, `curation.yaml` and `scripts/make_clips.py`. The file itself was not probed, and the 640 × 480 size of the source recording is taken from a comment in `make_clips.py`.
- **The summary band's wording for Isaac 0.5 Expert.** The band says 92% for "the slots the demonstrations used as a destination" and 30% for the others. `src/lib/score.ts` splits the slots the same fixed way for every run. Isaac was trained on the 220 demonstrations minus 8 held out. The [evaluation record](../evaluation/evaluation.md) concludes from `demo_sets` in `src/data/results.json` that the fixed split matches all three training sets; that was not checked against the dataset itself.
- **"Trained from the base model on the 220"** in the home page's Results chapter is a fixed sentence about Plain Bagel, not read from the data.
- **Where the current code is.** That the workstation's `~/lerobot` checkout holds the October and November code is inferred from the remote repository lacking it.
- **The Lab notes' sources.** No number in them was checked against the session logs, sheets or tools they cite; see [what these records lack](../../experiments/experiments.md#what-these-records-lack).
- **The full-screen icon's hover state** was not seen: the preview could not produce a real pointer hover.