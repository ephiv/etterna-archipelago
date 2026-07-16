# Etterna APWorld status report

## Completion estimate

- APWorld content model: 86% complete.
- Overall playable Etterna integration: 53% complete.

The world now covers every roadmap category with concrete locations and items, including optional veteran tiers for 23-35 MSD play plus community, daily, profile, and replay-lab content, but the project is not 100% done because it still needs validation inside a supported Archipelago release, Etterna-facing check reporting, and playtesting.

## What was expanded

- Locations now cover setup/profile tasks, profile setup, beginner through legend pack progression, community pack goals, daily challenge goals, replay improvement goals, grade goals, wife percent targets, meter/MSD milestones, rate mod checks, skillset milestones, modifier checks, marathon setlists, endgame gauntlets, optional hard checks, and the finale.
- Items now cover pack tier unlocks, veteran MSD licenses, community/daily/replay access, score tracking, modifier unlocks, skillset licenses, Goal Fragments, Finale Access, Progressive Setlist Length, quality-of-life items, cosmetic filler, and opt-in traps.
- Logic now gates setup/reporting regions, pack regions, challenge progression, marathon access, strict judgment checks, rate checks, modifier checks, skillset milestones, setlist length checks, and the finale.

## Remaining work

1. Test world generation inside the target Archipelago version instead of only checking Python syntax and archive shape.
2. Build or document the Etterna-side reporting path: client, tracker, Lua/overlay helper, or manual workflow.
3. Playtest sample seeds with beginner, standard, advanced, expert, challenge, and marathon goals.
4. Tune item counts, filler density, trap chance defaults, and goal fragment requirements based on playtest feedback.
5. Freeze IDs only after the location and item list is accepted as release-ready.
