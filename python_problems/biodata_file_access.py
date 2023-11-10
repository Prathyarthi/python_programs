# Reading from a file : 
f = open('biodata.txt','r')
data = f.read()
# data = f.read(10)
# data = f.readline()
# data = f.readlines()
print(data)
print("File read successfully!")
f.close()