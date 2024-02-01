num = int(input("Enter the number : "))

if num<=1:
    isPrime = False

else:
    isPrime = True
    for i in range(2,num):
        if num%i==0:
            isPrime = False
            break
    
if isPrime:
    print("Prime")
else:
    print("Not Prime")
