
# with parameters and return
# def add(num1,num2):
#     sum = num1+num2
#     return sum

# num1 = float(input("Enter number 1 : "))
# num2 = float(input("Enter number 2 : "))

# res = add(num1,num2)
# print("Sum of %.2f and %.2f is %.2f"%(num1,num2,res))



# With parameters and no return
# def add(num1,num2):
#     sum = num1+num2
#     print("Sum of %.2f and %.2f is %.2f"%(num1,num2,sum))
    

# num1 = float(input("Enter number 1 : "))
# num2 = float(input("Enter number 2 : "))

# add(num1,num2)



# Without parameters and no return
# def add():
#     num1 = float(input("Enter number 1 : "))
#     num2 = float(input("Enter number 2 : "))
#     sum = num1 + num2
#     print("Sum of %.2f and %.2f is %.2f"%(num1,num2,sum))

# add()


# Without parameters and return
# def add():
#     num1 = float(input("Enter number 1 : "))
#     num2 = float(input("Enter number 2 : "))
#     sum = num1 + num2
#     return sum


# res = add()
# print(f"Sum of two numbers is : {res}")

# Inner functions : 
# def outer_func():
#     def inner_func():
#         print("Welcome")
#     inner_func()
# outer_func()


# Recursive Functions : 
# Base case
# Recursive case

# filter()
# def even_check(n):
#     return n%2 == 0
# numbers = range(21,30)
# even_list = list(filter(even_check,numbers))
# print(even_list)

# map()
# Syntax: map(function,sequence)

# def sqr(x):
#     return x**2
# numbers = [1,2,3,4,5]
# sq_list = list(map(sqr,numbers))
# print(sq_list)


# reduce()
# Syntax(function,sequence)
# from functools import reduce
# def add(x,y):
#     return x+y
# numbers = [1,2,3,4,5]
# res = reduce(add,numbers)
# print(res)


