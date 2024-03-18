N = int(input())
arr = list(map(int,input().split()))

for i in range(1,N+1):
    if i not in arr:
        print(i)