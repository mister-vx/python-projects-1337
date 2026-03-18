def ft_plant_age() -> None:
    nb: int = int(input("Enter plant age in days: "))
    if (nb > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
