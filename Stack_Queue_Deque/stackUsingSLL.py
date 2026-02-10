class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class MyStack:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return -1
        popped = self.head.data
        self.head = self.head.next
        return popped
    

n = MyStack()

n.push(10)
n.push(20)
n.push(30)
print(n.pop())
