def ft_count_harvest_iterative() -> None:
    size: int = int(input("Days until harvest: "))
    i: int = 1
    while (i <= size):
        print(f"Day {i}")
        i += 1
    print("Harvest time!")
