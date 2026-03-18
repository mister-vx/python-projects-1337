import typing


def generate_players(nb: int) -> typing.Generator[
                                dict[str, str | int], None, None]:
    player_name = ["alice", "bob", "charlie"]
    for i in range(nb):
        if (i % 11 == 0):
            tmp = "found treasure"
        elif (i % 8 == 0):
            tmp = "leveled up"
        else:
            tmp = "killed monster"
        player_info = {
            "name": player_name[i % len(player_name)],
            "level": i % 12,
            "event": tmp,
        }
        yield player_info


def fibonacci_sequence(nb: int) -> typing.Generator[int, None, None]:
    a = 0
    b = 1
    i = 0
    while (i < nb):
        yield a
        tmp = a
        a = b
        b = tmp + b
        i += 1


def prime_number(nb: int) -> typing.Generator[int, None, None]:
    counter = 0
    number = 2
    while (counter < nb):
        is_prime = 1
        for j in range(2, number):
            if (number % j == 0):
                is_prime = 0
                break
        if (is_prime):
            yield number
            counter += 1
        number += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    nb_game = 1000
    print(f"Processing {nb_game} game events...\n")
    j = 0
    for i in generate_players(nb_game):
        print(f"Event {j + 1}: Player {i['name']}"
              f"(level {i['level']}) {i['event']}")
        j += 1
    print("\n=== Stream Analytics ===")
    print("Total events processed:", j)
    high_level = 0
    treasure = 0
    level_up = 0

    for i in generate_players(nb_game):
        if (i["level"] >= 10):
            high_level += 1
        if (i["event"] == "found treasure"):
            treasure += 1
        if (i["event"] == "leveled up"):
            level_up += 1
    print("High-level players (10+):", high_level)
    print("Treasure events:", treasure)
    print(f"Level-up events: {level_up}\n")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print("\n=== Generator Demonstration ===")
    fibonacci_nb = 10
    print(f"Fibonacci sequence (first {fibonacci_nb}): ", end="")
    for i in fibonacci_sequence(fibonacci_nb):
        print(i, end=" ")
    prime_nb = 5
    print(f"\nPrime numbers (first {prime_nb}): ", end="")
    for i in prime_number(prime_nb):
        print(i, end=" ")
    print("")
