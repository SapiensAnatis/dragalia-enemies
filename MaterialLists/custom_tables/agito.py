from dataclasses import dataclass
from materials import Material
from table_types import CustomTable


@dataclass
class AgitoArgs:
    coop: bool
    t1_material: Material
    t2_material: Material
    t3_material: Material
    tablets: list[Material]


def create_standard_agito_table(quest_id: int, args: AgitoArgs):
    return CustomTable(quest_id=quest_id, rupies=100000, drops={
        Material.CONSECRATED_WATER: 3,
        Material.AMPLIFYING_CRYSTAL: 4,
        Material.FORTIFYING_CRYSTAL: 4,
        args.t1_material: 24 + 18 if args.coop else 18 + 12  # TODO: Survival bonuses
    })


def create_expert_agito_table(quest_id: int, args: AgitoArgs):
    return CustomTable(quest_id=quest_id, rupies=100000, drops={
        Material.CONSECRATED_WATER: 3,
        Material.AMPLIFYING_CRYSTAL: 2,
        Material.AMPLIFYING_GEMSTONE: 2,
        Material.FORTIFYING_CRYSTAL: 2,
        Material.FORTIFYING_GEMSTONE: 2,
        args.t1_material: 12 if args.coop else 9,
        args.t2_material: 15 + 9 if args.coop else 12 + 6
    })


def create_master_agito_table(quest_id: int, args: AgitoArgs):
    return CustomTable(quest_id=quest_id, rupies=100000, drops={
        Material.CONSECRATED_WATER: 4,
        Material.AMPLIFYING_CRYSTAL: 4,
        Material.AMPLIFYING_GEMSTONE: 4,
        Material.FORTIFYING_CRYSTAL: 4,
        Material.FORTIFYING_GEMSTONE: 4,
        Material.ORICHALCUM: 6,
        args.t2_material: 12 if args.coop else 9,
        args.t3_material: 18 + 6 if args.coop else 12 + 6
    })
