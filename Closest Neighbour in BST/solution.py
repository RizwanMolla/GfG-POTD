'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        res = -1  # Default value if no such node is found
        while root:
            if root.data == k:
                return k  # Exact match
            elif root.data < k:
                res = root.data  # Update result
                root = root.right  # Try to find a closer value
            else:
                root = root.left  # Move to left subtree
        return res
