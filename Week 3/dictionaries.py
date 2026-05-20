person = {
    "name": "James",
    "age" : 40,
    "city" : "Amsterdam",
    "is_developer" : True
}

#in Python you use the keys to get the data out of a dictionaries
print(person["age"])

#change the value
person["age"] = 41

#add a key/value pair
person["hobby"] = "Python"

#delete a key
del person["city"]

print(person)

print(person["hobby"])

#check if a key exists
print("name" in person)

#check the number of key/value pairs
print(len(person))