class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt


class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    

    def get(self, index: int) -> int:
        cur = self.head.nxt
        i = 0
        while cur:
            if i == index:
                return cur.val
            i += 1
            cur = cur.nxt
        return -1
        

    def insertHead(self, val: int) -> None:
        node = Node(val)

        nxt = self.head.nxt
        self.head.nxt = node
        node.nxt = nxt

        if not node.nxt:
            self.tail = node


    def insertTail(self, val: int) -> None:
        self.tail.nxt = Node(val)
        self.tail = self.tail.nxt


    def remove(self, index: int) -> bool:
        i = 0
        cur = self.head

        while i < index and cur:
            i += 1
            cur = cur.nxt

        if cur and cur.nxt:
            if cur.nxt == self.tail:
                self.tail = cur
            cur.nxt = cur.nxt.nxt
            return True
        return False


    def getValues(self) -> List[int]:
        arr = []
        cur = self.head.nxt
        while cur:
            arr.append(cur.val)
            cur = cur.nxt
        return arr
        
