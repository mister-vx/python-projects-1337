class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self._age: int = age

    def grow(self) -> None:
        """ Increases the plant's height by 1 cm, simulating growth """
        self.height += 1

    def age(self) -> None:
        """ Increases the plant's age by 1 day """
        self._age += 1

    def get_info(self) -> None:
        """ Prints the plant's name, height, and age in a readable format """
        print(f"{self.name}: {self.height}cm, {self._age} days old")


if __name__ == "__main__":
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        ]
    i: int = 1
    for p1 in plants:
        default_height: float = p1.height
        while (i <= 7):
            print(f"=== Day {i} ===")
            if (i != 1):
                p1.grow()
                p1.age()
            p1.get_info()
            i += 1
        print(f"Growth this week: +{p1.height - default_height}cm")
        i = 1
