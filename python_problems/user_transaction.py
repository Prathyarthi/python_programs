import random
transaction = ()
available_balance = 5000
while True:
    print("1.Todo Transaction 2.View 3.Exit")
    ch = int(input("Enter your choice : "))
    if ch==1:
        transaction_type = input("1.Deposit 2.Withdraw : ")
        if transaction_type=='1':
            amount = int(input("Enter deposit amount : "))
            available_balance = available_balance + amount
            transaction_id = random.randint(1000,2000)
            print("Transaction id :",transaction_id)
            transaction = transaction + ((transaction_id,transaction_type,amount,available_balance),)
            print("Deposit done!")
            
        elif transaction_type=='2':
            withdraw_amount = int(input("Enter the amount to withdraw : "))
            if withdraw_amount>available_balance:
                print("Insufficient balance")
            else:
                available_balance = available_balance-withdraw_amount
                print("Available balance is :",available_balance)
                transaction_id = random.randint(1000,2000)
                print("Transaction id :",transaction_id)
                transaction = transaction + ((transaction_id,transaction_type,withdraw_amount,available_balance),)
                print("Withdraw done!")


    elif ch==2:
        if len(transaction) == 0:
            print("No transaction")
        else:
            print("Transaction id  Type  Amount  Balance")
            for i in transaction:
                print(*i)
        
    elif ch==3:
        break
