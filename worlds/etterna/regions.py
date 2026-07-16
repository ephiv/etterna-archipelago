from __future__ import annotations

from BaseClasses import Region

from .locations import EtternaLocation, HARD_LOCATIONS, LOCATION_GROUPS, LOCATION_NAME_TO_ID

VETERAN_REGIONS = {"Veteran Packs", "Elite Packs", "Legend Packs"}

REGION_EXITS = {
    "Menu": ["Profile Setup", "Beginner Packs", "Modifiers", "Community Packs", "Daily Challenges", "Replay Lab"],
    "Beginner Packs": ["Standard Packs", "Skillsets"],
    "Standard Packs": ["Advanced Packs"],
    "Advanced Packs": ["Expert Packs"],
    "Expert Packs": ["Challenge Packs", "Marathon"],
    "Challenge Packs": ["Veteran Packs", "Marathon"],
    "Veteran Packs": ["Elite Packs", "Marathon"],
    "Elite Packs": ["Legend Packs", "Marathon"],
    "Legend Packs": ["Marathon"],
    "Skillsets": ["Marathon"],
    "Modifiers": ["Marathon"],
    "Marathon": [],
}


def create_regions(world) -> None:
    regions = {}
    for region_name, location_names in LOCATION_GROUPS.items():
        if region_name in VETERAN_REGIONS and not world.options.include_veteran_checks.value:
            continue
        region = Region(region_name, world.player, world.multiworld)
        for location_name in location_names:
            region.locations.append(EtternaLocation(world.player, location_name, LOCATION_NAME_TO_ID[location_name], region))
        regions[region_name] = region
        world.multiworld.regions.append(region)

    if world.options.include_hard_checks.value:
        challenge = regions["Legend Packs"] if world.options.include_veteran_checks.value else regions["Challenge Packs"]
        for location_name in HARD_LOCATIONS:
            challenge.locations.append(EtternaLocation(world.player, location_name, LOCATION_NAME_TO_ID[location_name], challenge))

    for source, targets in REGION_EXITS.items():
        if source not in regions:
            continue
        for target in targets:
            if target in regions:
                regions[source].connect(regions[target])
