# Etterna APWorld glossary

## Chart

A chart is one playable steps file/difficulty for a song. In Etterna terms, a single song can have multiple charts because it can include multiple difficulties or step authors. APWorld location text such as `Clear 5 Beginner Charts` counts individual playable chart clears, not whole song folders.

## Meter chart

A meter chart is a chart whose in-game difficulty meter is at or above the named threshold. For example, `Pass a 14 Meter Chart` means passing any chart that Etterna displays as meter 14 or higher. The check is based on Etterna's chart difficulty/meter value, not the song title, pack name, or Archipelago item count.

## Pack

A pack is a collection of songs/charts installed in Etterna, normally represented by a song group folder or a curated collection from the Etterna/community ecosystem. Packs do not belong to the APWorld itself: the APWorld only defines checks and logic around pack clear goals. The player, client, tracker, or event ruleset must decide which local Etterna song groups count as eligible packs.

A pack clear should mean clearing a defined completion target for that pack, such as passing every required chart in the pack, passing one chart per song, or meeting a documented percentage threshold. The exact completion rule should be fixed by the release preset or tournament/session settings so every player in a seed uses the same interpretation.

## Beginner, Standard, Advanced, Expert, and Challenge packs

The pack tiers are APWorld progression buckets, not hardcoded ownership of specific copyrighted song packs. A pack should be assigned to a tier by the release preset or tracker configuration according to its expected difficulty range and intended progression role:

- Beginner: entry-level packs focused on easier charts and onboarding clears.
- Standard: comfortable normal-play packs that require basic consistency.
- Advanced: packs with harder timing, denser patterns, or higher meter requirements.
- Expert: high-skill packs requiring strong Etterna fundamentals and higher-grade play.
- Challenge: endgame packs for very high meters, strict goals, or specialized skillsets.

## Beginner Chart and Expert Chart

A Beginner Chart or Expert Chart is a chart assigned to that progression tier by meter, pack tier, or preset metadata. The APWorld does not currently inspect Etterna files to classify charts automatically. Until a client/tracker is implemented, the session rules should define the tier boundaries explicitly.

A practical default mapping for manual playtesting is:

- Beginner Chart: meter 1-8.
- Standard Chart: meter 9-12.
- Advanced Chart: meter 13-16.
- Expert Chart: meter 17-20.
- Challenge Chart: meter 21-22.
- Veteran Chart: 23-27 MSD.
- Elite Chart: 28-31 MSD.
- Legend Chart: 32+ MSD.

These ranges are defaults for APWorld check interpretation, not changes to Etterna's own rating system.
