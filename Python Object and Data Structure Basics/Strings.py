print("Hello World")
print("This is a string")
print("Hello\nWorld")
print(len("Hello World"))
mystring = "Hello World"
# Indexing
print(mystring[0])
# Slicing where we print the whole string. We use 11 as the slicing stops to stop-1
print(mystring[2:])
print(mystring[:10])
print(mystring[::2])
# Reversing a string
print(mystring[::-1])
print(mystring[-1:-10:-1])
print(mystring[0:11:])
print(mystring[0:11:2])
# Changing a string
name = "Sammy"
last_letters = name[1:]
name = 'P' + last_letters
print(name)
letter = 'z'
print(10 * letter)
print('2' + '3')
# Different functions of strings
print(mystring.upper())
print(mystring.upper())
print(mystring.lower())
print(mystring.split())
print(mystring.split('l'))
# Formatting a string
print("The {2} {0} {1}".format("brown", "fox", "quick"))
print("The {} {} {}\n".format("brown", "fox", "quick"))
q = "quick"
b = "brown"
f = "fox"
print(f"The {q} {b} {f}")
# Formatting using precision
result = 100 / 777
print("The result is {}".format(result))
print("The result is {r:1.5f}".format(r=result))
print("The result is {r:1.3f}".format(r=result))

