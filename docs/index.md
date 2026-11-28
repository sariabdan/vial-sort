# Documentation reading index

[Project context](PROJECT_CONTEXT.md) owns the repository map, build commands
and project choices. [Task routes](../AGENTS.md) name the guides to read before
each action.

## Current documentation

- [Website record](topics/website/website.md): how the site is built, where its numbers come from, its page conventions, how it is published and its known defects.
- [Lab notes](experiments/experiments.md): the dated records of arm tests and retrains, and what they lack as experiment records.
- [Moving the project's code here](topics/code-migration/code-migration.md): the plan for bringing the training, evaluation and robot code into this repository. A working document; deleted when the move has landed.
- [Capability map](CAPABILITY_MAP.md): what each script does and its state.
- [Open work](open/OPEN.md): routes to unfinished owners.
- [Worklog](worklog.md): append-only chronology.
- [Home source](topics/home/index.md): the landing page of the documentation site.

## Where a new document goes

| Subject | Home |
|---|---|
| A fact about the website: a page, a component, a convention, the pipeline | [Website record](topics/website/website.md); split it into a named file beside it when a part grows |
| A new subject, such as training or the robot runtime once their code is here | `docs/topics/<topic>/<topic>.md` |
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
