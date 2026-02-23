import sys

if len(sys.argv) < 2:
    print("Error: Please provide a name as an argument.")
    print(f"Usage: python {sys.argv[0]} <name>")
    sys.exit(1)

print(f"Hello, {sys.argv[1]}!")
