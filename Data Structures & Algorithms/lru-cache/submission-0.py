class Node:
    def __init__(self, key: None, val: None):
        self.key = key
        self.val = val
        self.nxt = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity    
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.nxt = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        # return val of key
        if not key in self.cache:
            return -1

        node = self.cache[key]
        # update LRU cache
        # 1- remove the item from wherever it is
        self.remove_at(node)
        # 2- add to the end self.right
        self.append(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove_at(node)
            node = Node(key, value)
            self.append(node)
            self.cache[node.key] = node
        else:
            node = Node(key, value)
            # 1- if over capacity, remove self.left item
            if len(self.cache) >= self.cap:
                lru = self.left.nxt
                self.remove_at(lru)
                del self.cache[lru.key]
            # 2- add to self.right
            self.append(node)
            self.cache[node.key] = node
    
    def remove_at(self, node):
        prev = node.prev
        nxt = node.nxt
        
        prev.nxt = nxt
        nxt.prev = prev
    
    def append(self, node):
        prev = self.right.prev
        nxt = self.right

        node.prev = prev
        prev.nxt = node
        node.nxt = nxt
        nxt.prev = node


        
        
