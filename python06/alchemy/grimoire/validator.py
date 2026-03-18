def validate_ingredients(ingredients: str) -> str:
    valid = ["fire", "water", "earth", "air"]
    res = ingredients.split()
    for i in res:
        if i not in valid:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
