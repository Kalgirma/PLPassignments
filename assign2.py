# starting with an empty list
my_list = []

# adding numbers one by one
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# I want 15 to be second in the list
my_list.insert(1, 15)

# now adding more numbers at the end in one go
my_list.extend([50, 60, 70])

# removing the last number (don’t need it)
my_list.pop()

# sorting everything from small to big
my_list.sort()

# checking where 30 is in the list
index_of_30 = my_list.index(30)

# final check
print("Final list:", my_list)
print("Index of 30:", index_of_30)
