from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules
from .options import EtternaOptions


class EtternaWorld(World):
    """Manual-friendly Archipelago world for Etterna rhythm-game progression."""

    game = "Etterna"
    options_dataclass = EtternaOptions
    options: EtternaOptions
    item_name_to_id = items.ITEM_NAME_TO_ID
    location_name_to_id = locations.LOCATION_NAME_TO_ID
    origin_region_name = "Menu"

    def create_regions(self) -> None:
        regions.create_regions(self)

    def create_items(self) -> None:
        items.create_itempool(self)

    def set_rules(self) -> None:
        rules.set_rules(self)

    def create_item(self, name: str) -> items.EtternaItem:
        return items.create_item(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict("goal_fragments_required", "include_hard_checks", "include_veteran_checks", "starting_pack_tier")
