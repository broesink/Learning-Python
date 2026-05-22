import requests
import time

url = "https://official-joke-api.appspot.com/random_joke"

user_input = input("Do you want to hear a joke (yes/no)? ")

while user_input.lower() == "yes":
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        setup = data["setup"]
        punchline = data["punchline"]

        print(setup)
        time.sleep(2)
        print(punchline)

        user_input = input("Do you want to hear another joke (yes/no)? ")
    else:
        print(f"Oops, something went wrong: {response.status_code}")
        user_input = input("Try again (yes/no)? ")
else:
    print("Oke, you're boring")
