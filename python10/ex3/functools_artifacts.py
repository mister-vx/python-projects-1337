from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    operations: dict[str, Callable] = {
        "max": max,
        "min": min,
        "multiply": operator.mul,
        "add": operator.add,
    }
    if operation not in operations:
        raise ValueError("operation is unknown")
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    water = partial(base_enchantment, 50, "water")
    earth = partial(base_enchantment, 50, "earth")
    wind = partial(base_enchantment, 50, "wind")
    return {
        "water": water,
        "earth": earth,
        "wind": wind
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("number must be >= 0")
    if n in (0, 1):
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"
    return dispatch


def main() -> None:
    print("\nTesting spell reducer...")
    numbers = [10, 20, 30, 40]
    try:
        print(f"Sum: {spell_reducer(numbers, 'add')}")
    except Exception as err:
        print(err)
    try:
        print(f"Product: {spell_reducer(numbers, 'multiply')}")
    except Exception as err:
        print(err)
    try:
        print(f"Max: {spell_reducer(numbers, 'max')}")
    except Exception as err:
        print(err)
    print("\nTesting memoized fibonacci...")
    numbers = [0, 1, 10, 15]
    for i in range(len(numbers)):
        try:
            res = memoized_fibonacci(numbers[i])
            print(f"Fib({numbers[i]}): {res}")
        except Exception as err:
            print(err)
    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher(0.0))


if __name__ == "__main__":
    main()
