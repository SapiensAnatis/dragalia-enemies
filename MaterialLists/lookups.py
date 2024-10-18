IGNORED_ITEM_TYPES = ["Weapon"]

TYPO_ADJUSTMENTS = {
    "wind Orb": "Wind Orb",
    "Papier-Mâché": "Papier-mâché",
    "Tiny Dragonatas": "Tiny Dragoñatas",
    "\\&quot;A Knight's Dream\\&quot; (Axe's Boon)": "\"A Knight's Dream\" (Axe's Boon)",
    "An Unfreezing Flower (Axe's  Boon)": "An Unfreezing Flower (Axe's Boon)"
}


DRAGON_AUG_MATERIALS = ["Fortifying Dragonscale", "Amplifying Dragonscale"]
MANACASTER_TABLET_MATERIALS = ["Manacaster Tablet"]
LAMBENT_GHOST_MATERIALS = ["Void Leaf",
                           "Void Seed",
                           "Bat's Wing",
                           "Ancient Bird's Feather",
                           "Old Cloth",
                           "Floating Yellow Cloth",
                           "Unearthly Lantern"]

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
    # Battle in the Dornith Mountains Standard/Expert/Master
    211040102: MANACASTER_TABLET_MATERIALS,
    211040103: MANACASTER_TABLET_MATERIALS,
    211040104: MANACASTER_TABLET_MATERIALS,
    # Battle at the Wartarch Ruins Standard
    211050102: MANACASTER_TABLET_MATERIALS,
    211050103: MANACASTER_TABLET_MATERIALS,
    211050104: MANACASTER_TABLET_MATERIALS,
    # Lambent Ghost Strike
    301020103: LAMBENT_GHOST_MATERIALS}

GIFT_LOOKUP: dict[str, int] = {
    "Dragonyule Cake": 30002,
    "Four-Leaf Clover": 30001
}
