# If - elif - else statements
name = "Sammy"
if name == "Sammy":
    print("Hello Sammy")
elif name == "Pammy":
    print("Hello Pammy")
else:
    print("Hello Frankie")
# for loop
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
    print(num)
for num in mylist:
    if num % 2 == 0:
        print(num)
mystring = "Hello World"
for letter in mystring:
    print(letter)
tup = (1, 2, 3, 4, 5)
for item in tup:
    print(item)
mylist1 = [(1, 2), (3, 4), (5, 6), (7, 8)]
for t in mylist1:
    print(t)

# while loop
x = 0
while x < 5:
    print(f"The current value of x is {x}")
    x += 1
