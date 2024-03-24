import math

a,b = list(map(int,input().split()))
print(math.gcd(a,b))
print(math.lcm(a,b))

# Functions
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
def lcm(a,b):
    return (a*b)//gcd(a,b)

