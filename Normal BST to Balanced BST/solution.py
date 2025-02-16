'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def inorderTraversal(self, root, nodes):
        if not root:
            return
        self.inorderTraversal(root.left, nodes)
        nodes.append(root)
        self.inorderTraversal(root.right, nodes)

    def sortedArrayToBST(self, nodes, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = nodes[mid]
        root.left = self.sortedArrayToBST(nodes, start, mid - 1)
        root.right = self.sortedArrayToBST(nodes, mid + 1, end)
        return root

    def balanceBST(self, root):
        nodes = []
        self.inorderTraversal(root, nodes)
        return self.sortedArrayToBST(nodes, 0, len(nodes) - 1)