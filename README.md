# Vial sort

The website of the vial-sort project: a low-cost SO-101 arm moves small vials between two racks and a bin, following a command that names the slot to take the vial from and where to put it. The site reports the data, the models, the training and the results.

Live site: https://cognitive-software-labs.github.io/vial-sort/

This repository holds the site, the scripts that build its data, and the project documentation. The training, evaluation and robot code lives in a separate repository for now.

## Run it

Needs Node.js 22.23.4 or later.

```sh
npm install
npm run dev      # http://localhost:4321/vial-sort/
npm run build    # writes dist/
```

Every push to `main` publishes the site to GitHub Pages.

## Before changing anything

- The numbers on the pages come from `src/data/*.json`, which scripts generate. Do not edit those files by hand.
- `docs/PROJECT_CONTEXT.md` has the repository map and every command; `docs/topics/website/website.md` explains how the site is built and its conventions.
- `AGENTS.md` tells coding agents which rule to read before each kind of action. The rules come from the documentation kit in `.docs-kit/`, a Git submodule: run `git submodule update --init` after cloning.
