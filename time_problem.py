minutes = int(input("Enter minutes : "))

days = minutes//1440
hours=int((minutes%1440)/60)
min=int((minutes%1440)%60)
print(days,"days,",hours,"hours,",min,"minutes")