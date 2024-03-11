N = int(input())
arr = list(map(int,input().split()))

found = False

res = 0

for i in range(N):
    sum1 = sum(arr[:i])
    sum2 = sum(arr[i+1:])

    if sum1 == sum2:
        found = True
        res = i
        break

if not found:
    print("NOT FOUND")
else:
    print(res)