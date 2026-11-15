"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        we have a root node

        we need to copy all its neighbors and values

        and put it into a fresh node Node(.val, .neighbors.)

        we need to fill the neighbors, which indicate a recursive function

        Loop: number 1
        create Node(val1), neighbors: cant yet

        Loop: number 2 (thorugh node.neighbors)
        create Node(val2).

        repeat loop

        after that, we need to fill the neighbors
        loop through the hahsmap
        """

        hashmap = {}

        def dfs(node):
            if node in hashmap:
                return hashmap[node]
            
            copy = Node(node.val)
            hashmap[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node) if node else None

        
        