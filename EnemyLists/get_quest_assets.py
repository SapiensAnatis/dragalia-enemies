"""
Produce a list of assets containing quest scene data.
"""

import os
import json
import get_enemies

WORKING_DIR = os.path.dirname(os.path.realpath(__file__))
ASSET_DIR = 

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

        return filter(filter_quest, all_assets)


if __name__ == "__main__":
    hashes = []
    assets = get_quest_assets(os.path.join(WORKING_DIR, "DragaliaManifests/Android/20221002_y2XM6giU6zz56wCm/assetbundle.manifest.json"))
    for a in assets:
        hashes.append(a["hash"])

    for h in hashes:

