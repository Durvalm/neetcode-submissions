# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = []
        self.dfs_serialize(root)
        return ",".join(self.res)
    
    def dfs_serialize(self, node):
        if not node:
            self.res.append("N")
            return
        self.res.append(str(node.val))
        self.dfs_serialize(node.left)
        self.dfs_serialize(node.right)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.vals = data.split(",")
        self.i = 0
        return self.dfs_desirialize()
    

    def dfs_desirialize(self):
        if self.vals[self.i] == "N":
            self.i += 1
            return None
        node = TreeNode(int(self.vals[self.i]))
        self.i += 1
        node.left = self.dfs_desirialize()
        node.right = self.dfs_desirialize()
        return node

        

        


