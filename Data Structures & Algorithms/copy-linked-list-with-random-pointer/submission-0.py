"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        cur = head

        hashmap = {None: None}

        while cur:
            hashmap[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            copy = hashmap[cur]
            copy.next = hashmap[cur.next]
            copy.random = hashmap[cur.random]
            cur = cur.next

        return hashmap[head]