age = int(input("What is your age? "))

has_license = True

if age >= 18:
    print("Adult")
else:
    print("Minor")


if age >= 18:
    print("You're an adult")
    if has_license:
        print(" and you have your license!")
    else:
        print(" you don't have a license.")
else:
    print("You're a minor")


if age >= 18 and has_license:
    print("You are 18 or older and have a license.")
else:
    print("You're a minor.")