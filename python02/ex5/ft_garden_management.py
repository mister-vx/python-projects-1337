#!/usr/bin/python3
class GardenManager:
    def add_plant(self, name: str) -> None:
        if (not name):
            raise ValueError("Error adding plant: Plant name cannot be empty!")
        else:
            print(f"Added {name} successfully")

    def water_plants(self, plant_list: list) -> None:
        print("Opening watering system")
        try:
            for name in plant_list:
                if (not name):
                    raise ValueError("Cannot water None - invalid plant!")
                else:
                    print(f"Watering {name} - success")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plant_health(self, plant_name: str, water_level: int,
                           sunlight_hours: int) -> str:
        if (not plant_name):
            raise ValueError("Plant name cannot be empty!")
        if (water_level < 1):
            raise ValueError(f"Error checking {plant_name}: Water level \
{water_level} is too low (min 1)")
        if (water_level > 10):
            raise ValueError(f"Error checking {plant_name}: Water level \
{water_level} is too high (max 10)")
        if (sunlight_hours < 2):
            raise ValueError(f"Sunlight hours \
{sunlight_hours} is too low (min 2)")
        if (sunlight_hours > 12):
            raise ValueError(f"Sunlight hours \
{sunlight_hours} is too high (max 12)")
        return f"{plant_name}: healthy (water: \
{water_level}, sun: {sunlight_hours})"


class GardenError(Exception):
    pass


class WaterError(GardenError):
    pass


class PlantError(GardenError):
    pass


def build_water_error() -> None:
    raise WaterError("Not enough water in tank")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    obj = GardenManager()
    try:
        print("Adding plants to garden...")
        lst: list = ["tomato", "lettuce", ""]
        for i in lst:
            obj.add_plant(i)
    except ValueError as err:
        print(f"{err}\n")
    except Exception as err:
        print(err)
    try:
        print("Watering plants...")
        obj.water_plants(["tomato", "lettuce"])
    except ValueError as err:
        print(f"Error: {err}\n")
    except Exception as err:
        print(err)
    try:
        print("Checking plant health...")
        res: str = obj.check_plant_health("tomato", 5, 8)
        print(res)
        obj.check_plant_health("lettuce", 15, 8)
    except ValueError as err:
        print(f"{err}\n")
    except Exception as err:
        print(err)
    try:
        print("Testing error recovery...")
        build_water_error()
    except GardenError as err:
        print("Caught GardenError:", err)
    finally:
        print("System recovered and continuing...\n")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
