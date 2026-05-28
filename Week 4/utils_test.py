import utils

age = utils.get_valid_input("Enter your age: ", int)
print(age)

utils.print_header("Welcome home!")

formatted = utils.format_large_number(123456789)
print(formatted)

timestamp = utils.get_timestamp()
print(timestamp)