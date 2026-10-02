class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None

class LinkedList:
    
    def __init__(self):
        self.root = Node(-1)

    
    def get(self, index: int) -> int:
        cur = self.root.nxt
        count = 0
        while cur:
            if count == index:
                return cur.val
            cur = cur.nxt
            count += 1
        return -1

    def insertHead(self, val: int) -> None:
        node = Node(val)
        tmp = self.root.nxt
        self.root.nxt = node
        node.nxt = tmp


    def insertTail(self, val: int) -> None:
        cur = self.root
        while cur.nxt:
            cur = cur.nxt

        node = Node(val)
        cur.nxt = node
        

    def remove(self, index: int) -> bool:
        cur = self.root  # Start at the dummy node
        count = 0
        
        # Traverse to the node before the one to remove
        while cur.nxt and count < index:
            cur = cur.nxt
            count += 1
        
        # If we haven't reached the desired index, or if cur.nxt is None (index out of bounds)
        if not cur.nxt or count < index:
            return False
        
        # Remove the node by skipping it
        cur.nxt = cur.nxt.nxt
        return True
        

    def getValues(self) -> List[int]:
        arr = []
        cur = self.root.nxt
        while cur:
            arr.append(cur.val)
            cur = cur.nxt
        return arr




        
