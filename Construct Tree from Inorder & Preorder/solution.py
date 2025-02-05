class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, preorder):
        if not inorder or not preorder:
            return None
        
        root_val = preorder.pop(0)
        root = Node(root_val)
        mid = inorder.index(root_val)
        
        root.left = self.buildTree(inorder[:mid], preorder)
        root.right = self.buildTree(inorder[mid+1:], preorder)
        
        return root