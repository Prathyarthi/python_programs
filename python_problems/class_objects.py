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

class Test:
    name = None
    id = None
    def set_details(self,nm,id):
        self.name = nm
        self.id = id
    
    def display(self):
        print(f"Name : {self.name} ID : {self.id}")

obj = Test()
obj.set_details("Hello",123)
obj.display()
