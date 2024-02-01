# class Midpoint:
#     def __init__(self,x1,x2,y1,y2):
#         self.x1 = x1
#         self.x2 = x2
#         self.y1 = y1
#         self.y2 = y2
#         self.m1 = (x1+x2)/2
#         self.m2 = (y1+y2)/2

#         self.midpoint = self.m1,self.m2

#     def display(self):
#         print("The midpoint is :",self.midpoint)

# x1 = int(input("Enter x1 value : "))
# x2 = int(input("Enter x2 value : "))
# x3 = int(input("Enter y1 value : "))
# x4 = int(input("Enter y2 value : "))

# x = Midpoint(x1,x2,x3,x4)
# x.display()


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"

def midpoint(p1,p2):
    mx = (p1.x+p2.x)/2
    my = (p1.y+p2.y)/2
    return Point(mx,my)

p = Point(-2,1)
q = Point(5,4)
r = midpoint(p,q)
print(str(r))
