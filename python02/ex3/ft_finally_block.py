#!/usr/bin/python3
def water_plants(plant_list: list) -> None:
    is_seccess = 0
    print("Opening watering system")
    try:
        for name in plant_list:
            if (not name):
                raise ValueError("Error: Cannot water None - invalid plant!")
            else:
                print("Watering", name)
        is_seccess = 1
    except ValueError as err:
        print(err)
    finally:
        print("Closing watering system (cleanup)")
    if (is_seccess):
        print("Watering completed successfully!\n")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    try:
        print("Testing normal watering...")
        water_plants(["tomato", "lettuce", "carrots"])
    except ValueError as err:
        print(err)
    except Exception as err:
        print(err)
    try:
        print("Testing with error...")
        water_plants(["tomato", None])
    except ValueError as err:
        print(err)
    except Exception as err:
        print(err)
    finally:
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
