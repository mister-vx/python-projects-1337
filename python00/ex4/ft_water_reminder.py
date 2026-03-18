def ft_water_reminder() -> None:
    nb: int = int(input("Days since last watering: "))
    if (nb > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
