# Etterna APWorld testing plan

## Short answer

Yes. The APWorld should be tested in layers: package loading, generation, option coverage, spoiler/log sanity, manual playthrough reporting, and eventually a real Etterna client. Archipelago Launcher is enough to test loading, generation, and manual tracker workflows. A dedicated client is not required for the first APWorld validation pass, but it is required for a polished non-manual release.

## Phase 1: package and launcher smoke test

Use this phase to confirm the `.apworld` is structurally loadable by Archipelago.

1. Build or copy `dist/etterna.apworld` into Archipelago's custom worlds folder.
2. Start Archipelago Launcher.
3. Confirm that Etterna appears as an available game/world.
4. Generate a one-player Etterna seed with default options.
5. Generate additional seeds with `include_hard_checks` and `include_veteran_checks` enabled.
6. Confirm generation completes without missing item, missing location, or unreachable-region errors.

## Phase 2: option matrix generation

Generate a small matrix of seeds to catch option-specific mistakes:

- Default options.
- `include_hard_checks: true`.
- `include_veteran_checks: true`.
- Both hard and veteran checks enabled.
- `starting_pack_tier: standard`.
- Low, default, and high `goal_fragments_required` values.
- Trap chance at 0, default, and 100.

For each seed, inspect the generated output and spoiler/log data for item-count balance, reachable completion, and sensible filler density.

## Phase 3: manual tracker playtest

Before a dedicated client exists, test with a manual tracker or manual `/send` workflow:

1. Install a known Etterna pack set.
2. Pick a documented preset that assigns packs/charts to Beginner, Standard, Advanced, Expert, Challenge, and optional Veteran/Elite/Legend tiers.
3. Start a generated Etterna slot in Archipelago.
4. Play Etterna normally.
5. Manually report locations as checks are completed.
6. Confirm received items unlock later checks according to the APWorld rules.
7. Complete the finale condition and verify Archipelago marks the slot finished.

## Phase 4: multiworld compatibility

After one-player generation works, test Etterna inside mixed multiworlds:

- Etterna plus one established Archipelago game.
- Etterna plus multiple established games.
- Two Etterna players with different options.
- One Etterna player with veteran checks enabled and one without.

The goal is to catch itempool, slot-data, and filler/trap behavior issues that do not appear in solo tests.

## Phase 5: client plan

A dedicated Etterna client should be created after the APWorld rules and location list settle. The client should not be required to validate the APWorld scaffold, but it is the correct long-term path for a good player experience.

The client should eventually:

- Detect installed packs and selected preset metadata.
- Read Etterna scores/profile data or consume an exported score file.
- Classify chart clears, grades, wife percent, MSD thresholds, pack clears, replay improvements, and setlist goals.
- Connect to Archipelago and report completed locations automatically.
- Validate preflight requirements, especially zero eligible packs.
- Display received items and currently unlocked Etterna goals.

## Phase 6: release gates

Do not call the APWorld release-ready until:

1. Launcher loading is confirmed.
2. Solo generation works for the option matrix.
3. Mixed multiworld generation works.
4. Manual playthrough completion is confirmed at least once.
5. Veteran-check generation is confirmed separately.
6. The no-pack preflight story is either implemented in a client or documented clearly for manual players.
7. Location and item IDs are frozen.
