import sys

if __name__ == "__main__":
    size = len(sys.argv)
    print("=== Command Quest ===")
    if (size > 1):
        print("Program name:", sys.argv[0])
        print("Arguments received:", size - 1)
        i = 1
        while (i < size):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    else:
        print("No arguments provided!")
        print("Program name:", sys.argv[0])
    print("Total arguments:", size)
