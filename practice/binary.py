n = int(input())
b = bin(n)

sum = 0

for i in b[2:]:
    if i == '1':
        sum+=int(i)

print(sum)