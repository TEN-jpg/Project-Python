class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            return "Cannot dequeue, Queue is empty"
        x = self.items.pop(0)
        return x
    
    def front(self):
        if len(self.items) == 0:
            return "Cannot peek, Queue is empty"
        return self.items[0]
    
    def rear(self):
        if len(self.items) == 0:
            return "Cannot read, Queue is empty"
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
queue = Queue()
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
print(queue.dequeue())
print(queue.front())
print(queue.rear())
print(queue.size())
print(queue.is_empty())