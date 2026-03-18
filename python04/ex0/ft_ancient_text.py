def main() -> None:
    try:
        file_name = "ancient_fragment.txt"
        file = None
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
        print("Accessing Storage Vault:", file_name)
        file = open(file_name, 'r')
        print("Connection established...\n")
        data = file.read()
        print("RECOVERED DATA:")
        print(data)
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    finally:
        if file:
            file.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(err)
