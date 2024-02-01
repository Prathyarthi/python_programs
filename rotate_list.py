l = []
values = int(input(f"Enter the value : "))
while values!=0:
    l.append(values)
    values = int(input(f"Enter the value : "))
print(l)

rotate = int(input("Enter how many places you want to rotate : "))

r = l[-rotate:] + l[:-rotate]    
print("Right rotated string",r)
r = l[rotate:] + l[:rotate]    
print("Left rotated string",r)