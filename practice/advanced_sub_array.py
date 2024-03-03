N = int(input())
size = int(input())
arr = list(map(int,input().split()))

max_sum = 0

for i in range(0,len(arr)):
    sub = arr[i:i+size]
    index = 1
    sum = 0

    for j in sub:
        sum+=j*index
        index+=1

        if sum>max_sum:
            max_sum = sum

print(max_sum)