def recursive_counter(nb: int, size: int) -> None:
    if (nb > size):
        return
    print("Day", nb)
    recursive_counter(nb + 1, size)


def ft_count_harvest_recursive() -> None:
    size: int = int(input("Days until harvest: "))
    recursive_counter(1, size)
    print("Harvest time!")
