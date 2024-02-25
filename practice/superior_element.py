def superior_element(arr):
    max_element = float('-inf')
    count = 0

    for i in range(len(arr)-1,-1,-1):
        if arr[i]>max_element:
            count+=1
            max_element = arr[i]

    return count

arr = list(map(int,input("Enter array: ").split()))
print(superior_element(arr))