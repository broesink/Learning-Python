import random

def attempt_counter(attempts):
    if attempts < 5:
        print(f"Excellent! You guessed it in {attempts} attempts!")
    elif attempts < 10:
        print(f"Decent! You guessed it in {attempts} attempts!")
    else:
        print(f"You can do better! You guessed it in {attempts} attempts!")
        
secret_number = random.randint(1, 100)
print(f"Guess a number between 1 and 100!")

attempts = 0

while True:
    user_input = int(input("Number: "))
    attempts += 1
    if user_input < secret_number:
        print(f"Too low, this was attempt number: {attempts}")
    elif user_input > secret_number:
        print(f"Too high, this was attempt number: {attempts}")
    else:
        break

attempt_counter(attempts)