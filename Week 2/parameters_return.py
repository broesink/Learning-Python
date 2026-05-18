# a function can get a parameter
def salute(name):
    print(f"Hello, {name}")

salute("David")
salute("Erik")


#a function can get multiple parameters
def counter(a, b):
    return a + b

result = counter(5, 3)
print(result)
print(counter(5, 4))


#a function can also get default values
def say_hello_in_language(name, language="nl"):
    if language == "nl":
        print(f"Hallo, {name}")
    else:
        print(f"Hello, {name}")

say_hello_in_language("Jim")
say_hello_in_language("Jim", "en")


#a function can also return multiple values
def min_max(numbers):
    return min(numbers), max(numbers)

lowest, highest = min_max([5, 7, 2, 9, 13, 2])
print(f"Lowest: {lowest}, Heighest: {highest}")