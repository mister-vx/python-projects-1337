from collections.abc import Callable
import functools
import time
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return res
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get("power", args[-1])
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for att in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if att == max_attempts:
                        return (f"Spell casting failed after"
                                f" {max_attempts} attempts")
                    else:
                        print(f"Spell failed, retrying..."
                              f" (attempt {att}/{max_attempts})")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (len(name.strip()) >= 3
                and all(n.isalpha() or n.isspace() for n in name))

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(0.101)
    return "Fireball cast!"


@retry_spell(3)
def failed_spell() -> None:
    raise Exception("spell failed")


@retry_spell(3)
def successed_spell() -> str:
    return "Waaaaaaagh spelled !"


def main() -> None:
    print("Testing spell timer...")
    res = fireball()
    print(f"Result: {res}")
    print("\nTesting retrying spell...")
    res = failed_spell()
    print(res)
    res = successed_spell()
    print(res)
    print("\nTesting MageGuild...")
    guild = MageGuild()
    try:
        print(guild.validate_mage_name("ahmed"))
    except Exception as err:
        print(err)
    try:
        print(guild.validate_mage_name("011"))
    except Exception as err:
        print(err)
    try:
        print(guild.cast_spell("Lightning", power=15))
    except Exception as err:
        print(err)
    try:
        print(guild.cast_spell("Lightning", power=6))
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
