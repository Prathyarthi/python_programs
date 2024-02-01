number_of_days = int(input("Enter the number of days you are late to return the book : "))

if(0<number_of_days<=5):
    fine=15
    print("You have to pay the fine of $%d"%fine)

elif(number_of_days<=10):
    fine=50
    print("You have to pay the fine of $%d"%fine)

elif(10<number_of_days<30):
    fine=100
    print("You have to pay the fine of $%d"%fine)

elif(number_of_days>=30):
    fine=300
    print("You have to pay the fine of $%d,and your library's membership will be cancelled"%fine)

else:
    print("Thank you for returning the book")