def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    else:
        return a / b

message1 = "Give your first number: "
message2 = "Give your second number: "

user_input_1 = int(input(message1))
user_input_2 = int(input(message2))

division_result = divide(user_input_1, user_input_2)

print(f"{user_input_1} + {user_input_2} = {add(user_input_1, user_input_2)}")
print(f"{user_input_1} - {user_input_2} = {subtract(user_input_1, user_input_2)}")
print(f"{user_input_1} * {user_input_2} = {multiply(user_input_1, user_input_2)}")

if division_result == None:
    print("Cannot divide by zero")
else:
    print(f"{user_input_1} / {user_input_2} = {division_result}")