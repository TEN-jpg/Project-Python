class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "Cannot pop, stack is empty"
        x = self.items.pop()
        return x
    
    def top(self):
        if len(self.items) == 0:
            return "Cannot top, stack is empty"
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    

stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
print(stack.pop())
print(stack.top())
print(stack.size())
print(stack.is_empty())
