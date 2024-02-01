PIN = 1234
Card_number = "1234 5678 9012 3456"
balance = 1000
with open('password.txt', 'r') as f:
    password = f.read()
# password = 'hello'

username = input("Enter Username: ")
pwd = input("Enter Password: ")
if password==pwd:    
    pin = int(input("Enter pin: "))
    if pin==PIN:
        card = input("Enter card number: ")
        if Card_number==card:
            amount = int(input("Enter the amount you want to withdraw: "))
            if amount>balance:
                print("Insufficient balance")
            print("Transaction successfull!")
            balance = balance-amount
            print("Your remaining balance is :",balance)

        else:
            print("Invalid card number")
    else:
        print("Please enter correct pin")
else:
    print('Please enter correct password')
    forgot_password = input("Forgot Password? (y/n)")
    if forgot_password=='y' or forgot_password=='Y':
        new_password = input("Enter new password : ")
        confirm_password = input("Enter new password again : ")
        if new_password==confirm_password:
            with open('password.txt', 'w') as f:
                # password=new_password
                password = new_password
                f.write(password)
            print("Password updated successfully!")
        else:
            print("Password and confirm password are not same!")
    else:
        print("Thank you for banking with us!")

