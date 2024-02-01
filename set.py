# SET
# -> No duplicate entries
# -> Unordered collection
# -> Curly braces



# empty set : 
# s = set()
# print(type(s))

# l = []
# d = {}
# print(type(l))
# print(type(d))

# Hashing technique : 
# k = {1122,21.2,'k',True,1122}
# print(k)
# v = {1122,21.2,'k',1122,True}
# print(v)

# Looping in set : 
# s = {1,2,3,4,5}
# for i in s:
#     print(i,end=' ')


# s.add(45)
# print(s)
# s.discard(4)
# print(s)
# s.pop()
# print(s)
# s.remove(2)
# print(s)

# k = {1,2,3,4}
# v = {5,6,7,8}

# k.update(v)
# print(k)

# k.union(v)    # combines into a new set
# print(k)

# k = {33,12,11,44}
# v = {33,66,44,55}
# print(k.intersection(v))


# intersection_update()
# k = {33,12,11,44}
# v = {33,66,44,55}
# k.intersection_update(v)      # Updates the k variable with the values which are same in k and v
# print(k)                        

# difference()
# k = {33,22,11,44}
# v = {33,66,44,55}
# print(k.difference(v))

# k = {33,22,11,44}
# v = {33,66,44,55}
# k.difference_update(v)
# print(k)

# k = {33,22,11,44}
# v = {33,66,44,55}
# k.symmetric_difference(v)           # Prints the set keeping only elements found in either set, but not both
# print(k^v)

# k.symmetric_difference_update(v)
# print(k)


# k = {33,111,44,22}
# v = {33,66,44,55}
# print(k.isdisjoint(v))      # Returns True if there are no elements in common

k = {33,22}
v = {33,66,22,55}
print(k.issubset(v))

print(k.issuperset(v))
print(v.issuperset(k))

# Attributes and Methods
print(dir(set))