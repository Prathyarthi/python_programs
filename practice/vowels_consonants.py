string = input()
vowels = "aeiouAEIOU"

vowel_count = 0
consonant_count = 0

for i in string:
    if i.isalpha():
        if i in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(vowel_count)
print(consonant_count)