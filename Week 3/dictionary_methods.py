person = {"name":"James","age":30,"city":"Madrid"}

#get > prevents crashing when key doesn't exist
print(person.get("name"))
print(person.get("email","unknown")) #if you don't place somthing like "unknown", it will output "none" when the key doesn't exist

#show all keys
print(person.keys())

#show all values
print(person.values())

#show the key/value pairs (which you will use in loops)
print(person.items())

#go through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")

#.update() > edit or add multiple values at the same time
person.update({"age":31, "hobby": "Python"})

print(person.items())

#you should always use .get when you're not sure if a key exists, especially when working with APIs