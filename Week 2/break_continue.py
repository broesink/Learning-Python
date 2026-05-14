numbers = [1, 4, 6, 7, 2, 9, 3]

for number in numbers:
    if number > 5:
        print(f"First number bigger then 5: {number}")
        break

for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)