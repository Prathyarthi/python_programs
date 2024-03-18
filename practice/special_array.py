N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))

flag = True

for i in range(N-1):
    if (arr[i]%2==0 and arr[i+1]%2==0) or (arr[i]%2!=0 and arr[i+1]%2!=0):
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")