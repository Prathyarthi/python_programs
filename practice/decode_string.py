def decode_string(string):
    chunks = string.split('0')

    result = ''
    
    for chunk in chunks:
        if chunk:
            letter = chr(len(chunk) + ord('A')-1)
            result+=letter

    return result

string = input("Enter the string : ")
print(decode_string(string))