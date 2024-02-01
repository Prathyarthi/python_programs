# enque()

que = []
front = rr = -1
size = int(input("Enter size of Queue : "))

def en_que():
    global front,rr
    if rr == size-1:
        print("Queue Overflow")
    else:
        element = int(input("Enter element to be enqueued : "))
        if rr == -1:
            front = 0
        rr = rr+1
        que.append(element)
        print(que)

# deque()
def deque():
    global front,rr
    if front == -1 or front > rr:
        print("Queue is underflow")
    else:
        element = que[front]
        front+=1
        print("Element dequeued",element)



# display()
def display():
    global front,rr
    if front == -1 or front > rr:
        print("Queue is empty")
    else:
        for i in range(front,rr+1):
            print(que[i],end=" ")
        print()


# peek()
def peek():
    global front,rr
    if front == -1 or front > rr:
        print("Queue is empty")
    else:
        print("Front element of the queue is :",que[front])


while True:
    print("1.Enqueue 2.Dequeue 3.Display 4.Peek 5.Quit")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        en_que()
    elif ch == 2:
        deque()
    elif ch == 3:
        display()
    elif ch == 4:
        peek()
    elif ch == 5:
        break
    else:
        print("Enter correct choice")

    