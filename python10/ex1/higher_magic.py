from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combiner(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combiner


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} with {power} power"


def heal(target: str, power: int) -> str:
    return f"Heals {target} for {power} HP"


def condition(target: str, power: int) -> bool:
    return power >= 10


def main() -> None:
    try:
        print("\nTesting spell combiner...")
        spell_combined = spell_combiner(fireball, heal)
        res = spell_combined("Dragon", 10)
        print(f"Combined spell result {res[0]}, {res[1]}")
        print("\nTesting power amplifier...")
        mega_fireball = power_amplifier(fireball, 3)
        res = mega_fireball("Orc", 10)
        print(res)
        print("\nTesting conditional caster...")
        safe_fireball = conditional_caster(condition, fireball)
        print(safe_fireball("Dragon", 5))
        print(safe_fireball("Dragon", 12))
        print("\nTesting spell sequence...")
        spells = [fireball, heal]
        sequence = spell_sequence(spells)
        print(sequence("Knight", 20))
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
