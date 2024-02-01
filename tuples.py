# t = (1,2,3,4)
# print(t)
# print(type(t))


# Looping : 
# t = (11,22,33,44)
# for i in t:
#     print(i,end=' ')

# t1 = (11,22,33,44,55)
# i=0
# while i<len(t1):
#     print(t1[i],end=" ")
#     i = i+1


# t2 = (11,22,33,44,55)
# for i in range(len(t2)):
#     print(t2[i],end=" ")

# t3 = (11,22,33,44,55)
# for i,j in enumerate(t3):
#     print(i,j)

# immmutable
# t5 = (11,22,33,44,55)
# t5[0]=12
# print(t5)

# t6 = (11,22,33,44,55)
# print(t6[:])

# Cannot modilfy or delete individual elements in tuple : 
# k = (11,22,33,44,55)
# del(k[1])
# print(k)

# List inside the tuple is mutable
# t = ([1,2,3],True,"python",1,2,3)
# t[0][1] = 4
# t[0].append(5)
# print(t)

# Tuple Assignment : 
# Tuple to tuple
# (x,y) = (10,20)
# # Tuple to variables
# x,y = (10,20)
# # Variables to tuple
# (x,y) = 10,20

# # Unpack a tuple : 
# k = (11,22,33,44)
# s = (1,2,k,3,4)
# print(s)
# s1 = (1,2,*k,3,4)
# print(s1)

# Packing into a tuple : 
# k = 11,22,33
# print(k)
# k,v = 11,22,33


# *k,v = 11,22,33
# print(k)
# print(v)

# k,*v = 11,22,33
# print(k)
# print(v)

# *f,s,t = (11,22,33,44,55)
# print(f)
# print(s)
# print(t)


# Disposable variable(_)
# f,*_,l = (11,22,33,44,55)      # Use _ to ignore values in unpacking or looping
# print(f)
# print(l)
# print(_)


# t = (1,2,3,4,5,8,6,7)
# print(len(t))
# print(max(t))
# print(min(t))
# print(sum(t))
# print(any(t))
# print(all(t))
# print(sorted(t))      # Return sorted list, not sorted tuple
# print(reversed(t))


# print(dir(tuple))

# zip() function
# players = ["kohli" , "Rohit"]
# jerseys = [18,45]
# t = list(zip(players,jerseys))
# print(list(t))
# print(tuple(t))

# Tuple complrehension
l = [1,2,3,4,5]
d = tuple(i ** 2 for i in l)
print(d)


l1 = [-12,84,11,22,-3,0,-25]
d1 = tuple(i for i in l1 if i>0)
print(d1)

t = ()
n = int(input("Enter the number of elements :"))
for i in range(n):
    element = int(input(f"Enter {i+1} value : "))
    t = t + (element,)

print(t)