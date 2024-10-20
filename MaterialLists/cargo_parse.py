"""
Parses the data produced by cargo_query.py into more usable JSON.
"""

import os.path
import json
from classes import Entity, ParsedQuest
from quest_alt_ids import QUEST_ALT_IDS
import materials
import crests
import lookups
import custom_tables
import quest_name

WORKING_DIR = os.path.dirname(os.path.realpath(__file__))


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


def initialize_quest(result: dict[int, ParsedQuest], quest_id: int):
    if quest_id not in result:
        result[quest_id] = ParsedQuest(
            _QuestId=quest_id,
            _Rupies=250_000,
            _Mana=10_000,
            _Drops=set(),
            _Comment=None
        )


def add_to_result(result: dict, drop, quest_id):
    entity = Entity(drop)
    result[quest_id]._Drops.add(entity)


def cargo_parse(query_row):
    """
    For a row in the drops table, substitute its name values with material/wyrmprint ids.
    Does not currently substitute some misc resource drops with ID values.
    """
    result: dict[int, ParsedQuest] = {}

    for drop in query_row:
        quest_id = int(drop["QuestId"])
        initialize_quest(result, quest_id)

        drop = process_drop(drop)
        if drop is None:
            continue

        add_to_result(result, drop, quest_id)

        if (quest_id in QUEST_ALT_IDS):
            print("Copying drops to alias", quest_id)

            alt_id = QUEST_ALT_IDS[quest_id]

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

        result[quest_id]._Drops.update(entities)

    for _, quest in result.items():
        quest._Drops = sorted(
            quest._Drops, key=lambda e: (e._EntityType, e._Id))

    return result


def set_default(obj):
    """
    Hack to serialize set objects.
    """
    if isinstance(obj, set):
        return list(obj)

    if isinstance(obj, Entity):
        return obj.__dict__

    if isinstance(obj, ParsedQuest):
        return obj.__dict__


if __name__ == "__main__":
    query = []
    with open(os.path.join(WORKING_DIR, "cargo_query.json"), "r", encoding="utf-8") as f:
        query = json.load(f)

    processed = cargo_parse(query)

    quest_name.set_quest_names(processed)
    custom_tables.apply_custom_tables(processed)

    result_list = sorted(processed.values(),
                         key=lambda quest: quest._QuestId)

    with open(os.path.join(WORKING_DIR, "cargo_query_proc.json"), "w", encoding="utf-8") as f:
        json.dump(result_list, f, default=set_default, indent=2)

    dawnshard_path = r"C:\Users\jay0\Projects\Dawnshard\DragaliaAPI\DragaliaAPI.Shared\Resources\QuestDrops\QuestDropInfo.json"
    if (os.path.exists(dawnshard_path)):
        with open(dawnshard_path, "w", encoding="utf-8") as f:
            json.dump(result_list, f, default=set_default, indent=2)
