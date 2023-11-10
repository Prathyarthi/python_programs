import booking.view
import booking.cancel
print("Welome to BRCTC")
d1={}
while True:
    print("1.Book Ticket? 2.View Ticket 3.Cancel Ticket 4.Exit")
    ch = int(input("Enter what you want to do?"))

    if ch == 1:
        name = input("Enter your name : ")
        age = int(input("Enter your age : "))
        source = input("Enter source : ")
        destination = input("Enter destination : ")

        d1['Name'] = name
        d1['Age'] = age
        d1['Source'] = source
        d1['Destination'] = destination

        
    elif ch == 2:
        if len(d1)==0:
            print("No tickets booked")
        else:
            booking.view.viewTicket()
            for i,j in d1.items():
                print(i,j,sep="\t\t")
                print("----------------------------------------")
    elif ch == 3:
        booking.cancel.cancelticket()
    elif ch==4:
        break

        


