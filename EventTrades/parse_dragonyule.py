#!/usr/bin/env python3

import json
import eventtrades
import sys

print(sys.argv)

if (len(sys.argv) != 3):
    print("Usage: parse_dragonyule.py [path to dumped wiki page] [event id]")
    sys.exit(1)

with open(sys.argv[1], "r", encoding="utf8") as f:
    content = f.read()

eventtrades.init_maps()

trades = eventtrades.parse_content(content)

# change 10229 trade group ID, not sure how to get it except check what the client sends in request to /event_trade/get_list
json_trades = [trade.to_json(10229, int(sys.argv[2])) for trade in trades]

with open("out.json", "w", encoding="utf8") as f:
    json.dump(json_trades, f)
    print("Wrote trades to: out.json")
