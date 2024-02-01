class Circle:
    pi = 3.14159           # pi -> Class variable
    def __init__(self,r):
        self.radius = r          # radius -> object variable
                                 # r -> Local variable   
    def area(self):
        return self.pi * self.radius ** 2

c1 = Circle(3)

print(f"Area of the Circle is : {c1.area()}")