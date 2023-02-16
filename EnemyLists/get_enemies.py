#! /usr/bin/env python3

"""
Functions for getting a list of enemy_param ids from an asset stage.
"""

import os.path
import UnityPy # @ 1.9.26

WORKING_DIR = os.path.dirname(os.path.realpath(__file__))

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
    for transform in difficulty.m_Components:
        for gameobj in gen_gameobject_endnode(transform.read()):
            yield from gen_enemies_from_group(gameobj)

def gen_difficulty(asset):
    """
    From an asset, yield every game object with a name matching a quest
    """
    for obj in asset.objects.values():
        if obj.type.name == "GameObject":
            read = obj.read()
            if read.name in ["Normal", "Hard", "VeryHard"]:
                yield read

def get_enemies(asset):
    """
    For an asset, build a dictionary of `{ difficulty: enemy_list }`
    """
    result = {}
    for obj in gen_difficulty(asset):
        read = obj.read()
        difficulty = read.name
        result[difficulty] = list(gen_enemies_from_difficulty(read))

    return result

if __name__ == "__main__":
    env = UnityPy.load(os.path.join(WORKING_DIR, "testassets/DOEBJI2NAV6TUU5ZYKILA3EPN3GX55TONMZFIMXVEWHADLRRA6EQ"))
    print(get_enemies(env.assets[0]))
