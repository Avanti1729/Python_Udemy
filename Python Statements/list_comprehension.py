mystring = "Hello World"
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)

mylist = [letter for letter in mystring]
print(mylist)
mylist = [x for x in range(0, 11)]
print(mylist)
mylist = [x ** 2 for x in range(0, 11) if x % 2 == 0]
print(mylist)
results = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
print(results)
st = "Print out only the words that start with s in this sentence"
for word in st.split():
    if word[0] == 's' or word[0] == 'S':
        print(word)
for i in range(0, 11, 2):
    print(i)
div_by_3 = list(x for x in range(1, 51) if x % 3 == 0)
print(div_by_3)
for word in st.split():
    if len(word) % 2 == 0:
        print(word)
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
