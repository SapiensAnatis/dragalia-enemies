def filter_quest(manifest_asset: dict) -> bool:
    return manifest_asset["name"].startswith("prefabs/ingame/quest")

def get_quest_assets(json_path: str) -> list:
    print(json_path)
    with open(json_path, "r", encoding="utf-8") as f:
        manifest = json.loads(f.read())
        all_assets = manifest["rawAssets"]
        for cat in manifest["categories"]:
            all_assets += cat["assets"]

        return filter(filter_quest, all_assets)

if not os.path.exists("manifests"):
    Repo.clone_from("https://github.com/DragaliaLostRevival/DragaliaManifests", "manifests")

folders = sorted(os.listdir(os.path.join("manifests", "Android")), reverse=True)
processed_quests = []
hashes = []

for folder in folders:
    print(folder)

    assets = get_quest_assets(os.path.join("manifests", "Android", folder, "assetbundle.manifest.json"))
    for a in assets:
        if a["name"] not in processed_quests:
            processed_quests.append(a["name"])
            hashes.append(a["hash"])

with open("output/asset_hashes.json", "w") as f:
    json.dump(hashes, f)
