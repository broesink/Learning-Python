import json
import os

menu = ["1. Add task", "2. View tasks", "3. Mark as done", "4. Quit"]

tasks = []

if os.path.exists("tasks.json"):
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
else:
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

while True:
    
    for item in menu:
        print(item)
    print()
    choice = input("Select option 1 - 4 to continue.. ")

    if choice == "1":
        new_task = input("Add something.. ")
        tasks.append({"task": new_task, "done": False})
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)

    elif choice == "2":
        for index, task in enumerate(tasks):
            if task["done"]:
                print(index + 1, "✓", task["task"])
            else:
                print(index + 1, "✗", task["task"])

    elif choice == "3":
        edit_task = input("Which task do you want to mark as done? ")
        for task in tasks:
            if task["task"].lower() == edit_task.lower():
                task["done"] = True
                with open("tasks.json", "w") as file:
                    json.dump(tasks, file, indent=4)
                break
        else:
            print("Task not found..")

    elif choice == "4":
        break

    else:
        print("Invalid choice")