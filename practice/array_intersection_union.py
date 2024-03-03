arr1 = list(map(int,input("Enter array 1: ").split()))
arr2 = list(map(int,input("Enter array 2: ").split()))

intersection = sorted(list(set(arr1) & set(arr2)))
union = sorted(list(set(arr1) | set(arr2)))

print("Intersection : ",intersection)
print("Union : ",union)