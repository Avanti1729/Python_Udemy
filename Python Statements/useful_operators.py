for num in range(10):
    print(num)
for num in range(0, 11, 2):
    print(num)
print(list(range(0, 11, 2)))
for item in enumerate('abcde'):
    print(item)
mylist = [1, 2, 3]
mylist1 = ['a', 'b', 'c']

for item in zip(mylist, mylist1):
    print(item)

print(max(mylist))
print(min(mylist))
