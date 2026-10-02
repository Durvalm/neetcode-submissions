# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.k = k
        self.answer = None

        self._inorder(root)

        return self.answer

    def _inorder(self, root):
        if root is None:
            return

        self._inorder(root.left)

        self.count += 1

        if self.count == self.k:
            self.answer = root.val
            return

        self._inorder(root.right)
        