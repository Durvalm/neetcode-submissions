class Node:
    def __init__(self, key, val):
        self.left = None
        self.right = None
        self.key = key
        self.val = val

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if self.root is None:
            self.root = Node(key, val)
            return

        cur = self.root
        while True:
            if cur.key > key:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(key, val)
                    return 
            elif cur.key < key:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(key, val)
                    return
            else:
                cur.val = val
                return


    def get(self, key: int) -> int:
        cur = self.root
        while cur:
            if cur.key == key:
                return cur.val
            elif cur.key > key:
                cur = cur.left
            elif cur.key < key:
                cur = cur.right
        return -1



    def getMin(self) -> int:
        if self.root is None:
            return -1
        cur = self.root
        while cur.left is not None:
            cur = cur.left
        return cur.val


    def getMax(self) -> int:
        if self.root is None:
            return -1
        cur = self.root
        while cur.right is not None:
            cur = cur.right
        return cur.val


    def remove(self, key: int) -> None:
        self.root = self._remove(self.root, key)

    def _remove(self, root, key):
        if root is None:
            return None

        # Search left
        if key < root.key:
            root.left = self._remove(root.left, key)

        # Search right
        elif key > root.key:
            root.right = self._remove(root.right, key)

        # Found the node
        else:
            # Case 1: no left child
            if root.left is None:
                return root.right

            # Case 2: no right child
            elif root.right is None:
                return root.left
            # Case 3: two children
            else:
                successor = root.right

                while successor.left:
                    successor = successor.left

                root.key = successor.key
                root.val = successor.val

                root.right = self._remove(root.right, successor.key)

        return root


    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result

    def inorderTraversal(self, root: TreeNode, result: List[int]) -> None:
        if root != None:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)

