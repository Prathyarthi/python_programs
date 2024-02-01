l = []
values = int(input(f"Enter the value : "))
while values!=0:
    l.append(values)
    values = int(input(f"Enter the value : "))
print(l)

unique_list = []    

for i in l:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)