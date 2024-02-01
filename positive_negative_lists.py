l = []
values = int(input(f"Enter the value : "))
while values!=0:
    l.append(values)
    values = int(input(f"Enter the value : "))
print(l)


positive_list = [i for i in l if i>=0]
print(positive_list)
negative_list = [i for i in l if i<0]
print(negative_list)