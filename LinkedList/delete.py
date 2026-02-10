class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def insert_at(self, val, position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            prev = None
            count = 0
            while curr is not None and count < position:
                prev = curr
                curr = curr.next
                count += 1
            prev.next = new_node
            new_node.next = curr 

    def delete(self, val):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        if temp.next is not None:
            if temp.val == val:
                self.head = temp.next
                temp.next = None
                del(temp)
                return
            else:
                found = False
                prev = None
                while temp is not None:
                    if temp.val == val:
                        found = True
                        break
                    prev = temp
                    temp = temp.next
                
                if found:
                    prev.next = temp.next
                    del(temp)  
                else:
                    print("Node not Found")
    
            
    def traverse(self):
        if not self.head:
            print("SLL is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end=" -> ")
                curr = curr.next
            print("None")

sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
sll.delete(30)
sll.traverse()