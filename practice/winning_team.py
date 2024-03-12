n = int(input())
d = {}
count = 0

for i in range(n):
    string = input()

    if string in d:
        d[string] += 1
    else:
        d[string] = 1

count = max(d,key=d.get)
print(count)