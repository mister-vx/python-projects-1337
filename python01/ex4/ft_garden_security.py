class SecurePlant:
    """
        This class focuses on protecting plant data
        by using getters, setters, and validation.
    """
    def __init__(self, name: str, height: float, age: int) -> None:
        """
            Using _ makes attributes protected
        """
        self.name: str = name
        self._height: float = 0
        self._age: int = 0
        print(f"Plant created: {name}")
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> float:
        """ Returns the current height of the plant """
        return (self._height)

    def get_age(self) -> int:
        """ Returns the current age of the plant """
        return (self._age)

    def set_height(self, val: float) -> None:
        """ Updates the plant height after validating the value """
        if (val >= 0):
            self._height = val
            print(f"Height updated: {val}cm [OK]")
        else:
            print(f"\nInvalid operation attempted: height {val}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, val: int) -> None:
        """ Updates the plant age after validating the value """
        if (val >= 0):
            self._age = val
            print(f"Age updated: {val} days [OK]")
        else:
            print(f"\nInvalid operation attempted: age {val} [REJECTED]")
            print("Security: Negative age rejected")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p: SecurePlant = SecurePlant("Rose", 25, 30)
    p.set_height(-5)
    print(f"\nCurrent plant: {p.name} ({p.get_height()}cm, \
{p.get_age()} days)")
