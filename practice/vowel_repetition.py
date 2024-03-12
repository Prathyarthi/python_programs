string = input()
vowel = "aeiouAEIOU"

d = {}

max_element = 0

for i in string:
    if i in vowel:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

        if d[i]>max_element:
            max_element = d[i]
            res = i

print(res)