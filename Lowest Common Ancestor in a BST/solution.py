class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def LCA(self, root, n1, n2):
        n1 = n1.data if isinstance(n1, Node) else n1
        n2 = n2.data if isinstance(n2, Node) else n2

        while root:
            if n1 < root.data and n2 < root.data:
                root = root.left
            elif n1 > root.data and n2 > root.data:
                root = root.right
            else:
                return root