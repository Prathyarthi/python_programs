# Converting an instance into string : 
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
            return "({0},{1})".format(self.x,self.y)
        
p = Point(12,13)
print(p)




            