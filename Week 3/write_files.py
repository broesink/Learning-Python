with open("output.txt", "w") as file:
    file.write("Hello, file!\n")
    file.write("This is the second line.\n")

with open("output.txt", "a") as file:
    file.write("With 'a' a line is added at the end of the file.\n")

lines = ["Apple\n", "Banana\n", "Strawberry\n"]
with open("fruits.txt", "w") as file:
    file.writelines(lines)

import os
if os.path.exists("output.txt"):
    print("File already exists")
else:
    print("Creating new file..")