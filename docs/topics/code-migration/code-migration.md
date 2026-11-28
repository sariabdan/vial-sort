# Moving the project's code into this repository

## Scope

A plan. The project owner decided on 2026-11-28 that the project's code moves into this repository and is documented here, in their words: "all the code from the repo needs to be moved and dcoumented here (big task break it down a bit)". This document breaks that into steps and names the decisions that are the person's. It is deleted when the move has landed and its lasting content is in the owning records.

Nothing below has been started.

## What is known

Read from the remote repository `https://github.com/Cognitive-Software-Labs/lerebot` on 2026-11-28, at commit `8c0fb52` on `main`, its only branch. Only the file list, the commit log and the top of its README were read, not the code.

- It is a fork of LeRobot with 1,136 files. The largest folders: `src` 471, `tests` 217, `ee` 136, `docs` 110, `.agents` 54, `examples` 43, `isaac` 43.
- It has four commits; the last is from 2026-09-22.
- The project's own work appears to sit in `ee/`, `isaac/`, `calibration/` and parts of `docs/`. Which files under `src/` and `tests/` the project changed is not known.
- Its README describes the first campaign: ACT on the Jetson Thor rig with a fixed destination.

Files this repository's scripts read from the `~/lerobot` checkout, and whether the remote has them:

| File | In the remote |
|---|---|
| `ee/robometer_runs.csv` | yes |
| `ee/extract_episode_clips.py` | yes |
| `ee/eval_runs_v5.csv` | no |
| `ee/annotate_setup_v5.py` | no |
| `tools/assess_rollouts.py` | no; the remote has no `tools/` folder |

So the remote is behind the workstation. That the current code exists only in the workstation's `~/lerobot` checkout is an inference from this table and from the commit dates; it was not checked on the workstation.

## Step 1: publish the current state

Push the workstation's `~/lerobot` checkout to GitHub as it is, on a branch if `main` should stay untouched. Until this is done nothing else can be inventoried or moved from another machine.

Before pushing, check what is untracked or ignored there: recordings, checkpoints, tokens and machine-specific paths must not go up. Datasets and checkpoints stay on Hugging Face.

Done when: the remote has the files in the table above and the October training and evaluation scripts.

## Step 2: inventory

Sort every folder of the pushed state into one of four kinds:

- The project's own code: training and evaluation scripts, robot runtime and recording, calibration, the Isaac work, tools.
- Upstream LeRobot, unchanged.
- Upstream LeRobot, changed by the project. Each change needs a line saying what and why.
- Documents: the working notes under `ee/` and the write-ups under `docs/sections/`, each marked current or historical.

Also list which files this repository's scripts read, with the script that reads them.

Done when: the inventory is a table in this document, and the size of each kind is known in files and megabytes.

## Step 3: decisions for the person

Each is a choice that shapes the rest; none is made.

- **What moves.** Only the project's own code, or the whole fork with LeRobot's source and tests. The inventory gives the sizes.
- **How LeRobot is depended on.** A pinned upstream version plus the project's changes as patches or a small fork, or the full fork vendored here.
- **History.** Bring the old repository's commits along, or copy the files and cite the old repository's commit as the source.
- **Layout.** Where the code sits beside the site, for example `site/` and `robot/`, or the site stays at the root and code goes under named folders. Moving the site changes the deploy workflow and every path in these records.
- **Repository name.** This repository is called `vial-sort` and is published as a site at `/vial-sort/`. Holding all code here keeps that name and address.
- **The old documents.** Which of the working notes become topic records here, and which stay behind as history.

## Step 4: move in slices

Each slice is one deliverable: the code, its record under `docs/topics/<topic>/`, its rows in the [capability map](../../CAPABILITY_MAP.md) and a worklog entry. A slice lands only when what it needs runs from this repository.

1. **Evaluation and scoring.** The evaluation sheets, the rollout assessment tool and what `scripts/build_data.py` reads. After it, the site's data rebuilds from one repository.
2. **Training.** Training scripts and configurations for π0.5, FLUX 3 Action and Isaac 0.5, with the cluster commands.
3. **Robot runtime.** Running a model on the arm, recording, the camera setup and calibration.
4. **Data collection.** Demonstration recording, the command wording and dataset preparation.
5. **Isaac.** The `isaac/` folder.
6. **Earlier campaigns.** The August Thor work, kept as history with its original commands and results.

The order puts first what removes the dependency of the site on a second checkout.

## Step 5: repoint and retire

- Replace the `~/lerobot` defaults in `scripts/*.py` with paths inside this repository.
- Point the "Code on GitHub" link in `src/lib/site.ts` at this repository.
- Correct the deploy workflow's comment and decide whether the workflow runs the checks.
- Rewrite `README.md` and the [project context](../../PROJECT_CONTEXT.md) for a repository that holds code and site.
- Decide what happens to `Cognitive-Software-Labs/lerebot`: archived with a pointer here, or deleted. Archiving or deleting it is the person's action.

## Risks

- A push to `main` here publishes the site. Code slices should not ride along with unfinished site changes.
- Large files: recordings and checkpoints must not enter Git history, where they stay even after deletion.
- Paths of the workstation and the cluster, and any token, must be removed or made configurable before code is public. `scripts/check_text.py` checks the built site for these, not source files.
