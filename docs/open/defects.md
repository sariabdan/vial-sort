# Known defects

Things that are wrong or inconsistent in the website, the scripts or the documentation site and are not fixed yet. Each has one line in [open work](OPEN.md). A fixed defect is removed here and from the open list, and the worklog records the fix.

All were found on 2026-11-28, while the documentation was written. "Fixable here" means the data in this repository settles what is right.

## Wrong or stale statements on the website

### Hero text names π0.5 as the latest work

`src/components/Hero.astro` says "The latest work trains π0.5 on 220 demonstrations". The newest run on the site is Isaac 0.5 Expert, by the test days in `src/data/results.json`. Fixable here; the wording is the owner's.

### Data page names one missing move, the data has two

`src/pages/datasets.astro` names L1→L6 as the one move missing from the 220 demonstrations. `src/data/ws220.json` also has no L4→L3. Fixable here. Detail: [demonstrations, where the sources disagree](../topics/demonstrations/demonstrations.md#where-the-sources-disagree).

### "Destination only from the command" is said of all 220 demonstrations

The Data page and the hero say of the 220 that the destination can only come from the command. 70 of the 220 come from the first set, which was recorded one destination per sitting. Fixable here; the wording is the owner's. Detail: [demonstrations, where the sources disagree](../topics/demonstrations/demonstrations.md#where-the-sources-disagree).

### Testing page counts one logged FLUX rate, the data has two

`src/pages/method.astro` says one FLUX session had its rate logged. `src/data/experiments.json` logs two. Fixable here. Detail: [evaluation, where sources disagree](../topics/evaluation/evaluation.md#where-sources-disagree).

### "Code on GitHub" leads to a repository without the current code

The link in `src/lib/site.ts` points to `Cognitive-Software-Labs/lerebot`, whose last commit is from 2026-09-22 and which lacks the October and November work the site reports. The [code migration plan](../topics/code-migration/code-migration.md#step-5-repoint-and-retire) owns the fix.

## Inconsistent wording

### "Held out" means two things

In the glossary (`src/lib/glossary.ts`) it means rack slots never demonstrated as a destination. In `src/data/registry.json` and `src/data/results.json`, "220 minus 8 held out" means 8 demonstrations left out of Isaac's training copy. Needs the owner's decision on which meaning keeps the term.

### One camera and one vial colour have several names

The camera `left_bottom` is "Near eye level" in `src/lib/site.ts` and "Near table level" on the Data page. The third vial colour is "dark green" on the Data page, "lime" in `src/components/RackGlyph.astro` and `curation.yaml`, and "green" on the August page. Needs someone who knows the rig to say which is right.

## Counts that differ between sources

### The model accounts and the generated data disagree

The Models page shows the accounts in `models.yaml`. Several state counts that differ from the generated data the Results page shows, and from the Lab notes. Examples: Crispy Falafel at 30k grasped "4 of 4" in `models.yaml` and picked up the right vial in 2 of 4 rollouts in the data; the 4 November Lab note counts 35, 10 and 4 rollouts where the data has 37, 11 and 7.

Every case is in a table under "Where sources disagree" in the records for [models](../topics/models/models.md#where-sources-disagree), [training](../topics/training/training.md#where-sources-disagree), [evaluation](../topics/evaluation/evaluation.md#where-sources-disagree) and [results](../topics/results/results.md#where-sources-disagree). Which side is right needs the logs and recordings on the workstation.

## Scripts and repository

### A compiled Python file is tracked in Git

`scripts/__pycache__/upload_hf.cpython-312.pyc` is compiled output, not source. Removing it from Git needs the owner's go.

### `scripts/shoot.mjs` lists a page that does not exist

Its default pages include `paper/`; `src/pages/` has no such page. Fixable here.

### `scripts/upload_hf.py` describes itself wrongly

Its docstring says it publishes 3 model repositories; the code defines 5. Fixable here.

## Documentation site

### Wide tables scroll sideways in the reader

A page with wide tables scrolls sideways by about 100 px at a pane 1,000 px wide. Seen on `a16000-arm-test-9nov.html` and `results.html`. The reader comes from the documentation kit, so the fix belongs there or in narrower tables.
