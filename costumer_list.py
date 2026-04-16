import json


def main():
    dicto = {}
    filepath = "dict.json"
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
    except OSError as e:
        print(e)
        return None

    for order in data["orders"]:
        name = order["customer"].get("name")

        for item in order["items"]:
            total_cost = item["price"] * item["qty"] * (1 - item["discount"])
            ini_value = dicto.get(name, 0)
            dicto[name] = total_cost + ini_value
        dicto[name] += order["shipping"].get("cost", 0)
    
    print(dicto)

if __name__ == "__main__":
    main()