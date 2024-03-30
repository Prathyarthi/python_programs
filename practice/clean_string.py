string1 = input()
string2 = input()

left = []

for i in string1:
    if i not in string2:
        left.append(i)

res = "".join(left) if left else "Empty"

print(res)