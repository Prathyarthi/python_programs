N = int(input())
arr = list(map(int,input().split()))

sum = 0

for i in arr:
    if i>=5:
        sum+=i

print(sum)