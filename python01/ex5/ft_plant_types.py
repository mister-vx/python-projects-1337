class Plant:
    """ super class """
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age


class Flower(Plant):
    """
    The subclass (Flower) inherits all attributes from the parent class (Plant)
      (name, height, age)
    """
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        """
            Calls the constructor of the parent (Plant) class to initialize
            the common attributes: name, height, and age.
        """
        self.color: str = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    """
    The subclass (Tree) inherits all attributes from the parent class (Plant)
      (name, height, age)
    """
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        """ param trunk_diameter: diameter of the tree trunk """
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        """ The tree's ability to provide shade """
        calc: float = (self.height / 100)**2 * 3.14
        print(f"{self.name} provides {calc:.0f} square meters of shade\n")


class Vegetable(Plant):
    """
    The subclass (Vegetable) inherits all attributes from the
      parent class (Plant) (name, height, age)
    """
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """
        harvest_season : str
            harvest season example ("spring", "summer")
        nutritional_value : str
            Describes the nutritional benefits of the vegetable
        """
        super().__init__(name, height, age)
        self. harvest_season: str = harvest_season
        self. nutritional_value: str = nutritional_value


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    f1: Flower = Flower("Rose", 25, 30, "red")
    print(f"{f1.name} (Flower): {f1.height}cm, {f1.age} days, \
{f1.color} color")
    f1.bloom()
    t1: Tree = Tree("Oak", 500, 1825, 50)
    print(f"{t1.name} (Tree): {t1.height}cm, {t1.age} days, \
{t1.trunk_diameter}cm diameter")
    t1.produce_shade()
    v1: Vegetable = Vegetable("Tomato", 80,
                              90, "summer", "Tomato is rich in vitamin C")
    print(f"{v1.name} (Vegetable): {v1.height}cm, \
{v1.age} days, {v1.harvest_season} harvest")
    print(f"{v1.nutritional_value}\n")
    f2: Flower = Flower("Lily", 30, 50, "red")
    print(f"{f2.name} (Flower): {f2.height}cm, {f2.age} days, \
{f2.color} color")
    f2.bloom()
    t2: Tree = Tree("Palm", 400, 1450, 40)
    print(f"{t2.name} (Tree): {t2.height}cm, {t2.age} days, \
{t2.trunk_diameter}cm diameter")
    t2.produce_shade()
    v2: Vegetable = Vegetable("Lettuce", 20,
                              40, "spring", "Lettuce is low in calories")
    print(f"{v2.name} (Vegetable): {v2.height}cm, \
{v2.age} days, {v2.harvest_season} harvest")
    print(f"{v2.nutritional_value}")
