# Veteran difficulty support

## Purpose

Veteran difficulty support extends the Etterna APWorld beyond Challenge-tier play for players who regularly play very high MSD charts, including 23, 25, 30, and 35 MSD goals.

## New optional tier structure

Veteran support is controlled by the `include_veteran_checks` option. When enabled, the world adds three post-Challenge regions:

- Veteran Packs: early post-Challenge content around 23-25 MSD goals.
- Elite Packs: very high-end content around 28-30 MSD goals.
- Legend Packs: extreme content around 32-35 MSD goals and a Legend Gauntlet.

When disabled, those regions and locations are omitted and their dedicated pack/MSD progression items are removed from the generated item pool.

## Interpretation

MSD checks use Etterna's MSD-style chart difficulty expectations for veteran play. For manual playtesting, the intended thresholds are literal minimums: `Pass a 30 MSD Chart` means pass a chart rated 30 MSD or higher by the configured pack/preset/tracker rules.

The APWorld still does not ship charts or packs. Veteran, Elite, and Legend packs must be supplied and tiered by a preset, tracker, client, or session ruleset.
