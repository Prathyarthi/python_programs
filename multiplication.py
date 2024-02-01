num = int(input("Enter the number : "))
for i in range(1,11):
    # print(f"{num} X {i} = {num*i}")
    print(num,"X",i,"=","%02d"%(num*i))