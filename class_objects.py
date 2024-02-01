# Class is a blueprint
# Object is a instance

# class syntax : 
# class Class_name:
#       statements
#       def method(self,parameter):
#       statements

# creating object 
# syntax : obj_name = class()

# accessing members of class by using object
# syntax : obj_name.class_mem_name
# self stores the address of the objects 

# class Test:
#     name = None
#     id = None
#     def set_details(self,nm,id):
#         self.name = nm
#         self.id = id
    
#     def display(self):
#         print(f"Name : {self.name} ID : {self.id}")

# obj = Test()
# obj.set_details("Hello",123)
# obj.display()
# #creating 2nd objedt
# obj2 = Test()
# obj2.set_details("how are you",456)
# obj2.display()



# __init__ method (The class constructor) : 

class Test:
    def __init__(self,nm,id):
        self.name = nm
        self.id = id
    
    def display(self):
        print(f"Name : {self.name} \n ID : {self.id}")

obj = Test("Hello",123)
obj.display()

# Creating second object
obj2 = Test("How are you",456)
obj2.display()