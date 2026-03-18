class Plant:
    counter: int = 0

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age
        Plant.counter += 1


if __name__ == "__main__":
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    for i in plants:
        print(f"Created: {i.name} ({i.height}cm, {i.age} days)")
    print(f"\nTotal plants created: {Plant.counter}")
