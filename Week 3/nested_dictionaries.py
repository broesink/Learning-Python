#this is a dictionary with normal keys, but also keys representing a nested dictionary and a list
user = {
    "name" : "James",
    "age" : 30,
    "address" : {
        "city" : "Madrid",
        "country" : "Spain",
        "currency" : "Euro"
    },
    "skills" : ["Python", "HTML", "TailwindCSS", "JavaScript", "PHP", "WordPress"]
}

#get nested values
print(user["address"]["city"])
print(user["address"]["currency"])
print(user["skills"][0])

#loop through the skills list
for skill in user["skills"]:
    print(f"Skill: {skill}")

# A list of dictionaries, this you see a lot when working with API responses
all_users = [
    {"name": "James", "age": 40},
    {"name": "John", "age": 41},
    {"name": "Jack", "age": 42}
]

for user in all_users:
    print(f"{user['name']} is {user['age']} years old.")