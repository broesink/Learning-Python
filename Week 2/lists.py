names = ["Jim", "Freek", "Anna", "Thomas", "David"]

numbers = [10, 20, 30, 40, 50]

mixed = ["hello", 42, True]

print(names[0]) #first
print(names[1]) #second
print(names[-1]) #last
print(names[-2]) #second last

print(len(names)) #number of items in the list

print("Thomas" in names) #True > Thomas exists in the list
print("Anonymous" in names) #False > Anonymous doesn't exist in the list

#Take a part of the list
print(names[1:4]) #index of the first untill the 4th (index 1, 2 & 3 - so not including the 4th)
print(names[:2]) #only take the first two items, so index 0 and 1 in this example)
print(names[2:]) #take everything starting (and including) from index 2 in this example