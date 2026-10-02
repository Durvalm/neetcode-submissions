# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, root.val)
        return self.res

    def dfs(self, root, maxVal):
        if not root:
            return 0
        
        if root.val >= maxVal:
            self.res += 1
        
        maxVal = max(maxVal, root.val)
        
        self.dfs(root.left, maxVal)
        self.dfs(root.right, maxVal)





        