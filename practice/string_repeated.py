def string_repeated(string,N):
    new_string = string*N
    return new_string

string = input("Enter string: ")
N = int(input("Enter N: "))
print(string_repeated(string,N))