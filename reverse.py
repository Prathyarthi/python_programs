num = int(input("Enter the number : "))
rem = rev = 0
for i in range(len(str(num))):         
    rem = num%10
    rev = (rev*10) + rem
    num = num//10

print(rev)

