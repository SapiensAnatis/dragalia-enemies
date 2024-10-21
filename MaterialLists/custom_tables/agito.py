from dataclasses import dataclass
from materials import Material
from table_types import CustomTable


@dataclass
class AgitoArgs:
    t1_material: Material
    t2_material: Material
    t3_material: Material
    tablets: list[Material]


def get_agito_is_coop(quest_id: int):
    # 219041101: solo
    # 219040101: co-op
    #      ^ checking for this digit
    return quest_id % 10000 < 1000


def create_standard_agito_table(quest_id: int, args: AgitoArgs):
    coop = get_agito_is_coop(quest_id)

    return CustomTable(quest_id=quest_id, rupies=100000, drops={
        Material.CONSECRATED_WATER: 3,
        Material.AMPLIFYING_CRYSTAL: 4,
        Material.FORTIFYING_CRYSTAL: 4,
        args.t1_material: 24 + 18 if coop else 18 + 12  # TODO: Survival bonuses
    })


def create_expert_agito_table(quest_id: int, args: AgitoArgs):
    coop = get_agito_is_coop(quest_id)

    return CustomTable(quest_id=quest_id, rupies=100000, drops={
        Material.CONSECRATED_WATER: 3,
        Material.AMPLIFYING_CRYSTAL: 2,
        Material.AMPLIFYING_GEMSTONE: 2,
        Material.FORTIFYING_CRYSTAL: 2,
        Material.FORTIFYING_GEMSTONE: 2,
        args.t1_material: 12 if coop else 9,
        args.t2_material: 15 + 9 if coop else 12 + 6
    })


def create_master_agito_table(quest_id: int, args: AgitoArgs):
    coop = get_agito_is_coop(quest_id)

    return CustomTable(quest_id=quest_id, rupies=100000, drops={
        Material.CONSECRATED_WATER: 4,
        Material.AMPLIFYING_CRYSTAL: 4,
        Material.AMPLIFYING_GEMSTONE: 4,
        Material.FORTIFYING_CRYSTAL: 4,
        Material.FORTIFYING_GEMSTONE: 4,
        Material.ORICHALCUM: 6,
        args.t2_material: 12 if coop else 9,
        args.t3_material: 18 + 6 if coop else 12 + 6
    })
