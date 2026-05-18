names = ["Jim", "Freek", "Anna", "Thomas", "David"]

#   add and remove list items
#   names.append("Lisa") # add to the end of the list
#   names.insert(1, "Peter") # add on the second position (index 1 in this example)
#   names.insert(3, "John") # add on the fourth position (index 3 in this example)

#   names.remove("Jim") #remove specific item
#   names.pop() #remove last item
#   names.pop(0) #remove item based on index position

#   sorting
#   names.sort() #alphabetical sorting
#   names.reverse() #reverse sorting

sorting = sorted(names)

print(sorting)

print(names.index("Anna")) #on which index position is Anna in the default list?
print(sorting.index("Anna"))#on which index position is Anna in the sorted list?

print(names.count("Anna")) #how often appears Anna in the default list?
print(sorting.count("Anna")) #how often appears Anna in the sorted list?

# merge two lists

second_list = ["James", "John"]
all_names = sorted(names + second_list) #merge two lists and sort them right away
# names.extend(second_list) # or merge with .extend, no sorthing for now
print(all_names)