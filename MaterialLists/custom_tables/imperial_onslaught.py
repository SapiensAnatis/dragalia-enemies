from dataclasses import dataclass
from materials import Material
from table_types import CustomTable


@dataclass
class ImperialOnslaughtArgs:
    t1_upgrade: Material
    t2_upgrade: Material
    t3_upgrade: Material
    t1_medal: Material
    t2_medal: Material
    tablets: list[Material]


def create_beginner_io_table(quest_id: int, args: ImperialOnslaughtArgs):
    return CustomTable(quest_id, mana=150, rupies=500, drops={
        Material.BRONZE_WHETSTONE: 5,
        Material.SILVER_WHETSTONE: 3,
        args.t1_upgrade: 40,
        Material.DYRENELL_AES: 160,
        Material.DYRENELL_ARGENTEUS: 40
    })


def create_standard_io_table(quest_id: int, args: ImperialOnslaughtArgs):
    tablet_drops = {t: 30 for t in args.tablets}

    return CustomTable(quest_id, mana=222, rupies=670, drops={
        Material.BRONZE_WHETSTONE: 5,
        Material.SILVER_WHETSTONE: 5,
        Material.GOLD_WHETSTONE: 2,
        args.t1_upgrade: 80,
        args.t2_upgrade: 120,
        Material.DYRENELL_AES: 240,
        Material.DYRENELL_ARGENTEUS: 40,
        args.t1_medal: 160,
        **tablet_drops
    })


def create_expert_io_table(quest_id: int, args: ImperialOnslaughtArgs):
    tablet_drops = {t: 40 for t in args.tablets}

    return CustomTable(quest_id, mana=290, rupies=885, drops={
        Material.BRONZE_WHETSTONE: 5,
        Material.SILVER_WHETSTONE: 3,
        Material.GOLD_WHETSTONE: 3,
        args.t2_upgrade: 80,
        args.t3_upgrade: 160,
        Material.DYRENELL_AES: 360,
        Material.DYRENELL_ARGENTEUS: 40,
        Material.DYRENELL_AUREUS: 80,
        args.t1_medal: 200,
        **tablet_drops
    })


def create_master_io_table(quest_id: int, args: ImperialOnslaughtArgs):
    tablet_drops = {t: 70 for t in args.tablets}

    return CustomTable(quest_id, mana=369, rupies=1110, drops={
        Material.BRONZE_WHETSTONE: 8,
        Material.GOLD_WHETSTONE: 5,
        args.t2_upgrade: 160,
        args.t3_upgrade: 160,
        Material.DYRENELL_AES: 480,
        Material.DYRENELL_ARGENTEUS: 80,
        Material.DYRENELL_AUREUS: 160,
        args.t1_medal: 440,
        args.t2_medal: 200,
        **tablet_drops
    })


