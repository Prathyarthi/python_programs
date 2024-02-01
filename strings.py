# msg = 'python'
# print(msg[1])

# print(msg[0:])

# name = 'python programming'
# print(name[:18])
# print(name[-3:])
# print(name[len(name)-3:])   
# print(name[::-1])
# print(len(name))
# print(name[18:0:-1])


#string methods : 
# lang = 'python'
# print(lang.isalpha())
# print(lang.isalnum())
# print(lang.isdigit())
# print(lang.startswith('p'))
# print(lang.endswith('p'))
# print(lang.isupper())
# print(lang.islower())
# print(lang.isdecimal())
# lang = ' '
# print(lang.isspace())


# name = 'Python'
# print(name.find('y'))
# print(name.replace('y','j'))


s = "welcome to programming!"
# print(s.split())
# print(s.partition('to'))
# print("-".join(s))

# print(s.lower())
# print(s.upper())
# print(s.capitalize())
# print(s.title())
# print(s.swapcase())


# s = 65
# print(chr(s))
# print(ord('A'))


# print(ord('M'))
# print(ord('A'))
# print(ord('N'))
# print(ord('O'))
# print(ord('J'))

# m = 77
# a = 65
# n = 78
# o = 79
# j = 74
# print(chr(m))
# print(chr(a))
# print(chr(n))
# print(chr(o))
# print(chr(j))


# chr() and ord()
# name = input('Enter your name : ')
# for i in name:
#     print(ord(i))

# for i in range(65,91):
#     print(chr(i),end=' ')

# string = input("Enter the string : ")
# s = string[0]
# for i in range(len(string)):
#         if s[i] == s.upper() or s[i] == s.lower():
#             string = string[:i] + "$" + string[i+1:]
#         res = s + string[1:]
# print(res)


# string = input("Enter the string : ")
# s = string[0]

# for i in string:
#         r = string.replace(string[0],"$")
# print(s+r[1:])

string = input("Enter the string : ")
if len(string)>=3:
    if string.endswith('ing'):
        print(string+"ly")
    else: 
        print(string+"ing")
else:
    print(string)