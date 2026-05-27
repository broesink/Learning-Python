#Try / except is a python way of saying, try this and if it fails, do this (so you prevent crashing)

#without Try/Except the following will make the script crash if the user types "A B C":
#number = int(input("Enter a number: "))

#avoid crashing using try/except:
try:
    number = int(input("Enter a number: "))
    print(f"Your number doubled: {number * 2}")
except:
    print("That's not a valid number")

#you can also place it in a loop, so it keeps asking untill the input is valid:
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except:
        print("That's not a valid number")
print(f"Your number doubled: {number * 2}")