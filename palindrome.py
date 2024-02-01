num = int(input("Enter anything! : "))
temp = num
rem = rev = 0
for i in range(len(str(num))):         
    rem = num%10
    rev = (rev*10) + rem
    num = num//10

if temp==rev:
    print(f"{temp} is palindrome!")
else:
    print(f"{temp} is not a palindrome!")
