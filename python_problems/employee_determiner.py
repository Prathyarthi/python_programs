salary = int(input("Enter your salary : "))
if(25000<salary<40000):
    designation = 'Manager'
elif(15000<salary<=25000):
    designation = 'Accountant'
elif(10000<=salary<=15000):
    designation = 'Clerk'
else:
    designation = None

print('Your designation is :',designation)
