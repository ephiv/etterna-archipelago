# Etterna APWorld implementation plan

1. Use APQuest as the structural model: small world package, explicit `items.py`, `locations.py`, `regions.py`, `rules.py`, and options.
2. Keep the first release stable by avoiding Etterna binary patches. Treat Etterna checks as achievements that a client, Lua overlay, or manual tracker can report.
3. Model progression around rhythm-game concepts: pack tiers, rate mods, judgments, skillsets, marathon play, and a final goal.
4. Package the world as `etterna.apworld`, a zip-compatible archive that Archipelago can load from its custom worlds folder.
5. Validate syntax and package contents in CI or locally before publishing releases.
