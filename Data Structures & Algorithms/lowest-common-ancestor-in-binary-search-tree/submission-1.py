# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Whenever we go to the right, we record the current number as the highest ancestor
        Whenever left, we update

        we have p and q. It's a binary search tree.
        when looking, if both p and q are smaller than root, we need to go left.
        if both are bigger, we gotta go right
        if there's a split, where do we go?
        """

        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
