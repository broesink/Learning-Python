import csv

#read the CSV and turn each row into a dictionary
with open("keywords.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        print(f"{row['keyword']}: {row['volume']} searches/month")

#or load it as a list for further processing
with open("keywords.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=";")
    keywords = [row for row in reader]

#lastly sort it on volume
sorted_keywords = sorted(keywords, key=lambda x: int(x["volume"]), reverse=True)
for kw in sorted_keywords:
    print(f"{kw['keyword']}: {kw['volume']}")