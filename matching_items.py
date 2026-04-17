import json
from collections import defaultdict


def main():
    matching = defaultdict(list)
    filepath = "dict.json"
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
    except OSError as e:
        print(e)
        return None
    
    for order in data["orders"]:
        for item in order["items"]:
            for other in order["items"]:
                if item["product"] != other["product"]:
                    matching[item["product"]].append(other["product"])
                
    print(matching)
if __name__ == "__main__":
    main()