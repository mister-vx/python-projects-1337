#!/usr/bin/python3
def garden_operations(type_error: str) -> None:
    if (type_error == "ValueError"):
        print("Testing ValueError...")
        print(int("abc"))
    if (type_error == "ZeroDivisionError"):
        print("Testing ZeroDivisionError...")
        print(20/0)
    if (type_error == "FileNotFoundError"):
        print("Testing FileNotFoundError...")
        file = open("missing.txt")
        file.close()
    if (type_error == "KeyError"):
        print("Testing KeyError...")
        p = {
            "key1": "value 1",
            "key2": "value 2",
            "key3": "value 3"
        }
        print(p["missing_plant"])
    if (type_error == "MultipleErrors"):
        print("Testing multiple errors together...")
        print(int("abc"))
        print(20/0)


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    try:
        garden_operations("ValueError")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    except Exception as err:
        print(f"{err}\n")
    try:
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    except Exception as err:
        print(f"{err}\n")
    try:
        garden_operations("FileNotFoundError")
    except FileNotFoundError as err:
        print(f"Caught FileNotFoundError: No such file '{err.filename}'\n")
    except Exception as err:
        print(f"{err}\n")
    try:
        garden_operations("KeyError")
    except KeyError as err:
        print(f"Caught KeyError: {err}\n")
    except Exception as err:
        print(f"{err}\n")
    try:
        garden_operations("MultipleErrors")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")
    except Exception as err:
        print(f"{err}\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
