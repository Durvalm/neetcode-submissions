# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self._depth(root)

    def _depth(self, root):
        if root is None:
            return 0
        
        left = 1 + (self._depth(root.left))
        right = 1 + (self._depth(root.right))

        max_depth = max(left, right)
        return max_depth

        