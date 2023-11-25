"""
Parses the data produced by cargo_query.py into more usable JSON.
"""

import os.path
import json
from typing import Any, Optional
from dataclasses import dataclass
import materials
import crests
import lookups
import custom_tables


WORKING_DIR = os.path.dirname(os.path.realpath(__file__))


@dataclass
class Entity:
    """
    Class for entities to be dropped.
    """
    _Id: int
    _EntityType: str
    _Comment: str
    _Quantity: Optional[float]

    def __hash__(self) -> int:
        return hash(f"{self._Id}{self._EntityType}")

    def __init__(self, drop: Any):
        self.__initialize_idtype(drop)
        self.__initialize_quantity(drop)

    def __initialize_idtype(self, drop: dict):
        drop_type = drop["ItemType"]
        drop_value = drop["Item"]

        if drop_type == "Material" or drop_type == "Wyrmprint":
            self._Id = drop_value
            self._EntityType = drop_type
        elif drop_type == "Resource":
            self._Id = 0
            if drop_value == "Eldwater":
                self._EntityType = "Dew"
            else:
                self._EntityType = drop_value
        elif drop_type == "Gift":
            self._Id = lookups.GIFT_LOOKUP[drop_value]
            self._EntityType = "DragonGift"
        elif drop_type == "Consumable":
            match drop_value:
                case "Summon Voucher":
                    self._Id = 10101  # Single summon voucher
                    self._EntityType = "SummonTicket"
                case "Exquisite Honey":
                    self._Id = 100603
                    self._EntityType = "Item"
                case "Blessed Ethon Ashes":
                    self._Id = 100702
                    self._EntityType = "Item"
            self._Comment = drop_value
        else:
            raise ValueError(f"Unhandled drop type: {drop_type}")

    def __initialize_quantity(self, drop: dict):
        drop_type = drop["ItemType"]

        if drop.get("ExactDrop", None):
            self._Quantity = int(drop["ExactDrop"])

        self._Comment = drop.get("Comment", None)

        if drop_type == "Wyrmprint":
            self._Quantity = 0.1

        if drop_type == "Material":
            self._Quantity = 50

        if (self._Comment and "Boon" in self._Comment):
            self._Quantity = 5

        if drop_type == "Gift":
            self._Quantity = 1

        if drop_type == "Consumable":
            self._Quantity = 5

        if self._Quantity is None:
            raise ValueError("Missing quantity")


def process_drop(drop):
    """
    Substitute a drop with its entity ID in place of its name. Also add a comment
    """

    drop["Item"] = lookups.TYPO_ADJUSTMENTS.get(drop["Item"], drop["Item"])

    try:
        if drop["ItemType"] == "Material":
            if drop["Item"] not in materials.name_map:
                print("Failed to find material", drop["Item"])
                return None

            drop["Comment"] = drop["Item"]
            drop["Item"] = materials.name_map[drop["Item"]]
            return drop
        elif drop["ItemType"] == "Wyrmprint":
            drop["Comment"] = drop["Item"]
            drop["Item"] = crests.name_map[drop["Item"]]
            return drop
        elif drop["ItemType"] == "Consumable":
            drop["Comment"] = drop["Item"]
            return drop
        elif drop["ItemType"] == "Resource":
            drop["Comment"] = drop["Item"]
            return drop
        elif drop["ItemType"] == "Gift":
            drop["Comment"] = drop["Item"]
            return drop
        elif drop["ItemType"] in lookups.IGNORED_ITEM_TYPES:
            return None
        else:
            return drop
    except KeyError as exc:
        raise ValueError("Failed to process row", drop) from exc


def initialize_quest(result: dict[int, dict[str, Any]], quest_id: int):
    if quest_id not in result:
        result[quest_id] = {
            "_QuestId": quest_id,
            "_Rupies": 250_000,
            "_Mana": 10_000,
            "_Drops": set(),
        }


def add_to_result(result: dict, drop, quest_id):
    entity = Entity(drop)
    result[quest_id]["_Drops"].add(entity)


def cargo_parse(query_row):
    """
    For a row in the drops table, substitute its name values with material/wyrmprint ids.
    Does not currently substitute some misc resource drops with ID values.
    """
    result = {}

    for drop in query_row:
        quest_id = int(drop["QuestId"])
        initialize_quest(result, quest_id)

        drop = process_drop(drop)
        if drop is None:
            continue

        add_to_result(result, drop, quest_id)

        if (quest_id in lookups.QUEST_ALT_IDS):
            print("Copying drops to alias", quest_id)

            alt_id = lookups.QUEST_ALT_IDS[quest_id]
            initialize_quest(result, alt_id)
            add_to_result(result, drop, alt_id)

    # Insert additional drops
    for quest_id, mats in lookups.QUEST_ADDED_MATS.items():
        print("Adding extra mats to", quest_id)

        initialize_quest(result, quest_id)

        entities = [Entity({
            "ItemType": "Material",
            "Item": materials.name_map[m],
            "Comment": m
        }) for m in mats]

        result[quest_id]["_Drops"].update(entities)

    for _, quest in result.items():
        quest["_Drops"] = sorted(
            quest["_Drops"], key=lambda e: (e._EntityType, e._Id))

    return result


def set_default(obj):
    """
    Hack to serialize set objects.
    """
    if isinstance(obj, set):
        return list(obj)

    if isinstance(obj, Entity):
        return obj.__dict__


if __name__ == "__main__":
    query = []
    with open(os.path.join(WORKING_DIR, "cargo_query.json"), "r", encoding="utf-8") as f:
        query = json.load(f)

    processed = cargo_parse(query)

    custom_tables.apply_custom_tables(processed)

    result_list = sorted(processed.values(),
                         key=lambda quest: quest["_QuestId"])

    with open(os.path.join(WORKING_DIR, "cargo_query_proc.json"), "w", encoding="utf-8") as f:
        json.dump(result_list, f, default=set_default, indent=4)
