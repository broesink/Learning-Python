from datetime import datetime

def get_valid_input(prompt, input_type=str):
    while True:
        try:
            user_input = input(prompt)
            converted_input = input_type(user_input)
            return converted_input
        except ValueError:
            print(f"Please enter a valid {input_type.__name__}")

def print_header(title):
    line = "=" * (len(title))
    print(line)
    print(title)
    print(line)

def format_large_number(number):
    return f"{number:,}"

def get_timestamp():
    now = datetime.now()
    return(now.strftime("%d-%m-%Y | %H:%M"))