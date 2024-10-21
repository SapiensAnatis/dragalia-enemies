from materials import Material
from classes import ParsedQuest
from table_types import CustomTable
from imperial_onslaught import create_io_tables


def create_custom_tables() -> list[CustomTable]:
    return [
        # ATF beginner
        CustomTable(quest_id=202060101, rupies=300000),
        # ATF standard
        CustomTable(quest_id=202060102, rupies=500000),
        # ATF expert
        CustomTable(quest_id=202060103, rupies=750000),
        # ATF master
        CustomTable(quest_id=202060104, rupies=1000000),
        *create_io_tables()
    ]


def apply_custom_tables(cargo_parsed: dict[int, ParsedQuest]):
    for table in create_custom_tables():
        entry = cargo_parsed[table.quest_id]

        if table.rupies is not None:
            entry._Rupies = table.rupies

        if table.mana is not None:
            entry._Mana = table.mana

        if table.drops is not None:
            for drop in entry._Drops:
                if drop._EntityType != "Material":
                    continue

                drop._Quantity = table.drops[Material(drop._Id)]
