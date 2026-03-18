def ft_harvest_total() -> None:
    nb1: int = int(input("Day 1 harvest: "))
    nb2: int = int(input("Day 2 harvest: "))
    nb3: int = int(input("Day 3 harvest: "))
    total: int = nb1 + nb2 + nb3
    print(f"Total harvest: {total}")
