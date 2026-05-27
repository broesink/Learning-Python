#Python comes with a big library (stdlib), filled with modules that can be used without installing pip. The following are ones that i will be using on my projects

import os
import sys
import random
from datetime import datetime

#Time and Date related
now = datetime.now()
print(now.strftime("%d-%m-%Y"))
print(now.strftime("%H:%M"))
print(now.day, now.month, now.year)

#OS (Operating system) > Files and folders
print(os.getcwd())
print(os.path.exists("data.json"))
#os.makedirs("output", exist_ok=True) >create a folder and don't crash when it already exists
print(os.path.join("output", "data.csv")) #join two paths

# Random
print(random.randint(1,100))
print(random.choice(["a","b","c"]))
random.shuffle([1,2,3,4,5]) #shuffle items in a list

# sys, stop program with exitcode
if not os.path.exists("config.json"):
    print("Error: config.json not found!")
    sys.exit(1)