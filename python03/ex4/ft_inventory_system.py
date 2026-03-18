import sys


def get_data() -> dict[str, int]:
    data: dict[str, int] = {}
    for d in sys.argv:
        i = 0
        size = len(d)
        while (i < size and d[i] != ':'):
            i += 1
        if (i < size):
            k = d[0:i]
            try:
                v = int(d[i + 1:])
                if (k == ""):
                    print("Name cannot be empty")
                elif (v < 0):
                    print(f"Quantity cannot be negative '{v}'")
                else:
                    data.update({k: v})
            except ValueError as err:
                print("Error:", err)
    return data


def get_max(data: dict[str, int]) -> dict[str, int]:
    max_value = None
    max_key = None
    for key in data.keys():
        if (max_value is None or max_value < data.get(key)):
            max_value = data.get(key)
            max_key = key
    max_item = {max_key: max_value}
    return max_item


def get_min(data: dict[str, int]) -> dict[str, int]:
    min_value = None
    min_key = None
    for key in data.keys():
        if (min_value is None or min_value > data.get(key)):
            min_value = data.get(key)
            min_key = key
    min_item = {min_key: min_value}
    return min_item


def dictionary_properties(data: dict[str, int]) -> None:
    print("Dictionary keys: ", end="")
    is_true = True
    for key in data.keys():
        if (not is_true):
            print(", ", end="")
        print(key, end="")
        is_true = False
    print("\nDictionary values: ", end="")
    is_true = True
    for key in data.keys():
        if (not is_true):
            print(", ", end="")
        print(data.get(key), end="")
        is_true = False


def manage_categories(data: dict[str, int]) -> None:
    item_cat = {
        "abundant": {"Most": get_max(data), "Least": get_min(data)},
    }
    max_dic: dict = item_cat["abundant"]["Most"]
    min_dic: dict = item_cat["abundant"]["Least"]
    (max_key, max_value), = max_dic.items()
    (min_key, min_value), = min_dic.items()
    moderate_dic = {}
    for key, val in data.items():
        if (val == max_value):
            moderate_dic.update({key: val})
    item_cat.update({"moderate": moderate_dic})
    scarce_dic = {}
    for key, value in data.items():
        if (value != max_value):
            scarce_dic.update({key: value})
    item_cat.update({"scarce": scarce_dic})
    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {max_key} ({max_value} units)")
    if (min_value > 1):
        print(f"Least abundant: {min_key} ({min_value} units)")
    else:
        print(f"Least abundant: {min_key} ({min_value} unit)")
    print("\n=== Item Categories ===")
    print("Moderate:", item_cat.get("moderate"))
    print("Scarce:", item_cat.get("scarce"))
    print("\n=== Management Suggestions ===")
    print("Restock needed: ", end="")
    is_true = True
    for key in data.keys():
        if (data[key] == min_value):
            if (not is_true):
                print(", ", end="")
            print(key, end="")
            is_true = False


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    if (len(sys.argv) > 1):
        data = get_data()
        if (len(data) > 0):
            sm = 0
            for val in data.values():
                sm += val
            print("Total items in inventory:", sm)
            print("Unique item types:", len(data), "\n")
            print("=== Current Inventory ===")
            i = 0
            for i in data.keys():
                print(f"{i}: {data[i]} units ({(data[i] / sm) * 100:.1f}%)")
            manage_categories(data)
            print("\n\n=== Dictionary Properties Demo ===")
            dictionary_properties(data)
            ky = "sword"
            is_found = ky in data
            print(f"\nSample lookup - '{ky}' in inventory:", is_found)
    else:
        print("No items provided. Usage:",
              "python3 ft_inventory_system.py item:quantity ...")
