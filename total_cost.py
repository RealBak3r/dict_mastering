import json


def main():
    total_cost = 0
    filepath = "dict.json"
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
    except OSError as e:
        print(e)
        return None
    for x in data["orders"]:
        cost_ship = x["shipping"].get("cost", 0)
        for y in x["items"]:
            real_price = y["price"] * y["qty"] *(1- y["discount"]) - cost_ship
            total_cost = total_cost + real_price
            print(total_cost)
    print(total_cost)

if __name__ == "__main__":
    main()