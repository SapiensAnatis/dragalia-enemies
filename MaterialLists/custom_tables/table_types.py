from typing import Optional
from materials import Material


class CustomTable:
    """
    Defines a custom drop table for a quest.
    """
    quest_id: int
    rupies: Optional[int]
    mana: Optional[int]
    drops: Optional[dict[Material, float]]

    def __init__(self, quest_id: int, rupies: Optional[int] = None, mana: Optional[int] = None, drops: Optional[dict[Material, float]] = None):
        self.quest_id = quest_id
        self.rupies = rupies
        self.mana = mana
        self.drops = drops
