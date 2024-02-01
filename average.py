n = int(input("Enter the total number of values you want to enter : "))
sum = 0
for i in range(n):
    numbers = int(input("Enter the numbers to calculate average : \n"))
    sum = sum + numbers

# print("The average of",n,"numbers is : ",sum//n)
print(f"The average of {n} numbers is : {sum//n}")
