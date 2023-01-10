# python3 lists and methods

# create a list
my_list = [1, 2, 3, 4, 5]

#access an item in the list
print(my_list[3])

# add an item to the end of the list
my_list.append(6)

# add an item to the beginning of the list
my_list.insert(0, 0)

# remove an item from the end of the list
my_list.pop()

# remove an item from the beginning of the list
my_list.pop(0)

# remove an item from the list
my_list.remove(3)

# reverse the list
my_list.reverse()

# sort the list
my_list.sort()

# print the list
print(my_list)

# print the length of the list
print(len(my_list))

# print the index of an item in the list
print(my_list.index(5))

# print the number of times an item appears in the list
print(my_list.count(5))

# print the list as a string
print(",".join(str(x) for x in my_list))


