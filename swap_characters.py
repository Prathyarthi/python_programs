string = input("Enter the string : ")
if len(string)>2:
    first = string[0]
    second = string[-1]
    print(second + string[1:-1]+ first)
else:
    print("String is too short")