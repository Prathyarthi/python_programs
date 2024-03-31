N = int(input())

sum = 0

for i in range(1,N):
    if N%i==0:
        sum+=i

if sum==N:
    print(1)
else:
    print(sum)