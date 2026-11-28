# The website

## Scope

This record owns how the public site is built, where its numbers come from, the conventions its pages follow, how it is published and its known defects. It does not own the experiments themselves: what was trained and tested is reported on the site's pages and in the Lab notes under `src/pages/docs/`.

## How the site is built

The site is static. Astro 7 turns the `.astro` pages and the Markdown Lab notes under `src/pages/` into HTML at build time; there is no server at runtime. `astro build` wrote 17 pages on 2026-11-28. The base path is `/vial-sort`, set in `astro.config.mjs`, so every internal address goes through `url()` in `src/lib/site.ts`.

There is no theme and no UI library. The look comes from `src/styles/global.css` and the scoped styles of each component. The only visual dependencies are the Archivo font, Observable Plot and D3 for charts, and KaTeX for formulas.

Astro 7 processes Markdown with its own processor: `markdown.rehypePlugins` in the configuration is rejected unless `@astrojs/markdown-remark` is installed. `src/layouts/Doc.astro` therefore folds long tables itself, by rendering the slot and rewriting the HTML.

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

`.github/workflows/deploy.yml` builds with Node 24 and publishes to GitHub Pages on every push to `main`. The address is `https://cognitive-software-labs.github.io/vial-sort/`.

The workflow's comment says the data is regenerated with `make site`. No Makefile exists in the repository; the command is `scripts/update_site.py`.

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

- `scripts/__pycache__/upload_hf.cpython-312.pyc` is tracked in Git. It is compiled output, not source. Removing it from Git needs the person's go.
- The deploy workflow's comment names `make site`, which does not exist.
- The "Code on GitHub" link in `src/lib/site.ts` points to `Cognitive-Software-Labs/lerebot`, whose last commit is from 2026-09-22 and which lacks the October work the site reports. The [code migration plan](../code-migration/code-migration.md) owns the fix.
- The hero's text still says the latest work trains π0.5, while the newest run on the site is Isaac 0.5 Expert.
- `scripts/shoot.mjs` lists `paper/` among its default pages; no such page exists in `src/pages/`.
