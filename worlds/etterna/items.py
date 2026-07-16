from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import EtternaWorld

BASE_ID = 557700000

PROGRESSION_ITEMS = {
    "Beginner Pack Access": 0,
    "Standard Pack Access": 1,
    "Advanced Pack Access": 2,
    "Expert Pack Access": 3,
    "Challenge Pack Access": 4,
    "Marathon Pack Access": 5,
    "Veteran Pack Access": 6,
    "Elite Pack Access": 7,
    "Legend Pack Access": 8,
    "Rate Mod Unlock": 9,
    "Mirror Unlock": 10,
    "Shuffle Unlock": 11,
    "No Mines Unlock": 12,
    "CMod/MMod Unlock": 13,
    "Strict Judgment Unlock": 14,
    "Fail Type Options": 15,
    "Stream License": 16,
    "Jumpstream License": 17,
    "Handstream License": 18,
    "Stamina License": 19,
    "Jack License": 20,
    "Chordjack License": 21,
    "Technical License": 22,
    "Chordstream License": 23,
    "Veteran MSD License": 24,
    "Elite MSD License": 25,
    "Legend MSD License": 26,
    "Community Pack Access": 27,
    "Daily Challenge Board": 28,
    "Replay Lab Access": 29,
    "Score Tracker": 30,
    "Finale Access": 31,
    "Progressive Setlist Length": 32,
    "Goal Fragment": 33,
}
USEFUL_ITEMS = {
    "Practice Mode": 80,
    "Replay Review": 81,
    "Offset Helper": 82,
    "Wife Graph": 83,
    "Song Search": 84,
    "Favorites Wheel": 85,
}
FILLER_ITEMS = {
    "Toast Note": 120,
    "Extra Music Wheel Spin": 121,
    "Judgment Font Swap": 122,
    "Theme Toggle": 123,
}
TRAP_ITEMS = {
    "Minefield Trap": 160,
    "Sudden Rate Change Trap": 161,
    "Forced Mirror Trap": 162,
    "Visual Clutter Trap": 163,
    "Fake Offset Nudge Trap": 164,
}

ITEM_NAME_TO_ID = {
    name: BASE_ID + offset
    for table in (PROGRESSION_ITEMS, USEFUL_ITEMS, FILLER_ITEMS, TRAP_ITEMS)
    for name, offset in table.items()
}


class EtternaItem(Item):
    game = "Etterna"


def get_classification(name: str) -> ItemClassification:
    if name in PROGRESSION_ITEMS:
        return ItemClassification.progression
    if name in USEFUL_ITEMS:
        return ItemClassification.useful
    if name in TRAP_ITEMS:
        return ItemClassification.trap
    return ItemClassification.filler


def create_item(world: EtternaWorld, name: str) -> EtternaItem:
    return EtternaItem(name, get_classification(name), ITEM_NAME_TO_ID[name], world.player)


def get_filler_item_name(world: EtternaWorld) -> str:
    if world.random.randint(1, 100) <= world.options.trap_chance.value:
        return world.random.choice(tuple(TRAP_ITEMS))
    return world.random.choice(tuple(FILLER_ITEMS))


def create_itempool(world: EtternaWorld) -> None:
    item_names = [
        "Beginner Pack Access",
        "Standard Pack Access",
        "Advanced Pack Access",
        "Expert Pack Access",
        "Challenge Pack Access",
        "Marathon Pack Access",
        "Veteran Pack Access",
        "Elite Pack Access",
        "Legend Pack Access",
        "Rate Mod Unlock",
        "Mirror Unlock",
        "Shuffle Unlock",
        "No Mines Unlock",
        "CMod/MMod Unlock",
        "Strict Judgment Unlock",
        "Fail Type Options",
        "Stream License",
        "Jumpstream License",
        "Handstream License",
        "Stamina License",
        "Jack License",
        "Chordjack License",
        "Technical License",
        "Chordstream License",
        "Veteran MSD License",
        "Elite MSD License",
        "Legend MSD License",
        "Community Pack Access",
        "Daily Challenge Board",
        "Replay Lab Access",
        "Score Tracker",
        "Finale Access",
        *["Progressive Setlist Length" for _ in range(3)],
        *["Goal Fragment" for _ in range(18)],
        "Practice Mode",
        "Replay Review",
        "Offset Helper",
        "Wife Graph",
        "Song Search",
        "Favorites Wheel",
    ]
    if not world.options.include_veteran_checks.value:
        for veteran_item in (
            "Veteran Pack Access",
            "Elite Pack Access",
            "Legend Pack Access",
            "Veteran MSD License",
            "Elite MSD License",
            "Legend MSD License",
        ):
            item_names.remove(veteran_item)

    if world.options.starting_pack_tier.value >= 1:
        item_names.remove("Beginner Pack Access")
        item_names.remove("Standard Pack Access")
        world.push_precollected(world.create_item("Beginner Pack Access"))
        world.push_precollected(world.create_item("Standard Pack Access"))

    itempool = [world.create_item(name) for name in item_names]
    unfilled = len(world.multiworld.get_unfilled_locations(world.player))
    itempool.extend(world.create_filler() for _ in range(unfilled - len(itempool)))
    world.multiworld.itempool += itempool
