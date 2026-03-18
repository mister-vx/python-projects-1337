def main() -> None:
    try:
        file_name = "new_discovery.txt"
        print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
        print("Initializing new storage unit:", file_name)
        file = None
        file = open(file_name, 'w')
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        data_one = "[ENTRY 001] New quantum algorithm discovered\n"
        data_two = "[ENTRY 002] Efficiency increased by 347%\n"
        data_three = "[ENTRY 003] Archived by Data Archivist trainee\n"
        file.write(data_one)
        file.write(data_two)
        file.write(data_three)
        print(data_one, end="")
        print(data_two, end="")
        print(data_three, end="")
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{file_name}' ready for long-term preservation.")
    except Exception as err:
        print(err)
    finally:
        if file:
            file.close()


if __name__ == "__main__":
    main()
