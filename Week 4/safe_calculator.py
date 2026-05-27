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

running = True

while running:
    while True:
        try:
            user_input_1 = int(input("Give your first number: "))
        except ValueError:
            print("Please enter a valid number.")
        else:
            print(f"Success, you entered {user_input_1}. Now enter your next number.")
            break

    while True:
        try:
            user_input_2 = int(input("Give your second number: "))
        except ValueError:
            print("Please enter a valid number.")
        else:
            print(f"Success, you entered {user_input_2}. Now select your operator.")
            break

    while True:
        user_input_operator = input("Select operator: +  -  *  /")

        if user_input_operator not in ["+", "-", "*", "/"]:
            print(f"{user_input_operator} is not a valid operator")
        else:
            break
    print("Perfect. Here comes the answer.")
        
    if user_input_operator == "+":
        print(f"{user_input_1} + {user_input_2} = {add(user_input_1, user_input_2)}")
    elif user_input_operator == "-":
        print(f"{user_input_1} - {user_input_2} = {subtract(user_input_1, user_input_2)}")
    elif user_input_operator == "*":
        print(f"{user_input_1} * {user_input_2} = {multiply(user_input_1, user_input_2)}")
    elif user_input_operator == "/":
        if user_input_2 == 0:
            print("Cannot divide by zero")
        else:
            print(f"{user_input_1} / {user_input_2} = {divide(user_input_1, user_input_2)}")

    while True:
        again = input("Do you want another calculation (yes/no)? ")
        if again.lower() not in ["yes", "no"]:
            print("Please type 'Yes' or 'No'.")
        elif again.lower() == "no":
            running = False
            break
        else:
            break

