def handle_errors(file_name: str) -> None:
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
        print("SUCCESS: Archive recovered - ", end="")
        print(f"``{content}''")
        print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception as err:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print(err)


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    try:
        files = ["lost_archive.txt", "classified_vault.txt",
                 "standard_archive.txt"]
        for i in files:
            handle_errors(i)
    except Exception as err:
        print(err)
    print("All crisis scenarios handled successfully. Archives secure.")
