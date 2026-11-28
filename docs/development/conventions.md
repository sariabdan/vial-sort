# Development conventions

## Scope

This record owns the project's conventions that cut across topics. Today that is one list: the [terms](#terms) that have more than one name, or whose words on the website differ from the names in the data and code. Each term is defined in the record linked beside it; this list defines nothing itself. A rename changes this list first, then every surface: records, website pages, components, scripts and data labels.

## Terms

### One meaning, several names

The term in the first column is the one records and pages use. The words in the last column are the other names it stands for.

| Term | Defined in | Other names it replaces |
|---|---|---|
| Command | [Task and rig, the task](../topics/task-and-rig/task-and-rig.md#the-task) | "prompt" |
| Score | [Evaluation, the score of a run](../topics/evaluation/evaluation.md#the-score-of-a-run) | "total accuracy" in the evaluation record's terms; key `total` in `src/lib/score.ts` |
| Picked up the right vial | [Evaluation, the three outcome stages](../topics/evaluation/evaluation.md#the-three-outcome-stages) | data key `grasped_right` |
| In the asked slot | [Evaluation, the three outcome stages](../topics/evaluation/evaluation.md#the-three-outcome-stages) | data key `released`; outcome `placed` in the operator's notes as parsed by `scripts/notes_to_yaml.py` |
| Picked up, not in the asked slot | [Evaluation, the three outcome stages](../topics/evaluation/evaluation.md#the-three-outcome-stages) | data key `carried` |
| Never picked it up | [Evaluation, the three outcome stages](../topics/evaluation/evaluation.md#the-three-outcome-stages) | data key `no_grasp` |
| Overhead, Across the table, Near eye level, From the side, On the gripper | [Task and rig, the five cameras](../topics/task-and-rig/task-and-rig.md#the-five-cameras) | recording keys `top_down`, `left_top`, `left_bottom`, `right`, `wrist` |

The data keys `released` and `carried` are kept on purpose, "so older data and code keep working" (`scripts/build_data.py`). The recording keys of the cameras are kept because they name the streams in the recorded datasets. Records name a key in code formatting where they mean the key.

### Named in conflicting ways: a decision is owed

Each of these has its own line in [open work](../open/OPEN.md). Until it is decided, records name the meaning they use in full words, as the linked records do.

#### "Held out" means two things

In the glossary (`src/lib/glossary.ts`) and the [evaluation record](../topics/evaluation/evaluation.md#terms) it means rack slots never demonstrated on purpose: slots 2 and 5 are never a source, and slots 2, 4 and 5 never a destination. In `src/data/registry.json` and `src/data/results.json`, "220 minus 8 held out" means 8 demonstrations left out of Isaac 0.5 Expert's training copy and scored offline ([models](../topics/models/models.md)). Needs the owner's decision on which meaning keeps the term and what the other is called.

#### The camera `left_bottom` has two page names

It is "Near eye level" in `CAMERA_NAMES` in `src/lib/site.ts` and "Near table level" on the Data page (`src/pages/datasets.astro`); [task and rig](../topics/task-and-rig/task-and-rig.md#the-five-cameras) records both. Needs someone who knows the rig to say which is right.

#### The third vial colour has three names

It is "dark green" on the Data page, "lime" in `src/components/RackGlyph.astro` and `curation.yaml`, and "green" on the August page ([task and rig, the vials](../topics/task-and-rig/task-and-rig.md#the-vials)). Needs someone who knows the rig to say which is right.
