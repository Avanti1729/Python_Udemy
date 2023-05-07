priceLookup = {"apple": 2.99, "banana": 3.99, "papaya": 4.99}
# To display a value from a particular key
print(priceLookup["apple"])
# Dictionary with value as a list and dictionary
d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': "helloworld"}}
print(d['k1'])
print(d['k2'])
print(d['k2'][2])
print(d['k3'])
print(d['k3']['insideKey'])
print(d['k3']['insideKey'].upper())
# printing the keys
print(d.keys())
# printing the values
print(d.values())
print(d.items())
# Very Important
d = {'simplekey': "Hello"}
print(d['simplekey'])
d = {'k1': {'k2': "Hello"}}
print(d['k1']['k2'])
d = {'k1': [{'nestkey': ['this is deep', ['Hello']]}]}
print(d['k1'][0]['nestkey'][1][0])
d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['Hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])
