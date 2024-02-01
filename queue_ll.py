class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue_list:
    def __init__(self):
        self.front = None
        self.rear = None

    def enque(self):
        element = int(input("Enter element : "))
        nn = Node(element)
        # if self.front = self.rear

    def peek(self):
        if self.front is None:
            print("Queue empty")
        else:
            print(self.front.data,end=" ")

que = Queue_list()