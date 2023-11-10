name = input("Enter name : ")
frequency = {}
for i in name:
    if i in frequency:
        frequency[i] = frequency[i] + 1
    else:
        frequency[i] = 1
print(frequency)