num = int(input("Enter the range : "))

first,second=0,1

for i in range(num):
    print(first,end=" ")
    first,second = second,first+second