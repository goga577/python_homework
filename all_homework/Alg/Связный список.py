class Node:
    def __init__ (self,val):
        self.val = val
        self.next = next

class LinkedList:
    def __init__ (self):
        self.root = None
    def push (self, val):
        if self.root:
            p = self.root
            while p.next:
                p = p.next
        p.next = Node (val)
        else:
            self.root = Node (val)
