contacts = [
    {"name": "James", "phone": "6123456789", "email": "james@gmail.com", "city": "Amsterdam"},
    {"name": "David", "phone": "6987654321", "email": "david@gmail.com", "city": "Madrid"},
    {"name": "Janny", "phone": "9548623158", "email": "janny@gmail.com", "city": "Munchen"},
    {"name": "Anton", "phone": "6123321123", "email": "anton@gmail.com", "city": "Paris"},
]

for person in contacts:
    print(f"{person['name']}")

search_name = input("Search for a contact: ")

for person in contacts:
    if person["name"].lower() == search_name.lower():
        print(f"Name: {person['name']}")
        print(f"Phone: {person['phone']}")
        print(f"Email: {person['email']}")
        print(f"City: {person['city']}")
        break
else:
    print("This contact doesn't exist, sorry.")

#Let user add a new contact:
new_name = input("Enter new contact name: ")
new_phone = input("Enter phone number: ")
new_email = input("Enter email: ")
new_city = input("Enter city: ")
contacts.append({"name": new_name, "phone": new_phone, "email": new_email, "city": new_city})
print(f"\nContact {new_name} added!")

print("\nUpdated contact list:")
for person in contacts:
    print(f"{person['name']}: {person['phone']}")