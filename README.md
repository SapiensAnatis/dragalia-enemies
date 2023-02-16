## dragalia-enemies

A collection of Python scripts to try and determine enemy/quest drops.

## Scripts

### EnemyLists

#### get_enemies.py

Scans a given assetbundle for enemy generators and returns a data structure containing information about the enemy ids and quantity of each.

#### get_quest_assets.py

WIP - will scan the manifests for quest assets and iteratively call `get_enemies.py` on each.

### MaterialLists

#### cargo_query.py

Query the Dragalia Lost Wiki database for their data on drop lists for each quest, which have been manually added by contributors. NOTE: Please do not run this without good reason as it puts load on the wiki servers; the `cargo_query.json` file contains the results you can expect to get from this.

#### cargo_parse.py

Parse `cargo_query.json` into a more usable format, by replacing material/wyrmprint string names into IDs, and reformatting the JSON structure to be keyed by quest ID.