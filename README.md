# Etterna Archipelago

A standalone Archipelago `.apworld` implementation for **Etterna**, designed as a stable manual/overlay-friendly world for the open-source rhythm game.

This first version intentionally uses an APQuest-inspired, self-contained world structure instead of patching Etterna directly. The player reports Etterna achievements (grades, clear counts, packs, and skillset milestones) through an external client or manual tracker while Archipelago controls progression with gameplay goals and unlock items.

## Build

```bash
python tools/build_apworld.py
```

The packaged world is written to `dist/etterna.apworld`.

## Status and roadmap

This is not a complete Etterna client integration yet. It is the first stable `.apworld` scaffold and package. See [`docs/roadmap.md`](docs/roadmap.md) for planned locations, planned items, and release criteria.

A current completion estimate and remaining-work breakdown are tracked in [`docs/status_report.md`](docs/status_report.md).

Terminology for charts, meter checks, and packs is defined in [`docs/glossary.md`](docs/glossary.md).

Expected behavior for fresh Etterna installs with no packs is documented in [`docs/new_install_behavior.md`](docs/new_install_behavior.md).

Veteran difficulty support for 23-35 MSD play is described in [`docs/veteran_difficulties.md`](docs/veteran_difficulties.md).

APWorld validation and client-testing plans are documented in [`docs/testing_plan.md`](docs/testing_plan.md).

## World concept

Etterna progression is split into unlocks for play modes, judgments, pack tiers, rate mods, skillsets, and endgame stamina. Checks are stable achievement-style locations such as clearing packs, earning grades, passing higher meter charts, and reaching skillset milestones.

The default goal is to collect enough **Goal Fragments** and then complete **The Etterna Finale**.
