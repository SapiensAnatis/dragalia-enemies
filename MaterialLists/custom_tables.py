from typing import Optional

from classes import ParsedQuest


class CustomTable:
    """
    Defines a custom drop table for a quest.
    """
    quest_id: int
    rupies: Optional[int]
    mana: Optional[int]
    drops: Optional[dict[str, float]]

    def __init__(self, quest_id: int, rupies: Optional[int] = None, mana: Optional[int] = None, drops: Optional[dict[str, float]] = None):
        self.quest_id = quest_id
        self.rupies = rupies
        self.mana = mana
        self.drops = drops


custom_tables = [
    # ATF beginner
    CustomTable(quest_id=202060101, rupies=300000),
    # ATF standard
    CustomTable(quest_id=202060102, rupies=500000),
    # ATF expert
    CustomTable(quest_id=202060103, rupies=750000),
    # ATF master
    CustomTable(quest_id=202060104, rupies=1000000)
]


def apply_custom_tables(cargo_parsed: dict[int, ParsedQuest]):
    for t in custom_tables:
        entry = cargo_parsed.get(t.quest_id, None)
        if entry is not None:
            if t.rupies is not None:
                entry._Rupies = t.rupies
