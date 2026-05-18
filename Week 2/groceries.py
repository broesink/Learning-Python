items = []

message = "Add something to your shopping list (or type 'done' when you're finished adding items): "

new_item = input(message)

while new_item.lower() != "done":
    items.append(new_item)
    new_item = input(message)

if len(items) == 0:
    print("Your shopping list is empty!")
else:
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")

    print(f"Total: {len(items)} items")

#second addempt > works but not very clean imho
#while new_item.lower() != "done":
#    new_item = input("Add something to your shopping list (or type 'done' when you're finished adding items): ")
#    if new_item.lower() == "done":
#        print(items)
#        break
#    else:
#        items.append(new_item)


#first attempt
#while True:
#    new_item = input("Add something to your shopping list (or type 'done' when you're finished adding items): ")
#    if new_item == "done":
#        print(items)
#        break
#    else:
#        items.append(new_item)