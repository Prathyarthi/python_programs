import random

accounts = {}
available_balance = {}
while True:
    print("1.Create Account 2.View 3.Exit")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        acc_number = random.randint(10000,20000)
        if acc_number not in accounts:
            user_name = input("Enter name : ")
            deposit = input("Enter the amount to be deposited : ")
            accounts[acc_number] = user_name
            available_balance[acc_number] = deposit
            print("Account created successfully")
    elif ch==2:
        if len(accounts)==0:
            print("No accounts")
        else:
            print("----------------------------------------")
            print("Account number\tName\tAvailable Balance")
            print("----------------------------------------")
            for i,j in accounts.items():
                print(i,j,available_balance[i],sep="\t\t")
            print("----------------------------------------")
            
    elif ch==3:
        break
