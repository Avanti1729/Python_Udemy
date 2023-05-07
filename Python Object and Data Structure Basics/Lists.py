mylist = ["hello", 2, "3.14", 4, 2.53]
another_list = ['hey', 'aabcde', 4, 5, 6, 9]
print(len(mylist))
# Indexing and Slicing of Lists
print(mylist[0])
print(mylist[2:])
# Concatenating two lists
newlist = mylist + another_list
print(newlist)
newlist[0] = 1
# Appending an element to the last
newlist.append("six")
print(newlist)
# Removing the last element
print(newlist.pop())
my_list = [1, 10, 9, 7321]
# Sorting a list
my_list.sort()
print(my_list)
# Reversing a list
my_list.reverse()
print(my_list)
