# # try-except
# try:
#     n = int(input("Enter numerator : "))
#     d = int(input("Enter denominator : "))
#     q = n/d
#     print("Quotient : ",q)
# except ZeroDivisionError:
#     print("Denominator can not be ZERO")
# except ValueError:
#     print("Invalid datatype")



# The else Clause
# try:
#     n = int(input("Enter numerator : "))
#     d = int(input("Enter denominator : "))
#     q = n/d
#     print("Quotient : ",q)
# except ZeroDivisionError:
#     print("Denominator can not be ZERO")
# except ValueError:
#     print("Invalid datatype")
# else:
#     print("Spiderman")


# try-except in a single block
# try:
#     n = int(input("Enter numerator : "))
#     d = int(input("Enter denominator : "))
#     q = n/d
#     print("Quotient : ",q)
# except (ZeroDivisionError,ValueError):
#     print("Zero division or invalid datatype")


# # try-except, except block without exception
# try:
#     n = int(input("Enter numerator : "))
#     d = int(input("Enter denominator : "))
#     q = n/d
#     print("Quotient : ",q)
# except ZeroDivisionError:
#     print("Denominator can not be ZERO")
# except ValueError:
#     print("Invalid datatype")
# except:
#     print("Unknown Error")


# finally block : 
# Used to define clean up actions that must be executed under all circumstances
# It is executed before leaving the try block
# The finally block is executed irrespective of whether the excpection is occured  or not

# finally block : 
try:
    print("Raising an error")
    raise ValueError
finally:
    print("In finally Block")

