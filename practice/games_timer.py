N = int(input())
arr = list(map(int,input().split()))

res = []

for i in arr:
    res.append(i*6)

print(sum(res))