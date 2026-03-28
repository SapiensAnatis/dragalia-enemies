"""
Produce a list of assets containing quest scene data.
"""

import os
import json
from get_enemies import get_enemies_from_file

WORKING_DIR = os.path.dirname(os.path.realpath(__file__))
ASSET_DIR = r"/home/jay/mnt/WinD/DragaliaLost Assets/EU_locale"


def get_assetpath(hash: str) -> str:
    """
    Get an asset's path from its hash.
    """
    return os.path.join(ASSET_DIR, hash[:2], hash)


def filter_quest(manifest_asset: dict) -> bool:
    """
    Determines whether an asset is a quest asset.
    """
    return manifest_asset["name"].startswith("prefabs/ingame/quest")


def get_quest_assets(json_path: str) -> list:
    """
    Gets a list of quest assets from a manifest path.
    """
    print(json_path)
    with open(json_path, "r", encoding="utf-8") as f:
        manifest = json.loads(f.read())
        all_assets = manifest["rawAssets"]
        for cat in manifest["categories"]:
            all_assets += cat["assets"]

        return list(filter(filter_quest, all_assets))


if __name__ == "__main__":
    hashes = []
    assets = get_quest_assets(os.path.join(
        WORKING_DIR, "DragaliaManifests/Android/20210131_lqfRBhj2APlqf8RC/assetbundle.manifest.json"))

    result = {}
    with open ("/home/jay/Projects/Dawnshard/DragaliaAPI/DragaliaAPI.Shared/Resources/Enemy/QuestEnemies.json", "r", encoding="utf-8") as f_existing:
        existing_list = json.loads(f_existing.read())
        for entry in existing_list:
            result[entry["_AreaName"]] = entry

    complete_hashes = set()

    for i, a in enumerate(assets):
        print(f"{i} / {len(assets)}")

        hash_name = a["hash"]
        if (hash_name in complete_hashes):
            print("Skipping")
            continue

        path = get_assetpath(a["hash"])
        if not os.path.exists(get_assetpath(hash_name)):
            print(f"Could not find asset for {path}")
            continue

        enemies = get_enemies_from_file(path)
        areaname = enemies["_AreaName"]
        if areaname not in result:
            result[areaname] = enemies

        complete_hashes.add(hash_name)

    result_values = list(result.values())
    with open("output.json", "w", encoding="utf8") as f:
        json.dump(result_values, f, indent=4)
