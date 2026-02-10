class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def push(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    
    def pop(self):
        if self.front is None:
            return -1
        popped = self.front.data
        self.front = self.front.next
        if self.front is None: #If after popping front becomes None that means rear also becomes None
            self.rear = None
        return popped
    
ql = MyQueue()
ql.push(10)
ql.push(20)
ql.push(30)
print(ql.pop())
