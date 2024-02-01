top = -1
l = []
def push(element):
    global top
    size = 5
    if top == size-1:
        print("Stack is full") 
    else:
        top+=1
        l.append(element)
        print(f"Element {element} added")
    

def pop():
    global top
    if top == -1:
        print("Stack is underflow")
    else:
        l.remove(l[top])
        top-=1
        print("Element popped")

def peek():
    global top
    if top == -1:
        print("Stack is empty")
    else:
        print("Top element :",l[top])

def display():
    global top
    if top == -1:
        print("Stack is empty")
    else:
        for i in range(top+1):
            print(l[i],end=" ")


while True:
    print("\n1. Push 2. Pop 3. Peek 4. Display 5. Exit")
    ch  = int(input("Enter yor choice : "))
    if ch == 1:
        element = input("Enter element : ")
        push(element)
    elif ch == 2:
        pop()
    elif ch == 3:
        peek()
    elif ch == 4:
        display()
    elif ch == 5:
        break
    else:
        print("Enter valid choice")

    
# Algorithm to peek an element from a linked stack
# if top == NULL,then
#     print "Stack is empty"
# else:
#     print "Top element",top.data






