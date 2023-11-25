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
    # Battle in the Dornith Mountains Standard
    211040102: MANACASTER_TABLET_MATERIALS,
    # Battle at the Wartarch Ruins Standard
    211050102: MANACASTER_TABLET_MATERIALS,
    # Lambent Ghost Strike
    301020103: LAMBENT_GHOST_MATERIALS}

GIFT_LOOKUP: dict[str, int] = {
    "Dragonyule Cake": 30002,
    "Four-Leaf Clover": 30001
}
