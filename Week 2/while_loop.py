counter = 0
while counter < 5:
    print(f"Counter: {counter}")
    counter += 1

enter_something = ""

while enter_something != "stop":
    enter_something = input("Type something (or type 'stop' to stop): ")
    print(f"You typed {enter_something}")

print("Loop stopped!")