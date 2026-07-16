# New Etterna install behavior

## Short answer

Loading `etterna.apworld` into Archipelago does not install Etterna songs, packs, charts, or a gameplay client. On a fresh Etterna install with no packs, the APWorld can define the Archipelago slot, items, locations, and logic, but most gameplay checks cannot be completed until eligible Etterna content and a check-reporting workflow exist.

## What should happen

1. Archipelago should discover the Etterna world after the `.apworld` is placed in the appropriate custom worlds folder.
2. The generator should be able to create an Etterna slot using the world's items, locations, options, and rules.
3. The generated slot will contain checks such as chart clears, pack clears, grade goals, meter goals, skillset milestones, and finale goals.
4. A fresh Etterna install will not automatically satisfy those checks because the APWorld does not bundle or download song packs.
5. The player must install eligible Etterna packs and use a client, tracker, or manual workflow to report completed checks to Archipelago.

## What does not happen yet

- The APWorld does not modify Etterna.
- The APWorld does not install songs or copyrighted/community packs.
- The APWorld does not classify local song folders automatically.
- The APWorld does not currently provide a bundled Etterna client that reads local scores and reports locations.
- The APWorld does not make no-pack installs playable beyond non-gameplay/manual setup checks.

## Recommended behavior for no-pack installs

Until a real Etterna client or preset pack manifest exists, a no-pack install should be treated as not ready for normal play. The user should see setup documentation telling them to install eligible packs, choose or create a pack-tier preset, and connect a reporting method before attempting a seed.

For future client work, the desired behavior is a preflight check that detects zero eligible packs and reports a clear error such as: `No eligible Etterna packs were found. Install packs or select a pack preset before starting this Archipelago slot.`
