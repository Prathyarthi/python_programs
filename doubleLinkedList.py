class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertFirst(self,element):
        nn = Node(element)
        if self.head == None:
            self.head = nn
        else:
            nn.right = self.head
            self.head.left = nn
            self.head = nn


    def insertEnd(self,element):
        nn = Node(element)
        if self.head == None:
            self.head = nn
        else:
            curr = self.head
            while curr.right!=None:
                curr = curr.right
            curr.right = nn
            nn.left = curr

    def removeFirst(self):
        if self.head == None:
            print("List is empty")
        else:
            curr = self.head
            self.head = curr.right
            curr.left = None
            print("Deleted the node")
            del curr

    def removeEnd(self):
        if self.head == None:
            print("List is empty")
        elif(self.head.right == None):
            curr = self.head
            self.head.right = None
            print("Deleted the node")
            del curr
        else:
            curr = self.head
            while curr.right!=None:
                prev = curr
                curr = curr.right
            prev.right = None
            del curr
    
    def search(self,key):
        if self.head == None:
            print("'Linked List is empty")
        else:
            curr = self.head
            while curr!=None:
                if curr.data == key:
                    print(f"Key Found : {key}")
                    break
                else:
                    curr = curr.right
            else:
                print("Key Not Found")

    def display(self):
        if self.head == None:
                print("'Linked List is empty")
        else:
            curr = self.head
            print("The nodes are : ")
            while curr!=None:
                print(curr.data)
                curr = curr.right


l = DoublyLinkedList()
while True:
    print("\n 1. Insert First\n 2. Insert End\n 3. Remove First\n 4. Remove End\n 5. Search a element\n 6. Display\n 7. Exit")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        element = input("Enter the element : ")
        l.insertFirst(element)
    elif ch == 2:
        element = input("Enter the element : ")
        l.insertEnd(element)
    elif ch == 3:
        l.removeFirst()
    elif ch == 4:
        l.removeEnd()
    elif ch == 5:
        key = input("Enter the element : ")
        l.search(key)
    elif ch == 6:
        l.display()
    elif ch == 7:
        break
    else: 
        print("Enter correct choice")

