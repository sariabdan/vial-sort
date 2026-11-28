# Review of the documentation by a person

No person has read these records. They were written on 2026-11-28 by AI agents (Claude) from the files in this repository, and checked only by the documentation build and lint, which test links and structure, not facts. The project owner decided the same day that Sari Abdan reviews them.

Until a record is reviewed, treat it as a careful summary of the repository's files, not as confirmed project knowledge.

## What to review

| Record | What a reviewer who knows the project should check |
|---|---|
| [Task and rig](../topics/task-and-rig/task-and-rig.md) | The arm, the racks and slots, the camera names and positions, the earlier rigs |
| [Demonstrations](../topics/demonstrations/demonstrations.md) | The two sets, the batches, the coverage tables, the mapping of local dataset names to published ones, which is inferred |
| [Models](../topics/models/models.md) | Every model's origin, data, cameras and settings; that "base12k" is Mango Rice, which is inferred |
| [Training](../topics/training/training.md) | The runs, the cluster retrains, the quantile pinning, what each probe tests and found |
| [Evaluation](../topics/evaluation/evaluation.md) | How a session is really run, the scoring rules, the 12-move gate, the operator's rule of 24 November |
| [Results](../topics/results/results.md) | That the table matches what was observed at the robot |
| [Lab notes](../experiments/experiments.md) | That the four notes survived their move unchanged in meaning |
| [Website](../topics/website/website.md) | The pipeline steps and the publishing description |
| [Moving the code here](../topics/code-migration/code-migration.md) | Whether the breakdown fits the code as it is on the workstation |

## What the review should settle

- Each record's sections "Where sources disagree" and "Not verified": for every row, which source is right, or the missing fact.
- The [known defects](../topics/website/website.md#known-defects) and the [names that need a decision](../development/conventions.md#named-in-conflicting-ways-a-decision-is-owed), for those that need someone who knows the rig or the sessions.
- Anything a record states that is wrong, missing or misleading. The agents could only read what is in this repository; they had no recordings, logs or code.

## Recording the review

When a record has been read and corrected, add a line to the [worklog](../worklog.md) naming the record, the reviewer and the date, and remove the record from the table above. When the table is empty, this document and its line in [open work](OPEN.md) are deleted.
