"""
Parses the data produced by cargo_query.py into more usable JSON.
"""

import os.path
import json
import materials
import crests
from dataclasses import dataclass

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
    300210101: 301070103,  # Smoldering Manticore Strike
    208120101: 208310101,  # Seeking the Unknown
    208120102: 208310102,  # Beyond Darkness
    208060201: 208310301,  # The Crawling Nightmare: Beginner
    208060202: 208310302,  # The Crawling Nightmare: Standard
    208060203: 208310303,  # The Crawling Nightmare: Expert
    208120401: 208310401,  # It Prowls the Endless Dark...
    208120501: 208310501,  # Chaos's Calling: Expert
    208120502: 208310502,  # Chaos's Calling: Master
    208120601: 208310601,  # Chaos's Calling: Nightmare
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

QUEST_ADDED_MATS = {
    # The Consummate Creator
    100260108: DRAGON_AUG_MATERIALS,
    100260208: DRAGON_AUG_MATERIALS,
    100260308: DRAGON_AUG_MATERIALS,
    # Legend quests
    # Volk
    225010101: DRAGON_AUG_MATERIALS,
    225011101: DRAGON_AUG_MATERIALS,
    # Kai Yan
    225020101: DRAGON_AUG_MATERIALS,
    225021101: DRAGON_AUG_MATERIALS,
    # Ciella
    225030101: DRAGON_AUG_MATERIALS,
    225031101: DRAGON_AUG_MATERIALS,
    # Ayaha & Otoha
    225040101: DRAGON_AUG_MATERIALS,
    225041101: DRAGON_AUG_MATERIALS,
    # Tartarus
    225050101: DRAGON_AUG_MATERIALS,
    225051101: DRAGON_AUG_MATERIALS,
    # Jaldabaoth
    232010101: DRAGON_AUG_MATERIALS,
    232011101: DRAGON_AUG_MATERIALS,
    # Iblis
    232020101: DRAGON_AUG_MATERIALS,
    232021101: DRAGON_AUG_MATERIALS,
    # Surtr
    232030101: DRAGON_AUG_MATERIALS,
    232031101: DRAGON_AUG_MATERIALS,
    # Asura
    232040101: DRAGON_AUG_MATERIALS,
    232041101: DRAGON_AUG_MATERIALS,
    # Lilith
    232050101: DRAGON_AUG_MATERIALS,
    232051101: DRAGON_AUG_MATERIALS,
    # Morsayati's Reckoning
    226010101: DRAGON_AUG_MATERIALS,
    226011101: DRAGON_AUG_MATERIALS,
    # Manacaster tablets
    # Battle in the Dornith Mountains Standard
    211040102: MANACASTER_TABLET_MATERIALS,
    # Battle at the Wartarch Ruins Standard
    211050102: MANACASTER_TABLET_MATERIALS,
    # Lambent Ghost Strike
    301020103: LAMBENT_GHOST_MATERIALS}

GIFT_LOOKUP = {
    "Dragonyule Cake": 30002,
    "Four-Leaf Clover": 30001
}

WORKING_DIR = os.path.dirname(os.path.realpath(__file__))


@dataclass
class Entity:
    """
    Class for entities to be dropped.
    """
    _Id: int
    _EntityType: str
    _Comment: str
    _Quantity: int = None

    def __hash__(self) -> int:
        return hash(f"{self._Id}{self._EntityType}")

    def __init__(self, drop: any):
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
            self._Id = GIFT_LOOKUP[drop_value]
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

        else:
            raise ValueError(f"Unhandled drop type: {drop_type}")

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
            raise Exception("Missing quantity")


def process_drop(drop):
    """
    Substitute a drop with its entity ID in place of its name.
    """

    drop["Item"] = TYPO_ADJUSTMENTS.get(drop["Item"], drop["Item"])

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
        elif drop["ItemType"] in IGNORED_ITEM_TYPES:
            return None
        else:
            return drop
    except KeyError as exc:
        raise ValueError("Failed to process row", drop) from exc


def add_to_result(result: set, drop, quest_id):
    if quest_id not in result and quest_id is not None:
        result[quest_id] = {
            "_QuestId": quest_id,
            "_Drops": set()
        }

    entity = Entity(drop)

    result[quest_id]["_Drops"].add(entity)


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
        add_to_result(result, drop, quest_id)

        if (quest_id in QUEST_ALT_IDS):
            print("Copying drops to alias", quest_id)
            alt_id = QUEST_ALT_IDS[quest_id]
            add_to_result(result, drop, alt_id)

    # Insert additional drops
    for quest_id, mats in QUEST_ADDED_MATS.items():
        print("Adding extra mats to", quest_id)

        if quest_id not in result:
            result[quest_id] = {
                "_QuestId": quest_id,
                "_Drops": set()
            }

        entities = [Entity({
            "ItemType": "Material",
            "Item": m,
        }) for m in mats]

        result[quest_id]["_Drops"].update(entities)

    for _, quest in result.items():
        quest["_Drops"] = sorted(
            quest["_Drops"], key=lambda e: (e._EntityType, e._Id))

    return sorted(result.values(), key=lambda quest: quest["_QuestId"])


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

    with open(os.path.join(WORKING_DIR, "cargo_query_proc.json"), "w", encoding="utf-8") as f:
        json.dump(processed, f, default=set_default, indent=True)
