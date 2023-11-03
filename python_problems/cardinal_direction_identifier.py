# direction = input('Enter direction : ')

# if(direction=='N' or direction=='n'):
#     print('North')

# elif(direction=='S' or direction=='s'):
#     print('South')

# elif(direction=='E' or direction=='e'):
#     print('East')

# elif(direction=='W' or direction=='w'):
#     print('West')

# else:
#     print("Enter correct direction!")



# direction = input('Enter direction : ').upper()

# if(direction=='N'):
#     print('North')

# elif(direction=='S'):
#     print('South')

# elif(direction=='E'):
#     print('East')

# elif(direction=='W'):
#     print('West')

# else:
#     print("Enter correct direction!")



# for i in range(5):
#     print(i,end=' ')

# for j in range(10,16):
#     print(j,end=' ')

# for k in range(11,22,4):
#     print(k,end=' ')
    
# for l in range(22,11,-4):
#     print(l,end=' ')



num1 = int(input("Enter the range : "))
num2 = int(input("Enter the range : "))

if num1<num2:
    for i in range(num1,num2+1):
        print(i,end=' ')
else:
    for i in range(num2,num1+1):
        print(i,end=' ')

