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