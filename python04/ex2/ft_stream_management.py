import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")
    print(f"\n[STANDARD] Archive status from {archivist_id}: {status}")
    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("[STANDARD] Data transmission complete\n")
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    try:
        main()
    except BaseException as err:
        print(err)
