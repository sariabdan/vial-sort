# Capability map

This map lists what the project's tooling does, one need per row, so that a
need is solved once and found again. Read it before building tooling, a
harness or other supporting code. **Name the need first** and **The
capability map** in `.docs-kit/rules/engineering/code.md` say how to use it
and what each column holds.

The Imported by column is generated from Python imports; never type it.
`python .docs-kit/docsite.py capability-map --project .` rewrites it.

All scripts except `check_text.py` and `shoot.mjs` read a `~/lerobot` checkout
and its recordings. That checkout is not on the Windows development machine,
so "exists" below means the script is in the repository; none of them was run
there.

## Capabilities

| Need | Code | State | Imported by |
|---|---|---|---|
| Turn evaluation sheets, training logs and rollout reports into the JSON the pages read | [`scripts/build_data.py`](../scripts/build_data.py) | exists | no Python imports |
| Count the 220-demonstration set per move and per recording batch | [`scripts/build_ws220.py`](../scripts/build_ws220.py) | exists | no Python imports |
| Turn the operator's notes from an arm test into the yaml a model is scored from | [`scripts/notes_to_yaml.py`](../scripts/notes_to_yaml.py) | exists | no Python imports |
| Cut the site's videos and posters from the recordings and record their size and timing | [`scripts/make_clips.py`](../scripts/make_clips.py) | exists | no Python imports |
| One frame from each of the five cameras at the same instant | [`scripts/make_cams.py`](../scripts/make_cams.py) | exists | no Python imports |
| Label the photo of the rig | [`scripts/annotate_setup.py`](../scripts/annotate_setup.py) | exists | no Python imports |
| Run the whole path from notes to a rebuilt, published site with the checks between | [`scripts/update_site.py`](../scripts/update_site.py) | exists | no Python imports |
| Publish checkpoints and robot sessions to Hugging Face | [`scripts/upload_hf.py`](../scripts/upload_hf.py) | exists | no Python imports |
| Catch glued words and leaked private paths in the built pages | [`scripts/check_text.py`](../scripts/check_text.py) | exists | no Python imports |
| Screenshot the built site in light and dark, desktop and phone width, and report console errors and sideways scroll | [`scripts/shoot.mjs`](../scripts/shoot.mjs) | exists | not scanned: no Python code |
| Compiled Python cache, tracked by mistake | [`scripts/__pycache__`](../scripts/__pycache__) | exists | not scanned: no Python code |

## Seen but not built

- A check in the deploy workflow that the built pages pass `scripts/check_text.py`. Seen 2026-11-28 while documenting the build: the workflow builds and publishes without it. No decision yet.
