class Plant:
    """
        Plant class serves as a template (blueprint)
        for creating plant objects. Each plant has a name, height, and age.
    """
    def __init__(self, name: str, height: float, age: int) -> None:
        """
            Initializes a Plant object with the given
            name, height (in cm), and age (in days).
        """
        self.name: str = name
        self.height: float = height
        self.age: int = age


if __name__ == "__main__":
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
    print("=== Garden Plant Registry ===")
    for p in plants:
        print(f"{p.name}: {p.height}cm, {p.age} days old")
