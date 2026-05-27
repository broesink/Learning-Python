#This is the file where i will import the helpers.py module

import helpers #this imports the entire helpers file

helpers.print_divider()

print(helpers.APP_NAME)
print(helpers.format_number(1500000))

#Import specific things from the helpers module (these now dont need the helpers prefix like when the entire helpers module is imported (above))
from helpers import print_divider, format_number

print_divider("=", 10)
print(format_number(50000))