# d = {}
# print(type(d))

# d1 = {
#     'a':11,
#     'b':12,
#     'c':13
# }

# print(d1)

# Keys must be unique
# If keys are same, but values are different, latest key value pair gets stored

# d2 = {'a':11,'b':12,'b':13}
# print(d2)


# Accessing values : 
# Dictionaries cannot be sliced
# Elements are not accessed using the position index, but using the key index

# d3 = {'a':11,'b':12,'b':13}
# print(d3['a'])


# Dictionaries are mutable
# dictionary_name[key] = value

# d3['b'] = 4
# print(d3)

# Deleting a single key
# del(dictionary[key])

# To delete all keys at a time
# dictionary_name.clear()

# To delete entire dictionary
# del(dictionary_name)


# fromkeys()
# k = ['k','v','s']
# v = 1122
# d = dict.fromkeys(k,v)

# k = ['k','v','s']
# v = 1122
# d = dict.fromkeys(k)
# print(d)

# get()
# d = {'k':11,'v':22,'s':19}
# print(d.get('k',-1))
# print(d.get('y',-1))
# print(d.get('B'))
# print(d['B'])


# keys()
# d = {'k':11,'v':12,'s':19}
# for i in d.keys():
#     print(i,end=' ')

# # values
# d = {'k':11,'v':12,'s':19}
# for i in d.values():
#     print(i,end=' ')

# To display keys and values
# d = {'k':11,'v':12,'s':19}
# for i in d.items():
#     print(i,end=' ')


# d = {'k':11,'v':12,'s':19}
# for i,(j,k) in enumerate(d.items()):
#     print(i,j,k)


# pop()
# d = {'k':11,'v':12,'s':19}
# d.pop('k')
# print(d)

# popitem()
# d = {'k':11,'v':12,'s':19}
# d.popitem()
# print(d)

# update
d1 = {'k':11,'v':12,'s':19}
d2 = {'a':11,'b':12,'c':19}

print(d1,d2)
d1.update(d2)
print(d1)

# setdefault()
d = {'k':11,'v':12,'s':13}
print(d.setdefault('k',25))    # If key is present in the dictionary, its value is returned
print(d.setdefault('y',25))    # If key is not present in the dictionary, the key value pair is added onto the dictionary
print(d)

print(d.setdefault('z'))     # If no value is given to the key, None is the value for that key
print(d)

# copy()
# clear()

