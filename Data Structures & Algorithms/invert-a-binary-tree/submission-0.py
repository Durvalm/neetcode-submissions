# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self._invert(root)

    def _invert(self, root):
        if root is None:
            return
        
        left = root.left
        right = root.right

        root.left = right
        root.right = left

        self._invert(root.left)
        self._invert(root.right)

        return root