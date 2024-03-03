N = int(input())
arr = list(map(int,input().split()))

sum = 0
count = 0

for i in arr:
    sum+=i
    if sum==0:
        count+=1

print(count)
    