class Emp:
    def __init__(self,name,id):
        self.n = name
        self.i = id

    def display(self):
        print(self.n,self.i)

    def __len__(self):
        return len(self.n)           # Object variable name's length is returned to the object e1
    

e1 = Emp('Hello',1122)
e1.display()
print("Length of",e1.n,"is",len(e1))