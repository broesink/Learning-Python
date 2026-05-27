# helpers.py > A module that i can re-use by calling it in other files

def clean_input(text):
    """Delete white spice and convert to lower lowercase."""
    return text.strip().lower()

def format_number(number):
    """Format a number on the thousands"""
    return f"{number:,}"

def print_divider(char="-", length=40):
    """Print a seperator line"""
    print(char * length)

APP_NAME = "SEO Keyword Analyzer"
VERSION = "1.0"

#the following will only run if the current file helpers.py runs directly
#it wont run if this current file is imported in a different file
if __name__ == "__main__":
    print("Testing helpers module...")
    print(clean_input("    Hello   World  "))
    print(format_number(150000000000000))