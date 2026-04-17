import json


def main():
    category = {}
    filepath = "dict.json"
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
    except OSError as e:
        print(e)
        return None
    
    for item in data["orders"]:
        for prod in item["items"]:
                cat = prod.get("category")
                clean = category.get(cat, 0)
                category[cat] = clean + (prod["qty"] * prod["price"] * (1 - prod.get("discount", 0)))

    print(category)
    print(f"MAX: {max(category, key=category.get)}")

if __name__ == "__main__":
    main()