"""
Parses the data produced by cargo_query.py into more usable JSON.
"""

import os.path
import json
import materials
import crests
import math

IGNORED_ITEM_TYPES = ["Weapon"]

TYPO_ADJUSTMENTS = {
    "wind Orb": "Wind Orb",
    "Papier-Mâché": "Papier-mâché",
    "Tiny Dragonatas": "Tiny Dragoñatas",
    "\\&quot;A Knight's Dream\\&quot; (Axe's Boon)": "\"A Knight's Dream\" (Axe's Boon)",
    "An Unfreezing Flower (Axe's  Boon)": "An Unfreezing Flower (Axe's Boon)"
}

# Some void battles don't appear due to using outdated IDs
# SELECT t._Text, q.* FROM QuestData q
#   JOIN TextLabel t on q._QuestViewName = t._Id
#   WHERE t._Text like '%Shroom Strike%'
#   ORDER BY t._Text, q._Id
QUEST_ALT_IDS = {
    300090101: 301010102,  # Gust Shroom Strike
    300150101: 301010103,  # Scalding Shroom Strike
    300010101: 301010101,  # Wandering Shroom Strike,
    300060101: 301020101,  # Blazing Ghost STrike
    300250101: 301020104,  # Cerulean Ghost Strike
    300190101: 301020103,  # Lambent Ghost Strike
    300100101: 301020102,  # Violet Ghost Strike
    300020101: 301030101,  # Frost Hermit Strike
    300160101: 301030102,  # Twilight Hermit Strike
    300110101: 301040103,  # Amber Golem Strike
    300070101: 301040102,  # Obsidian Golem Strike
    300030101: 301040101,  # Steel Golem Strike
    300170101: 301050101,  # Catoblepas Anemos
    300260101: 301050102,  # Catoblepas Fotia Strike,
    300200101: 301060101,  # Eolian Phantom Strike
    300270101: 301060102,  # Infernal Phantom Strike
    300140101: 301070102,  # Greedy Manticore Strike
    300230101: 301070104,  # Proud Manticore Strike
    300050101: 301070101,  # Raging Manticore Strike
    300210101: 301070103   # Smoldering Manticore Strike
}

DRAGON_AUG_MATERIALS = [119001001, 118001001]
MANACASTER_TABLET_MATERIALS = [202005091]
LAMBENT_GHOST_MATERIALS = [201014001,
                           201014002,
                           202003001,
                           202003002,
                           204006001,
                           204019001,
                           204019002]


WORKING_DIR = os.path.dirname(os.path.realpath(__file__))


def process_drop(drop):
    """
    Substitute a drop with its entity ID in place of its name, and add its quantity
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


def add_to_result(result, drop, quest_id):
    if quest_id not in result:
        result[quest_id] = {
            "_QuestId": quest_id,
            "_Bonuses": [],
        }

    if drop["ItemType"] == "Resource":
        drop["ItemType"] = drop["Item"]
        drop["Item"] = 0

    result[quest_id]["_Bonuses"].append({
        "_EntityType": drop["ItemType"],
        "_Id": drop["Item"],
        "_Quantity": drop["Quantity"]
    })


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

        if drop["ExactDrop"]:
            drop["Quantity"] = int(drop["ExactDrop"])
        elif drop["MaxDrop"] and drop["MinDrop"]:
            drop["Quantity"] = math.ceil((int(drop["MaxDrop"]) +
                                          int(drop["MinDrop"])) / 2)
        else:
            print(f"Warning: could not derive quantity for {drop}")
            drop["Quantity"] = 10 if drop["ItemType"] == "Material" else 10000

        quest_id = int(drop["QuestId"])
        add_to_result(result, drop, quest_id)

        if (quest_id in QUEST_ALT_IDS):
            print("Copying drops to alias", quest_id)
            alt_id = QUEST_ALT_IDS[quest_id]
            add_to_result(result, drop, alt_id)

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
