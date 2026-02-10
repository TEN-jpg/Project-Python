from collections import deque

lst = deque([])

lst.append(100)
lst.append(200)
lst.append(300)
lst.appendleft(400)
print(lst)
print(lst.pop())
print(lst.popleft())
