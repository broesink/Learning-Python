#ValueError > Wrong data types
int("Hello")
int("3.14")

# TypeError > Wrong datatype in operation
"hello" + 5
len(42)

# KeyError > The key doesn't exist in dictionary
person = {"Name": "James"}
person["email"]

#IndexError > index doesn't exist in the list
items = [1, 2, 3]
items[10]

#FileNotFoundError > File doesn't exist
open("non-existing-file.txt")

#ZeroDivisionError > Can't devide by 0
10 / 0

#AttributeError > Method doesn't exist on this type
42.upper()

# > When you get an error in the terminal, you'll see the error so its important to learn these error-types so you know right away what is going on