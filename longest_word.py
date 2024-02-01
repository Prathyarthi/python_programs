string = (input("Enter the sentence : "))
split_string = string.split()
longest = 0

for i in split_string:
    if len(i)>longest:
        longest = len(i)
    
print("Length of the longest word is :",longest)
