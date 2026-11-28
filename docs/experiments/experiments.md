# Lab notes

Dated records of arm tests and retrains, each written at the time of the session. They cover the work after the October pages of the website: demonstrations recorded so the destination comes from the command, two retrains of π0.5, and how each one did on the arm.

Newest first:

| Date | Note | What it records |
|---|---|---|
| 2026-11-09 | [Arm test: π0.5 A at 16000 steps, against B](2026-11-09-a16000-arm-test/a16000-arm-test.md) | A, trained from the pi05 base, on the same 31 moves as B; the probes and the camera check |
| 2026-11-08 | [Arm test: π0.5 B at 16000 steps](2026-11-08-b16000-arm-test/b16000-arm-test.md) | B at 16000 steps on the arm |
| 2026-11-07 | [Retraining π0.5 on a university cluster](2026-11-07-retrains-on-the-cluster/retrains-on-the-cluster.md) | The two full fine-tunes on the 220 demonstrations |
| 2026-11-04 | [Arm test: π0.5 B at 4000 steps](2026-11-04-b4000-arm-test/b4000-arm-test.md) | B at 4000 steps on the arm |

A and B are the names the notes use. The website calls A "Plain Bagel" and B "Mango Pudding"; each note states its models under its title.

## Where they came from

Until 2026-11-28 these four notes were pages of the public website, written as Markdown with YAML frontmatter under `src/pages/docs/` and shown at `/vial-sort/docs/<name>/`. They moved here unchanged in their body. The frontmatter became the opening of each file: the title, the date and description, the models, and the list "In short". Links between the notes now point at the files. The old addresses redirect to the new pages; `public/docs/<name>/index.html` holds each redirect.

## What these records lack

A record of an experiment keeps its protocol, producing code, inputs and run output in its own folder, so that a claim can be checked again. These four hold the write-up only. What they cite lives in the `~/lerobot` checkout on the workstation, which is not in this repository and was not available when they moved:

| Cited in the notes | State |
|---|---|
| `ee/ROLLOUT_ws220_B16000_8nov.md`, `ee/CLUSTER_CLAUSTHAL.md` | Not in this repository; not found in the remote `Cognitive-Software-Labs/lerebot` file list of 2026-11-28 by name search for October and November work |
| `tools/assess_rollouts.py`, `tools/pin_quantiles.py` | Not in this repository; the remote has no `tools/` folder |
| `outputs/pi05_full_vial-sort-ws220_canon_base16k/checkpoints/016000` and the two `…_ft012000…` checkpoints | Training outputs on the workstation or cluster; whether the published Hugging Face models are the same files was not checked |
| The session logs and recordings each note counts rollouts from | Not in this repository |

So no number in these notes was checked against its source during the move. They are kept as written. The [code migration](../topics/code-migration/code-migration.md#step-4-move-in-slices) brings the evaluation tools and sheets here; after that, each note's folder can receive its inputs and run output, or a statement of where they are and how to check they are the same files.

## Writing a new note

One folder per session, `docs/experiments/<date>-<subject>/`, with the note named after its subject. Read `.docs-kit/rules/experiments/workflow.md` before designing a session and `.docs-kit/rules/records.md` before writing it up. Add the note to the table above and register it in `docs/site/site.toml` so it has a stable address.
