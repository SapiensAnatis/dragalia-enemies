import json
import eventtrades

with open("dragonyulepage.txt", "r", encoding="utf8") as f:
    content = f.read()

eventtrades.init_maps()

trades = eventtrades.parse_content(content)
json_trades = [trade.to_json(10803, 22903) for trade in trades]

with open("dragonyule.json", "w", encoding="utf8") as f:
    json.dump(json_trades, f)
