import json

#You can catch specific errors seperately
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"100 / {number} = {result}")
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("You can't devide by zero!")

#You can also save and show the error, which is very handy for debugging
try:
    with open("data.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    print("File not found, starting fresh.")
    data = {}
except Exception as e:
    print(f"Unexpected error: {e}")

#Important: Always try to use except Exception as e, so you get to see the exact error, because except only will hide bugs that might take you hours to find