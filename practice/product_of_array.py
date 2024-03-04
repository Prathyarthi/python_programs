N = int(input())
arr = list(map(int,input().split()))

product = 1

for i in arr:
    product = product*i

print(product)