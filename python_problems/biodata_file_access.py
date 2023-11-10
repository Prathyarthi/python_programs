# Reading from a file : 
# f = open('biodata.txt','r')
# data = f.read()
# # data = f.read(10)
# # data = f.readline()
# # data = f.readlines()
# print(data)
# print("File read successfully!")
# f.close()




# Writing to a file : 
f = open('biodata_write.txt','w')
data = f.write('hello')
# l = ["Hello World, this is Prathyarthi"]
# data = f.writelines(l)      # To write numerous lines,write string data into a list and pass list name into the writelines() function
print(data)
print("File updated successfully!")
f.close()