class Employee:
    def __init__(self):
        print("Object created")
    
    def __del__(self):
        print("Destructor called, object deleted")

obj = Employee()
del obj            # Automatically called when the object has no references or either deleted explicitly using del keyword