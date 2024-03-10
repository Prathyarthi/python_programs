string = input()

a = "abcdefghijklmnopqrstuvwxyz"

res = ""

for i in a:
    if i not in string:
        res+=i

print(res)