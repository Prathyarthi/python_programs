string = input()
split_string = string.split()

longest = ""

for i in split_string:
    if len(i) > len(longest):
        longest = i
        
print(longest)