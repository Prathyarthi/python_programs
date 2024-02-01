# item = int(input("Enter the price of the item : "))
# if(item>250):
#     item = item-40

# print("Your bill : ",item)

# One way selection
# day='Working day!'
# day_input=(input("Enter day : "))
# if(day_input=='sunday'):
#     day='Holiday!'
# print(day)

# vehicle='Car'
# number_of_people = int(input("Enter how many people are going to the trip : "))
# if(number_of_people>10):
#     vehicle = 'Bus'
    
# print(vehicle)


# Two way selection
# marks=int(input("Enter your marks :"))
# if(marks>=35):
#     print("Passed")
# else:
#     print("Fail")

# Problem
# blood_donors_age=int(input("Enter you age : "))
# blood_donors_weight=int(input("Enter you weight : "))

# if((18<=blood_donors_age<=55) and blood_donors_weight>=45):
#     # print("You are eligible to donate blood")
#     print("1")
# else:
#     # print("Sorry!,You are not eligible to donate blood")
#     print("0")

# day_input=(input("Enter day : ").lower())
# if(day_input=='sunday'):
#     print("Holiday!")
# else:
#     print("Working day!")
    
cost_price = float(input("Enter the cost price of the item : "))
selling_price = float(input("Enter the selling price of the item : "))

if(selling_price>cost_price):
    profit = selling_price-cost_price
    print('Profit :', profit)
    print('You have made a profit')
elif(selling_price==cost_price):
    print('You broke even')
else:
    loss = cost_price-selling_price
    print('Loss :%.2f' %loss)
    print('You have made a loss')






