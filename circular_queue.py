class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self,size):
        self.front = None
        self.rear = None
        self.size = size
        self.count = 0

    def is_full(self):
        return self.count == self.size
    
    def is_empty(self):
        return self.count == 0

    def enqueue(self,data):
        if self.is_full():
            print("Queue is overflow")
            return
        new_node = Node(data)



    def dequeue(self):
        if self.is_empty():
            print("Queue is underflow")
        else:
            data = self.front.data
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
                self.rear.next = self.front
            self.count -= 1
            print(data,"Deleted") 

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Peek of element",self.front.data)

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            temp = self.front
            while True:
                print(temp.data,end=" ")
                temp = temp.next
                if temp == self.front:
                    break
            print()

size = int(input("Enter size of queue : "))