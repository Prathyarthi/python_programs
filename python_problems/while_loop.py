# num = int(input("Enter the number : "))
# rem = rev = 0
# while num>0:        
#     rem = num%10
#     rev = (rev*10) + rem
#     num = num//10

# print(rev)


# for num in range(5):
#     print(f"Current number : {num} ")
#     if num==3:
#         print("Loop broke")
#         break
#     else:
#         print("Loop completed")


count = 0 
while count<10:
    print(f"Current count : {count}")
    count += 1
    if count>5:
        break
    else:
        print("Loop completed")