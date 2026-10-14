count = 0

try:
    with open("auth.log", "r") as file:
        for v in file:
            if "Failed password" in v:
                count = count + 1
    print(f"Total invalid attempts: {count}")
except FileNotFoundError:
    print("Error: File not found")

