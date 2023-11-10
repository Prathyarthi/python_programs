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
# f = open('biodata_write.txt','w')
# data = f.write('hello')
# # l = ["Hello World, this is Prathyarthi\n",'hello']
# # data = f.writelines(l)      # To write numerous lines,write string data into a list or tuple and pass list name into the writelines() function
# print(data)
# print("File updated successfully!")
# f.close()

# File Object Attributes : 
# file.name        # returns name of the file
# file.mode        # returns access mode of the file
# file.closed      # Returns True if the file is open otherwise false
# file.readable()  # Returns True if the file is readable
# file.writable()  # Returns True if the file is writable
# file.seekable()  # Returns True if the file is seekable


# f = open('biodata.txt','r')
# data = f.read()
# print(data)
# print(f.name)
# print(f.mode)
# print(f.closed)
# print(f.readable())
# print(f.writable())
# print(f.seekable())

# print("File read successfully!")
# f.close()


# Using with keyword
# with open('biodata.txt','r') as f:
#     data = f.read()
#     print(data)

# File positions seek
# Syntax : 
# seek(offfset,reference)

# reference determines the point for the offset. Reference can take three values : 
# 0(default) : beginning
# 1 : current position
# 2 : end

# with open('biodata.txt','rb') as f:
#     f.seek(6,0)
#     data = f.read(10)
#     print(data)

# tell()
# with open('biodata.txt','rb') as f:
#     f.seek(6,0)
#     p = f.tell()            # To know where the cursor is at
#     print(p)
#     data = f.read(10)
#     print(data)



# The OS module in Python has various methods that can be used to perform file processing operations like renaming and deleting files.

# rename() method : 
# The rename() method takes two arguments takes two arguments, the current filename and the new filename

# Syntax : 
# os.rename(old_filename,new_filename)

# remove() method : 
# Syntax : 
# os.remove(filename)
