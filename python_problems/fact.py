def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*fact(num-1)
    
n = 4
result = fact(n)
print(f"The factorial of {n} is : {result}")