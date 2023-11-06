username = []
account_no = []
limit = []

while True:
    print("1.Add 2.View")
    ch = int(input("Enter your choice : "))
    if ch==1:
        name = input("Enter your name : ")
        while True:
            acc = int(input("Enter your acc no. : "))
            confirm_acc = int(input("Enter your acc no. again : "))
            if acc==confirm_acc:
                transation_limit = int(input("Enter transaction limit : "))
                username.append(name)
                account_no.append(acc)
                limit.append(transation_limit)
                print("Beneficiary added!")
                break
            else:
                print("A/c not matched,Try again")

        print()
    elif ch==2:
        if len(username)==0:
            print("List is empty")
        else:
            print("Name\t\tAccount\t\tLimit")
            print("--------------------------------------------------")
            for i in range(len(username)):
                print("%s\t\t%d\t\t%d"%(username[i],account_no[i],limit[i]))
        
    c = input("Do you wish to continue : (y/n) ").lower()
    if c=='n':
        break


            