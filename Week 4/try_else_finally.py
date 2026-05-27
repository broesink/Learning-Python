import requests

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Not a valid number.")
else: #the else will only run if there is no try error
    print(f"Succes! You entered: {number}")
finally: #finally will always run, error or no error
    print("Program finished.")

# An example for try except else finally with an API call
try:
    response = requests.get(url, timeout=5) # type: ignore
    data = response.json()
except requests.exceptions.ConnectionError:
    print("No internet connection")
except requests.exceptions.Timeout:
    print("Request timed out.")
except Exception as e:
    print(f"Something went wrong: {e}")
else:
    print("Data received successfully!")
finally:
    print("This is the end of the API call.")