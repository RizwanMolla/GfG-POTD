'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def findPreSuc(self, root, key):
        # Initialize predecessor and successor as None
        pre = suc = None
        
        # Helper function to find predecessor and successor
        def find_pre_suc(node):
            nonlocal pre, suc
            
            # Base case
            if not node:
                return
            
            # If key is found in BST
            if node.data == key:
                # For predecessor: find the maximum value in the left subtree
                if node.left:
                    temp = node.left
                    while temp.right:
                        temp = temp.right
                    pre = temp
                
                # For successor: find the minimum value in the right subtree
                if node.right:
                    temp = node.right
                    while temp.left:
                        temp = temp.left
                    suc = temp
                
                return
            
            # If key is smaller than node's key, go to left subtree
            # Current node could be a potential successor
            if key < node.data:
                suc = node
                find_pre_suc(node.left)
            
            # If key is greater than node's key, go to right subtree
            # Current node could be a potential predecessor
            else:  # key > node.key
                pre = node
                find_pre_suc(node.right)
        
        # Start the search from root
        find_pre_suc(root)
        
        # Return the predecessor and successor
        return [pre, suc]