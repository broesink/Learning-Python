import csv

# data as a list of dictionaries - typical format
keywords = [
    {"keyword": "python developer", "volume": 8100, "difficulty": 45},
    {"keyword": "learn python", "volume": 22000, "difficulty": 38},
    {"keyword": "python tutorial", "volume": 18000, "difficulty": 52},
]

# write to CSV - DictWriter uses keys as column-names
with open("keywords.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["keyword", "volume", "difficulty"]
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";") #added delimiter so columns are seperated correctly in EU countries
    writer.writeheader() #this writes the columns
    writer.writerows(keywords) #this writes all rows

print("Saved to keywords.csv")