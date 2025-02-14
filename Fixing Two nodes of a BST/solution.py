'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def correctBST(self, root):
        # your code here
        first = middle = last = prev = None

        def inorder(node):
            nonlocal first, middle, last, prev
            if not node:
                return

            inorder(node.left)

            if prev and node.data < prev.data:
                if not first:
                    first = prev
                    middle = node
                else:
                    last = node

            prev = node
            inorder(node.right)

        inorder(root)

        if first and last:
            first.data, last.data = last.data, first.data
        elif first and middle:
            first.data, middle.data = middle.data, first.data
        
        return root