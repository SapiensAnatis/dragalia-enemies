#! /usr/bin/env python3

"""
Functions for getting a list of enemy_param ids from an asset stage.
"""

import os.path
import UnityPy  # @ 1.9.26

WORKING_DIR = os.path.dirname(os.path.realpath(__file__))
DIFFICULTY_VARIATIONTYPE = {
    "Normal": 1,
    "Hard": 2,
    "VeryHard": 3,
    "Extreme": 4,
    "Hell": 5,
    "Variation6": 6,
    "Variation7": 7,
    "Variation8": 8,
}


def gen_children(gameobject):
    """
    Get the child gameobjects of a gameobject.
    """
    transform = next(c.read()
                     for c in gameobject.m_Components if c.type.name == "Transform")
    for c in transform.m_Children:
        yield c.read().m_GameObject.read()


def gen_gameobject_endnode(transform):
    """
    Recurse a transform down to the root and get the matched gameobject (e.g. Group_002)
    """
    children = len(transform.m_Children)
    if children > 0:
        for child in transform.m_Children:
            yield from gen_gameobject_endnode(child.read())
    else:
        yield transform.m_GameObject.read()


def gen_enemies_from_group(group_obj):
    """
    From a Group_XXX gameobject, yield the MonoBehaviour components containing _enemyParam
    """
    for component in group_obj.m_Components:
        if component.type.name == "MonoBehaviour":
            read = component.read()
            tree = read.read_typetree()
            if "_enemyParam" in tree:
                yield (tree["_enemyParam"], tree["_generateCount"])


def gen_enemies_from_difficulty(difficulty):
    """
    Combine the other generators to yield enemies from a root difficulty object
    """
    for component in difficulty.m_Components:
        if component.type.name != "Transform":
            continue

        for gameobj in gen_gameobject_endnode(component.read()):
            yield from gen_enemies_from_group(gameobj)


def gen_difficulty(asset):
    """
    From an asset, yield every game object with a name matching a quest
    """
    for obj in asset.objects.values():
        if obj.type.name == "GameObject":
            read = obj.read()
            if read.name == "EnemyGenerators":
                yield from gen_children(read)


def get_enemies(asset):
    """
    For an asset, build a dictionary of `{ difficulty: enemy_list }`
    """
    result = {}
    result["_Enemies"] = {}
    for obj in gen_difficulty(asset):
        read = obj.read()
        difficulty = DIFFICULTY_VARIATIONTYPE[read.name]
        result["_Enemies"][difficulty] = []
        for enemy_pair in gen_enemies_from_difficulty(read):
            result["_Enemies"][difficulty] += [enemy_pair[0]
                                               for _ in range(enemy_pair[1])]

    return result


def get_enemies_from_file(asset_filepath):
    """
    Load a quest asset file and generate an enemy list from it.
    """
    env = UnityPy.load(asset_filepath)
    filename = next(iter(env.container))
    filename_trim = filename.replace(
        "assets/_gluonresources/resources/prefabs/ingame/quest/", "").replace(".prefab", "")
    result = get_enemies(env.assets[0])
    result["_AreaName"] = filename_trim
    return result


if __name__ == "__main__":
    print(get_enemies_from_file(
        # r"D:\DragaliaLost Assets\EU_locale\OY\OYANUNWK3SRJWTFTES35I5VOH4WKXQQP3FG6DBUUHCO6ID7GC65Q")) # Golem tough
        r"D:\DragaliaLost Assets\EU_locale\CY\CYCS4KMK255JKD6MWOLTBTO6CQCUBL244UMNKTRQXHHC52UYWADQ"))
