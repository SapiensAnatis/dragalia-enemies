"""
Interface for Dragalia Lost Wiki's CargoQuery to fetch all quest drops from the DropRewards table.

Please be kind to the wiki's servers and use the provided cargoquery.json instead of running this.
"""

from time import sleep
import json
import requests
import MaterialLists.cargo_constants as cargo_constants


def query(req_params):
    """
    Generator for paged CargoQuery API.
    """
    i = 0
    while True:
        # Clone original request
        new_params = req_params.copy()
        new_params.update({"offset": i})

        # Call API
        result = requests.get(
            cargo_constants.DRAGALIA_WIKI_URL,
            params=new_params,
            headers=cargo_constants.HEADERS,
            timeout=100
        ).json()

        if "error" in result:
            raise ValueError(result["error"])
        if "warnings" in result:
            print(result["warnings"])
        if "cargoquery" in result:
            result_count = len(result["cargoquery"])
            print(f"Found {result_count} results")
            if result_count > 0:
                yield result["cargoquery"]
            else:
                print("Finished!")
                break

        i += 500
        print(f"Processed request {i}")
        sleep(cargo_constants.REQUEST_SLEEP_SECS)


if __name__ == "__main__":
    params = {
        "action": "cargoquery",
        "maxlag": 1,
        "format": "json",
        "limit": "max",
        "tables": "DropRewards, Quests",
        "where": "DropRewards.DropType = 'Common'",
        "fields": "Quests.Id=QuestId, DropRewards.ItemType, DropRewards.Item, DropRewards.DropType, DropRewards.MinDrop, DropRewards.MaxDrop, DropRewards.ExactDrop,",
        "join_on": "Quests._pageID = DropRewards._pageID"
    }

    cargoquery = []

    gen = query(params)
    for response in gen:
        cargoquery += [r["title"] for r in response]

    with open("cargo_query.json", "w", encoding="utf-8") as f:
        json.dump(cargoquery, f)
