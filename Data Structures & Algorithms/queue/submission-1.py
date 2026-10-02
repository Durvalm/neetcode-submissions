class Node:
    def __init__(self, val, nxt=None, prev=None):
        self.val = val
        self.nxt = nxt
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)

        self.head.nxt = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        if self.head.nxt == self.tail:
            return True
        return False
    

    def append(self, value: int) -> None:
        node = Node(value)
        prev = self.tail.prev
        self.tail.prev = node
        prev.nxt = node
        node.prev = prev 
        node.nxt = self.tail
        

    def appendleft(self, value: int) -> None:
        node = Node(value)
        nxt = self.head.nxt
        node.prev = self.head
        node.nxt = nxt
        self.head.nxt = node
        nxt.prev = node
        

    def pop(self) -> int:
        popped = self.tail.prev
        if popped == self.head:
            return -1
        prev = popped.prev
        prev.nxt = self.tail
        self.tail.prev = prev
        return popped.val
        

    def popleft(self) -> int:
        popped = self.head.nxt
        if popped == self.tail:
            return -1
        nxt = popped.nxt
        self.head.nxt = nxt
        nxt.prev = self.head
        return popped.val
        
