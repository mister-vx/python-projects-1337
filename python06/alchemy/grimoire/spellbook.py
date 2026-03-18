from typing import Callable, Optional


def record_spell(spell_name: str, ingredients: str,
                 funct: Optional[Callable[[str], str]] = None) -> str:
    if funct is None:
        from .validator import validate_ingredients
        funct = validate_ingredients
    res = funct(ingredients)
    valid = res.split("-")[-1].strip()
    if (valid == "VALID"):
        return f"Spell recorded: {spell_name} ({res})"
    return f"Spell rejected: {spell_name} ({res})"
