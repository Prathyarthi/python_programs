def gcd(num1,num2):
    if num2==0:
        return num1
    else:
        return gcd(num2,num1%num2)
    

n1 = 48
n2 = 18
result = gcd(n1,n2)

print(f"The GCD of {n1} and {n2} is : {result}")

