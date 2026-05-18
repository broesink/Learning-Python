#normally using a for loop
numbers = [1, 2, 3, 4, 5]
#   squares = []
#   for g in numbers:
#       squares.append(g ** 2)

#the same, but using list comprehension (only one line)
squares = [g ** 2 for g in numbers]
print(squares)

#now with a condition > only double the even numbers
even_doubled = [g * 2 for g in numbers if g % 2 == 0]
print(even_doubled)

#we can also use this with strings, for example making sure all names in a list are uppercase
names = ("Jim", "james", "Anna", "david")
capitalize = [name.upper() for name in names]
print(capitalize)