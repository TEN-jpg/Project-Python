from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, item):
        self.queue.append(item)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if len(self.queue) == 0:
            return "Stack is empty"
        return self.queue.popleft()
    
    def peek(self):
        if len(self.queue) == 0:
            return "Stack is empty"
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue)
    
    def size(self):
        return len(self.queue)
    
sq = StackUsingQueue()

sq.push(100)
sq.push(200)
print(sq.queue)
print(sq.pop())
print(sq.peek())
print(sq.is_empty())
print(sq.size())  
print(sq.queue)
