import json
from typing import Dict, Tuple, List, Any

text_strings: Dict[str, str] = {}
current_trade_id_list: Dict[int, int] = {}

event_name_id_map: Dict[str, int] = {}
event_id_group_map: Dict[int, int] = {}


class TTItem():
    name: str
    quantity: int

    def __init__(self, name: str, quantity: int) -> None:
        self.name = name
        self.quantity = quantity
        pass


class TTrade():
    target: TTItem
    limit: int
    needed: List[TTItem]

    def __init__(self, target: TTItem, limit: str, needed: List[TTItem]) -> None:
        self.target = target
        self.limit = 0 if '∞' in limit else int(limit.replace(",", ""))
        self.needed = needed
        pass

    def to_json(self, id: int, eventId: int):
        global current_trade_id_list

        base_id = id * 10000

        if id not in current_trade_id_list:
            current_trade_id_list[id] = 1

        base_id += current_trade_id_list[id]
        current_trade_id_list[id] += 1

        trade_json = {
            "_Id": base_id,
            "_TradeGroupId": id,
            "_Limit": self.limit,
            "_TabGroupId": 1,
            "_Priority": base_id,
            "_ResetType": 0,
            "_CommenceData": "",
            "_CompleteDate": "",
            "_IsLockView": 0,

            "_NeedEntityType1": 0,
            "_NeedEntityId1": 0,
            "_NeedEntityQuantity1": 0,
            "_NeedEntityLimitBreak1": 0,
            "_NeedEntityType2": 0,
            "_NeedEntityId2": 0,
            "_NeedEntityQuantity2": 0,
            "_NeedEntityLimitBreak2": 0,
            "_NeedEntityType3": 0,
            "_NeedEntityId3": 0,
            "_NeedEntityQuantity3": 0,
            "_NeedEntityLimitBreak3": 0,
            "_NeedEntityType4": 0,
            "_NeedEntityId4": 0,
            "_NeedEntityQuantity4": 0,
            "_NeedEntityLimitBreak4": 0,
            "_NeedEntityType5": 0,
            "_NeedEntityId5": 0,
            "_NeedEntityQuantity5": 0,
            "_NeedEntityLimitBreak5": 0,
        }

        if id == 10104 and get_id_from_string(self.needed[0].name, eventId) == 2140102:
            trade_json["_TabGroupId"] = 2
        elif id == 10105 and get_id_from_string(self.needed[0].name, eventId) == 2140302:
            trade_json["_TabGroupId"] = 2

        for i in range(1, len(self.needed) + 1):
            trade_json["_NeedEntityType" +
                       str(i)] = get_type_from_string(self.needed[i-1].name)
            trade_json["_NeedEntityId" +
                       str(i)] = get_id_from_string(self.needed[i-1].name, eventId)
            trade_json["_NeedEntityQuantity" +
                       str(i)] = self.needed[i-1].quantity
            trade_json["_NeedEntityLimitBreak" + str(i)] = 0

        trade_json["_DestinationEntityType"] = get_type_from_string(
            self.target.name)
        trade_json["_DestinationEntityId"] = get_id_from_string(
            self.target.name, eventId)
        trade_json["_DestinationEntityQuantity"] = self.target.quantity
        trade_json["_DestinationEntityLimitBreak"] = 0

        return trade_json

    def __str__(self) -> str:
        return f"Trade: {[f'{x.quantity}x {x.name}' for x in self.needed]} -> {self.target.quantity}x {self.target.name} (limit {self.limit})"


class TTradeEvent():
    event_name: str
    trades: List[TTrade]
    page_id: int

    def __init__(self, name: str, trades: List[TTrade], page: int) -> None:
        self.event_name = name
        self.trades = trades
        self.page_id = page
        pass

    def to_json(self) -> Any:
        eventId = event_name_id_map[text_strings[self.event_name]]
        id = event_id_group_map[eventId]
        print(f"{self.event_name} -> {id}")

        tradelist = []
        for trade in self.trades:
            tradelist.append(trade.to_json(id, eventId))

        return tradelist

    def print(self):
        print(f"Event name: {self.event_name}")
        for trade in self.trades:
            print(f"\t{str(trade)}")


