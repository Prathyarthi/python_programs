d = {
    'arjun':'arjun123',
    'rishab':'rishab123',
    'raj':'raj123'
}

username = input("Enter username : ")
password = input("Enter password : ")

if username in d.keys():
    if d[username] == password:
        print("You are logged in!")
    else:
        print("Password doesn't match!")
else:
    print("Username does not exist")