def create_io_tables() -> list[CustomTable]:
    flame_io_args = ImperialOnslaughtArgs(
        t1_upgrade=Material.IRON_ORE,
        t2_upgrade=Material.GRANITE,
        t3_upgrade=Material.METEORITE,
        t1_medal=Material.VERMILION_INSIGNIA,
        t2_medal=Material.ROYAL_VERMILION_INSIGNIA,
        tablets=[Material.BLADE_TABLET,
                 Material.LANCE_TABLET,
                 Material.WAND_TABLET]
    )

    water_io_args = ImperialOnslaughtArgs(
        t1_upgrade=Material.FIENDS_CLAW,
        t2_upgrade=Material.FIENDS_HORN,
        t3_upgrade=Material.FIENDS_EYE,
        t1_medal=Material.AZURE_INSIGNIA,
        t2_medal=Material.ROYAL_AZURE_INSIGNIA,
        tablets=[Material.AXE_TABLET,
                 Material.BOW_TABLET,
                 Material.STAFF_TABLET]
    )

    wind_io_args = ImperialOnslaughtArgs(
        t1_upgrade=Material.BATS_WING,
        t2_upgrade=Material.ANCIENT_BIRDS_FEATHER,
        t3_upgrade=Material.BEWITCHING_WINGS,
        t1_medal=Material.JADE_INSIGNIA,
        t2_medal=Material.ROYAL_JADE_INSIGNIA,
        tablets=[Material.SWORD_TABLET,
                 Material.DAGGER_TABLET,
                 Material.STAFF_TABLET]
    )

    light_io_args = ImperialOnslaughtArgs(
        t1_upgrade=Material.IRON_ORE,
        t2_upgrade=Material.GRANITE,
        t3_upgrade=Material.METEORITE,
        t1_medal=Material.AMBER_INSIGNIA,
        t2_medal=Material.ROYAL_AMBER_INSIGNIA,
        tablets=[Material.SWORD_TABLET,
                 Material.BLADE_TABLET,
                 Material.DAGGER_TABLET,
                 Material.AXE_TABLET,
                 Material.MANACASTER_TABLET]
    )

    shadow_io_args = ImperialOnslaughtArgs(
        t1_upgrade=Material.FIENDS_CLAW,
        t2_upgrade=Material.FIENDS_HORN,
        t3_upgrade=Material.FIENDS_EYE,
        t1_medal=Material.VIOLET_INSIGNIA,
        t2_medal=Material.ROYAL_VIOLET_INSIGNIA,
        tablets=[Material.LANCE_TABLET,
                 Material.BOW_TABLET,
                 Material.WAND_TABLET,
                 Material.STAFF_TABLET,
                 Material.MANACASTER_TABLET]
    )

    return [
        # Battle at Mount Adolla: Beginner
        create_beginner_io_table(quest_id=211010101, args=flame_io_args),
        # Battle at Mount Adolla: Standard
        create_standard_io_table(quest_id=211010102, args=flame_io_args),
        # Battle at Mount Adolla: Expert
        create_expert_io_table(quest_id=211010103, args=flame_io_args),
        # Battle at Mount Adolla: Master
        create_master_io_table(quest_id=211010104, args=flame_io_args),
        # Battle at Myriage Lake: Beginner
        create_beginner_io_table(quest_id=211020101, args=water_io_args),
        # Battle at Myriage Lake: Standard
        create_standard_io_table(quest_id=211020102, args=water_io_args),
        # Battle at Myriage Lake: Expert
        create_expert_io_table(quest_id=211020103, args=water_io_args),
        # Battle at Myriage Lake: Master
        create_master_io_table(quest_id=211020104, args=water_io_args),
        # Battle in Rovetelle Forest: Beginner
        create_beginner_io_table(quest_id=211030101, args=wind_io_args),
        # Battle in Rovetelle Forest: Standard
        create_standard_io_table(quest_id=211030102, args=wind_io_args),
        # Battle in Rovetelle Forest: Expert
        create_expert_io_table(quest_id=211030103, args=wind_io_args),
        # Battle in Rovetelle Forest: Master
        create_master_io_table(quest_id=211030104, args=wind_io_args),
        # Battle in the Dornith Mountains: Beginner
        create_beginner_io_table(quest_id=211040101, args=light_io_args),
        # Battle in the Dornith Mountains: Standard
        create_standard_io_table(quest_id=211040102, args=light_io_args),
        # Battle in the Dornith Mountains: Expert
        create_expert_io_table(quest_id=211040103, args=light_io_args),
        # Battle in the Dornith Mountains: Master
        create_master_io_table(quest_id=211040104, args=light_io_args),
        # Battle at the Wartarch Ruins: Beginner
        create_beginner_io_table(quest_id=211050101, args=shadow_io_args),
        # Battle at the Wartarch Ruins: Standard
        create_standard_io_table(quest_id=211050102, args=shadow_io_args),
        # Battle at the Wartarch Ruins: Expert
        create_expert_io_table(quest_id=211050103, args=shadow_io_args),
        # Battle at the Wartarch Ruins: Master
        create_master_io_table(quest_id=211050104, args=shadow_io_args),
    ]
