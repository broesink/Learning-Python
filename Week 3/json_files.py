import json

person = {
    "name" : "James",
    "age" : 40,
    "skills" : ["Word", "Excel", "Powerpoint"]
}

with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

with open("person.json", "r") as file:
    data = json.load(file)

print(data["name"])
print(data["skills"][0])

json_string = '{"city":"Benidorm", "country":"Spain"}'
location = json.loads(json_string)
print(location["city"])