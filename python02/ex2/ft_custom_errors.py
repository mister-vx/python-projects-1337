#!/usr/bin/python3
class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def build_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def build_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        build_plant_error()
    except PlantError as err:
        print(f"Caught PlantError: {err}\n")
    try:
        print("Testing WaterError...")
        build_water_error()
    except WaterError as err:
        print(f"Caught WaterError: {err}\n")
    try:
        print("Testing catching all garden errors...")
        build_plant_error()
    except GardenError as err:
        print("Caught a garden error:", err)
    try:
        build_water_error()
    except GardenError as err:
        print(f"Caught a garden error: {err}\n")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
