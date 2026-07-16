# Etterna APWorld roadmap

## Current status

This repository is not a finished Etterna integration yet. It is a stable first `.apworld` scaffold that can generate and package an Archipelago world, but it still needs a real Etterna-facing client or tracker before it should be considered a complete release.

The first milestone intentionally uses achievement-style checks so the world can remain stable while client integration is designed separately.

## Planned locations

The next location expansion should add checks in groups that map cleanly to Etterna play without requiring binary patching:

- Profile and setup checks: profile sync, offset calibration, first successful score upload, first replay saved, favorites setup, input consistency, and personal best setup.
- Pack progression checks: clear 1/3/5 packs in each tier, clear curated community pack groups, tournament packs, stamina/technical-focused packs, and shuffled daily goals.
- Grade checks: earn A, AA, AAA, and AAAA counts at beginner, standard, advanced, and expert tiers.
- Wife percent checks: hit target wife percentages across multiple difficulty bands.
- Meter and MSD checks: pass representative charts at 6, 8, 10, 12, 14, 16, 18, 20, 22+, and optional veteran 23/25/30/35 MSD thresholds.
- Rate mod checks: pass qualifying charts at 0.9x, 1.0x, 1.1x, 1.2x, and higher rate targets.
- Skillset checks: reach tiered stream, jumpstream, handstream, stamina, jack, chordjack, and technical milestones.
- Marathon checks: clear 10, 20, 30, and 45 minute setlists, plus an endgame gauntlet.
- Optional challenge checks: no-mine clears, low-miss clears, sightread clears, replay review, replay improvement, offset-fix reclears, and failed-chart reclears.

## Planned items

The next item expansion should make progression feel more like gradually unlocking an Etterna session:

- Pack tier unlocks and activity unlocks: Beginner, Standard, Advanced, Expert, Challenge, Marathon, Veteran, Elite, Legend, Community, Daily, Replay Lab, and Score Tracker access.
- Modifier unlocks: rate mods, mirror, shuffle, no mines, CMod/MMod, judge difficulty, and fail type options.
- Skillset unlocks: stream, jumpstream, handstream, stamina, jack, chordjack, technical, chordstream, and veteran MSD licenses.
- Goal items: Goal Fragments, Finale Access, and optional Progressive Setlist Length.
- Quality-of-life useful items: practice mode, replay review, offset helper, wife graph, song search, and favorites wheel.
- Filler items: cosmetic note/toast items, music wheel spins, judgment font swaps, and harmless theme toggles.
- Trap items: minefield, sudden rate change, mirror forced, visual clutter, and fake offset nudge traps for clients that opt in.

## Release criteria

A release should be considered finished only after the following are true:

1. The `.apworld` can generate successfully inside a supported Archipelago release.
2. A client, tracker, or documented manual workflow can report every location reliably.
3. Logic has been playtested for early, midgame, and endgame seeds.
4. Location and item IDs are frozen for backwards compatibility.
5. The packaged `.apworld` is produced by the build script and verified before release.
