#!/usr/bin/python3
def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    if (not plant_name):
        raise ValueError("Plant name cannot be empty!")
    if (water_level < 1):
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if (water_level > 10):
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if (sunlight_hours < 2):
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if (sunlight_hours > 12):
        raise ValueError(f"Sunlight hours \
{sunlight_hours} is too high (max 12)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        res = check_plant_health("tomato", 5, 10)
        print(f"{res}\n")
    except ValueError as err:
        print(f"Error: {err}\n")
    except Exception as err:
        print(f"{err}\n")
    print("Testing empty plant name...")
    try:
        res = check_plant_health("", 8, 10)
        print(f"{res}\n")
    except ValueError as err:
        print(f"Error: {err}\n")
    except Exception as err:
        print(f"{err}\n")
    print("Testing bad water level...")
    try:
        res = check_plant_health("tomato", 15, 10)
        print(f"{res}\n")
    except ValueError as err:
        print(f"Error: {err}\n")
    except Exception as err:
        print(f"{err}\n")
    print("Testing bad sunlight hours...")
    try:
        res = check_plant_health("tomato", 10, 0)
        print(f"{res}\n")
    except ValueError as err:
        print(f"Error: {err}\n")
    except Exception as err:
        print(f"{err}\n")
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