def get_type_from_string(name: str) -> int:
    global text_strings

    if name == "Papier-mâché":
        name = "Papier-Mâché"

    if name == "Jack Chocolates":
        name = "Jack Chocolate"

    if name == "Mana":
        return 18

    if name == "Rupies":
        return 4

    if name == "Eldwater":
        return 14

    if "Sticker:" in name:
        name = "Sticker: Hey, not bad!"

    label = text_strings[name]

    if label.startswith("FORT_PLANT"):
        return 9
    elif label.startswith("MATERIAL"):
        return 8
    elif label.startswith("EV_BUILD_ITEM"):
        return 22
    elif label.startswith("EV_CLB_01") or "Universal Shard" == name or "Universal Crystal" == name:
        return 25
    elif label.startswith("EV_COMBAT"):
        return 34
    elif label.startswith("EV_EARN"):
        return 40
    elif label.startswith("USE_ITEM"):
        return 2
    elif label.startswith("DRAGON_GIFT"):
        return 15
    elif label.startswith("GATHER_ITEM"):
        return 33
    elif label.startswith("STAMP_"):
        return 11
    elif label.startswith("AMULET_NAME"):
        return 39

    print(label)
    raise RuntimeError("invalid label")


event_item_type_file_map = {
    20: "Raid",
    22: "Build",
    24: "Collect",
    25: "Clb01",
    29: "ExRush",
    30: "Simple",
    34: "Combat",
    36: "BattleRoyal",
    40: "Earn"
}

event_item_cache = {

}


def get_actual_id_for_event_item(id, type, event):
    if type not in event_item_cache.keys():
        with open(f"json/{event_item_type_file_map[type]}EventItemDY.json", "r") as f:
            data = json.loads(f.read())
            event_item_cache[type] = {}
            for entry in data:
                eventId = entry["_EventId"] if type != 20 else entry["_RaidEventId"]
                if eventId not in event_item_cache[type].keys():
                    event_item_cache[type][eventId] = {}
                event_item_cache[type][eventId][int(
                    entry["_Name"].split("_")[-1])] = entry["_Id"]

    print(f"{id} ({type}) => {event_item_cache[type][event][id]}")
    return event_item_cache[type][event][id]


def get_id_from_string(name: str, eventId: int = 0) -> int:
    global text_strings

    if name == "Papier-mâché":
        name = "Papier-Mâché"

    if name == "Jack Chocolates":
        name = "Jack Chocolate"

    if name in ["Mana", "Rupies", "Eldwater"]:
        return 0

    if name == "Universal Shard":
        return 2140301

    if name == "Universal Crystal":
        return 2140302

    if "Sticker:" in name:
        name = "Sticker: Hey, not bad!"

    id = int(text_strings[name].split("_")[-1])

    type = get_type_from_string(name)

    if type in [20, 22, 24, 25, 29, 30, 34, 36, 40]:
        return get_actual_id_for_event_item(id, type, eventId)

    return id


def parse_content(content: str) -> list[TTrade]:
    if "TreasureTradeShop" in content:
        # print(f"Trades for page {page_id}:")
        shop_begin = content.find("TreasureTradeShop")
        shop_end = content.find("</div>\n</div>", shop_begin)

        shop_data = content[shop_begin:shop_end]

        trades = parse_treasure_trade_table(shop_data)
        if len(trades) == 0:
            print("warn: found no trades")

        return trades

    return []


