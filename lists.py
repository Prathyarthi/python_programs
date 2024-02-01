# l = [11,22,22,'hello',True,22,[44,55,66]]
# print(l)
# print(type(l))

# print(l[0])
# print(l[2])
# print(l[3])
# print(l[4])
# print(l[-1])


# list = [10,20,30]
# print(list*3)
# l.append('hello1')
# print(l)
# print(l.count(22))
# print(l.index(22))
# print(l.index(22,3))
# print(l.index(22,1,5))
# list = [10,20,30]
# list.insert(22,'K')
# print(list)
# list.pop()
# print(list)
# list1 = [100,20,3]
# list1.sort()
# print(list1)
# list2 = [100,20,3]
# list3 = [5,10,15]
# list2.extend(list3)
# print(list2)

# k=[]
# print(help(k.clear))


# #Cloning Lists : 
# k = [11,22,33,44]
# v = k[:]
# print(id(k))
# print(id(v))


#Looping in Lists : 
# l = [1,2,3,4]
# for i in l:
#     print(l,end=' ')

# l = [11,22,33,44,55]
# i = 0
# while i < len(l):
#     print(l[i],end=' ')
#     i = i+1

# for i in range(len(l)):
#     print(l[i],end=' ')


#enumerate() and range() function : 
# for i,j in enumerate(l):
#     print(i,j)

# for i in range(len(l)):
#     print(l[i],end=' ')

# List comprehension : 
#  Syntax : new_list = [expression for element in sequence if condition]

# l = [1,2,3,4,5]
# new_list = [i**2 for i in l]
# print(new_list)


# l = [-12,84,11,22,-1,45,4]
# positive_list = [i for i in l if i>0]
# print(sorted(positive_list))

# l = [1,2,3,4,5,6,7]
# odd_list = [i for i in l if i%2!=0]
# print(odd_list)


# read values into the list : 
# l = []
# values = int(input("Enter the number of values : "))
# for i in range(values):
#     values = int(input(f"Enter the {i+1} value : "))
#     l.append(values)
# print(l)


# l = []
# values = int(input(f"Enter the value : "))
# while values!=0:
#     l.append(values)
#     values = int(input(f"Enter the value : "))
# print(l)