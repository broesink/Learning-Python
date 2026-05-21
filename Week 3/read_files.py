with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())

with open("notes.txt", "r") as file:
    lines = file.readlines()
    print(f"Numer of lines: {len(lines)}")