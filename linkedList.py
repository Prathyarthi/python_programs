class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None
        print("Node Created")

class LinkedList:
    def __init__(self):
        self.head = None

    def addFirst(self,element):
        nn = Node(element)
        if self.head == None:
            self.head = nn
        else:
            nn.next = self.head
            self.head = nn

    def addEnd(self,element):
        nn = Node(element)
        if self.head == None:
            self.head = nn
        else:
            curr = self.head
            while curr.next!=None:
                curr = curr.next
            curr.next = nn

    def delFirst(self):
        if self.head == None:
            print("Linked List is empty")
        else:
            curr = self.head
            self.head = curr.next
            print("Deleted the node")
            del curr

    def delLast(self):
        if self.head == None:
            print("Linked List is empty")
        elif(self.head.next == None):
            curr = self.head
            curr.next = None
            del curr
        else:
            curr = self.head
            prev = self.head
            while curr.next!=None:
                prev = curr
                curr = curr.next
            prev.next = None
            print("Deleted the node")
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
                    curr = curr.next
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
                curr = curr.next

l = LinkedList()
while True:
    print("\n 1. Insert First\n 2. Insert End\n 3. Remove First\n 4. Remove End\n 5. Search a element\n 6. Display\n 7. Exit")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        element = input("Enter the element : ")
        l.addFirst(element)
    elif ch == 2:
        element = input("Enter the element : ")
        l.addEnd(element)
    elif ch == 3:
        l.delFirst()
    elif ch == 4:
        l.delLast()
    elif ch == 5:
        key = input("Enter the element : ")
        l.search(key)
    elif ch == 6:
        l.display()
    elif ch == 7:
        break
    else: 
        print("Enter correct choice")
