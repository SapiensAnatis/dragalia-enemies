"""
Parses the data produced by cargo_query.py into more usable JSON.
"""

import os.path
import json
import materials
import crests

IGNORED_ITEM_TYPES = ["Weapon"]

TYPO_ADJUSTMENTS = {
    "wind Orb": "Wind Orb",
    "Papier-Mâché": "Papier-mâché",
    "Tiny Dragonatas": "Tiny Dragoñatas",
    "\\&quot;A Knight's Dream\\&quot; (Axe's Boon)": "\"A Knight's Dream\" (Axe's Boon)",
    "An Unfreezing Flower (Axe's  Boon)": "An Unfreezing Flower (Axe's Boon)"
}

WORKING_DIR = os.path.dirname(os.path.realpath(__file__))


def process_drop(drop):
    """
    Substitute a drop with its entity ID in place of its name.
    """

    drop["Item"] = TYPO_ADJUSTMENTS.get(drop["Item"], drop["Item"])

    try:
        if drop["ItemType"] == "Material":
            drop["Item"] = materials.name_map[drop["Item"]]
            return drop
        elif drop["ItemType"] == "Wyrmprint":
            drop["Item"] = crests.name_map[drop["Item"]]
            return drop
        elif drop["ItemType"] in IGNORED_ITEM_TYPES:
            return None
        else:
            return drop
    except KeyError as exc:
        raise ValueError("Failed to process row", drop) from exc


def cargo_parse(query_row):
    """
    For a row in the drops table, substitute its name values with material/wyrmprint ids.
    Does not currently substitute some misc resource drops with ID values.
    """
    result = {}

    for drop in query_row:
        drop = process_drop(drop)
        if drop is None:
            continue

        quest_id = int(drop["QuestId"])

        if quest_id not in result:
            result[quest_id] = {
                "_QuestId": quest_id,
                "_Material": set(),
                "_Wyrmprint": set(),
                "_Gift": set(),
                "_Consumable": set(),
                "_Resource": set()
            }

        result[quest_id]["_" + drop["ItemType"]].update([drop["Item"]])

    return result


def set_default(obj):
    """
    Hack to serialize set objects.
    """
    if isinstance(obj, set):
        return sorted(obj)
    raise TypeError


if __name__ == "__main__":
    query = []
    with open(os.path.join(WORKING_DIR, "cargo_query.json"), "r", encoding="utf-8") as f:
        query = json.load(f)

    processed = cargo_parse(query)

    with open(os.path.join(WORKING_DIR, "cargo_query_proc.json"), "w", encoding="utf-8") as f:
        json.dump(list(processed.values()), f, default=set_default)
