# Documentation reading index

[Project context](PROJECT_CONTEXT.md) owns the repository map, build commands
and project choices. [Task routes](../AGENTS.md) name the guides to read before
each action.

## Current documentation

- [Task and rig](topics/task-and-rig/task-and-rig.md): the task, the arm, the racks, the slots and the cameras.
- [Demonstrations](topics/demonstrations/demonstrations.md): the recorded demonstration sets, their commands and their coverage.
- [Models](topics/models/models.md): every model, what it started from, what it saw and its settings.
- [Training](topics/training/training.md): the training runs, the retrains and the offline probes.
- [Evaluation](topics/evaluation/evaluation.md): how a rollout is run, noted and scored.
- [Results](topics/results/results.md): every run with its counts and score, as a dated snapshot.
- [Website record](topics/website/website.md): how the site is built, where its numbers come from, its page conventions, how it is published, and its known defects.
- [Lab notes](experiments/experiments.md): the dated records of arm tests and retrains, and what they lack as experiment records.
- [Moving the project's code here](topics/code-migration/code-migration.md): the plan for bringing the training, evaluation and robot code into this repository. A working document; deleted when the move has landed.
- [Capability map](CAPABILITY_MAP.md): what each script does and its state.
- [Open work](open/OPEN.md): routes to unfinished owners.
- [Review by a person](open/human-review.md): no person has read these records yet; who reviews them and what to check.
- [Development conventions](development/conventions.md): the terms that have more than one name, and the names that need a decision.
- [Worklog](worklog.md): append-only chronology.
- [Home source](topics/home/index.md): the landing page of the documentation site.

## Where a new document goes

| Subject | Home |
|---|---|
| A fact about the website: a page, a component, a convention, the pipeline | [Website record](topics/website/website.md); split it into a named file beside it when a part grows |
| A fact about the rig, the data, a model, training, testing or a result | The matching record above |
| A new subject, such as the robot runtime once its code is here | `docs/topics/<topic>/<topic>.md` |
| A term renamed, or named in more than one way | [Development conventions](development/conventions.md#terms) |
| Something owed | One line in [open work](open/OPEN.md), linking the record that owns it |
| What landed and when | [Worklog](worklog.md) |
| A dated arm test or retrain | `docs/experiments/<date>-<subject>/`, listed in [Lab notes](experiments/experiments.md) |

## Shared practices

Read the matching guide in the initialized `.docs-kit` submodule:

| Action | Shared guide |
|---|---|
| Code, performance or execution | `rules/engineering/code.md`, `performance.md`, `execution.md` |
| Delivery, handoffs or Git | `rules/engineering/delivery.md`, `handoffs.md`, `git.md` |
| Writing or changing a record | `rules/records.md` |
| Documentation placement, order of work and lifecycle | `rules/documentation.md` |
| A page for people: new on request, existing kept in step | Focused guides linked from `rules/writing.md` and `rules/maintenance.md` |
| Site authoring, checks, publication and reader changes | Focused guides linked from `rules/maintenance.md` |
