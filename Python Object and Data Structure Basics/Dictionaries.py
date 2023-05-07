priceLookup = {"apple": 2.99, "banana": 3.99, "papaya": 4.99}
# To display a value from a particular key
print(priceLookup["apple"])
# Dictionary with value as a list and dictionary
d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': "helloworld"}}
print(d['k1'])
print(d['k2'])
print(d['k3'])
print(d['k3']['insideKey'])
print(d['k3']['insideKey'].upper())
# printing the keys
print(d.keys())
# printing the values
print(d.values())
print(d.items())
