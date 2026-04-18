from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count
    return increment


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def add_power(power: int) -> int:
        nonlocal total_power
        total_power += power
        return total_power
    return add_power


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, Callable]:
    memory_v = {}

    def store(key: str, value: Any) -> None:
        memory_v.update({key: value})

    def recall(key: str) -> Any:
        return memory_v.get(key, "Memory not found")
    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print("\nTesting spell accumulator...")
    base = 100
    accumulator = spell_accumulator(base)
    add_power1 = 20
    add_power2 = 30
    try:
        print(f"Base {base}, add {add_power1}: {accumulator(add_power1)}")
    except Exception as err:
        print(err)
    try:
        print(f"Base {base}, add {add_power2}: {accumulator(add_power2)}")
    except Exception as err:
        print(err)
    print("\nTesting enchantment factory...")
    factory1 = enchantment_factory("Flaming")
    factory2 = enchantment_factory("Frozen")
    print(factory1("Sword"))
    print(factory2("Shield"))
    print("\nTesting memory vault...")
    vault = memory_vault()
    try:
        key = "secret"
        val = 42
        vault["store"](key, val)
        print(f"Store '{key}' = {val}")
        print(f"Recall '{key}': {vault['recall'](key)}")
        key = "unknown"
        print(f"Recall '{key}': {vault['recall'](key)}")
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
