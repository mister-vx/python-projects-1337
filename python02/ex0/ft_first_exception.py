#!/usr/bin/python3
def check_temperature(temp_str: str) -> int | None:
    try:
        try:
            nbr: int = int(temp_str)
        except ValueError:
            print(f"Error: '{temp_str}' is not a valid number\n")
            return None
        if (nbr < 0):
            raise ValueError(f"{nbr}°C is too cold for plants (min 0°C)")
        elif (nbr > 40):
            raise ValueError(f"{nbr}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {nbr}°C is perfect for plants!\n")
            return nbr
    except ValueError as err:
        print(f"Error: {err}\n")
        return None


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    temperatures: list[str] = ["25", "abc", "100", "-50"]
    try:
        for temp in temperatures:
            print(f"Testing temperature: {temp}")
            check_temperature(temp)
    except Exception as err:
        print(err)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
