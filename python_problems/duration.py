num = int(input("Enter a number : "))

# num = 500

year=(int(num/365))
months=(int((num%365)/30))
days=(int(num%365)%30)

print(str(year)+" years,",str(months)+" months,",str(days)+" days")



    