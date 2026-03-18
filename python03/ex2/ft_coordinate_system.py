import math


def calc_distance(pos1: tuple[int, int, int],
                  pos2: tuple[int, int, int]) -> float:
    return (
        math.sqrt((pos2[0] - pos1[0])**2
                  + (pos2[1] - pos1[1])**2 + (pos2[2] - pos1[2])**2))


def parsing_coordinates(coord: str) -> tuple[int, int, int]:
    newc = coord.split(",")
    i = 0
    for c in newc:
        newc[i] = int(c)
        i += 1
    par_coord = tuple(newc)
    return par_coord


def get_coordinate(x: int | str,
                   y: int | str, z: int | str) -> tuple[int, int, int]:
    coord = (int(x), int(y), int(z))
    return coord


if __name__ == "__main__":
    try:
        is_valid_coord = True
        pos1 = ()
        pos2 = ()
        print("=== Game Coordinate System ===\n")
        pos1 = get_coordinate(0, 0, 0)
        pos2 = get_coordinate(10, 20, 5)
        print("Position created:", pos2)
        dis = calc_distance(pos1, pos2)
        print(f"Distance between {pos1} and {pos2}: {dis:.2f}\n")
    except Exception as err:
        print(err)
    try:
        coord = "3,4,0"
        par_coord = parsing_coordinates(coord)
        pos1 = get_coordinate(0, 0, 0)
        print(f'Parsing coordinates: "{coord}"')
        print("Parsed position:", par_coord)
        dis = calc_distance(pos1, par_coord)
        print(f"Distance between {pos1} and {par_coord}: {dis:.1f}\n")
    except ValueError as err:
        print("Error parsing coordinates:", err)
        message, = err.args
        print(f'Error details - Type: ValueError, Args: ("{message}",)\n')
        is_valid_coord = False
    except Exception as err:
        print(err)
    try:
        coord = "abc,def,ghi"
        print(f'Parsing invalid coordinates: "{coord}"')
        inv_corr = parsing_coordinates(coord)
    except ValueError as err:
        print("Error parsing coordinates:", err)
        message, = err.args
        print(f'Error details - Type: ValueError, Args: ("{message}",)')
    except Exception as err:
        print(err)
    try:
        if (is_valid_coord):
            print("\nUnpacking demonstration:")
            x, y, z = par_coord
            print(f"Player at x={x}, y={y}, z={z}")
            print(f"Coordinates: X={x}, Y={y}, Z={z}")
    except Exception as err:
        print(err)