def init_maps():
    with open("json/TextLabel.json", "r", encoding="utf-8") as f:
        texts = f.read()
        text_strs: list = json.loads(texts)
        # text_strings = dict((x["_Text"], x["_Id"]) for x in text_strs)
        for x in text_strs:
            if x["_Text"] not in text_strings:
                text_strings[x["_Text"]] = x["_Id"]

        text_strings["Trick or Treasure!"] = "EVENT_NAME_20811"
        text_strings["The Accursed Archives"] = "EVENT_NAME_20812"

    with open("json/EventData.json", "r", encoding="utf-8") as f:
        eventtext = f.read()
        eventdata: list = json.loads(eventtext)
        for event in eventdata:
            if event["_IsMemoryEvent"] == 1:
                event_name_id_map[event["_Name"]] = event["_Id"]

    with open("json/EventTradeGroup.json", "r", encoding="utf-8") as f:
        eventgrouptext = f.read()
        eventgroups: list = json.loads(eventgrouptext)
        for group in eventgroups:
            event_id_group_map[group["_EventId"]] = group["_Id"]


def main():
    global text_strings, event_name_id_map, event_id_group_map
    with open("api-result.json", "r", encoding="utf-8") as f:
        apidata = f.read()

    init_maps()

    api_json = json.loads(apidata)

    pages: dict = api_json["query"]["pages"]

    events: List[TTradeEvent] = []

    print(f"total pages: {len(pages.keys())}")

    for page_id, page_val in pages.items():
        # if page_id != "31760":
        #    continue

        content: str = page_val["revisions"][0]["slots"]["main"]["*"]
        if "TreasureTradeShop" in content:
            # print(f"Trades for page {page_id}:")

            shop_begin = content.find("TreasureTradeShop")
            shop_end = content.find("</div>\n</div>", shop_begin)

            if page_id in ["31760", "31761", "36579"]:
                shop_end = content.find("}}\n</div>", shop_begin)

            if page_id in ["37876", "38423", "38424"]:
                shop_end = content.find("</div></div>", shop_begin)

            # print(content[shop_begin:shop_end])

            shop_data = content[shop_begin:shop_end]

            if "tabber" in shop_data:
                print(f"warn: trade {page_id} has tabs")

            trades = parse_treasure_trade_table(shop_data)
            if len(trades) == 0:
                print("warn: found no trades")

            events.append(TTradeEvent(
                page_val["title"].split("/")[0], trades, int(page_id)))

    print("parsing done")
    total_list = []
    for event in events:
        # print(f"{event.event_name}: {event.page_id}")
        total_list += event.to_json()

    with open("EventTreasureTradeInfo.json", "w") as f:
        f.write(json.dumps(total_list, indent=1))
        # print(json.dumps(event.to_json()))
        # exit()

#            TODO: FIX EVENT ITEM IDS IN TRADE REWARDS


def parse_treasure_trade_table(table: str):
    trades = []

    for line in table.splitlines():
        if line.startswith("|") and "||" in line:
            # print(line)
            trades.append(parse_treasure_trade_line(line))

    return trades


def parse_treasure_trade_line(line: str) -> TTrade:
    parts = line.split("||")
    # print(parts)

    target_item = parse_treasure_trade_item(parts[0])
    limit = parts[1].strip().replace("<big>", "").replace("</big>", "")

    needed_items = [parse_treasure_trade_item(
        x.strip()) for x in parts[2].split(", ")]

    # print(f"Trade: {[f'{x.quantity}x {x.name}' for x in needed_items]} -> {target_item.quantity}x {target_item.name} (limit {limit})")

    return TTrade(target_item, limit, needed_items)


def parse_treasure_trade_item(item: str):
    global text_strings

    item_begin = item.find("{{")
    item_end = item.find("}}")

    is_normal_format = "{{Icon" in item

    if "Sticker:" in item:
        return TTItem(item, 1)

    quantity = int(item[item_end + 2:].replace("x", "").replace(",",
                   "").replace("-", "").replace(">", "").strip())

    if is_normal_format:
        item_parts = item[item_begin + 2:item_end].split("|")
        item_name = item_parts[2].strip()
    else:
        item_name = item[item_begin + 2:item_end - 1]

    # print(f"name: {text_strings[item_name]}, quantity {quantity}")

    return TTItem(item_name, quantity)


if __name__ == "__main__":
    main()
