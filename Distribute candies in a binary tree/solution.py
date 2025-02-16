'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def __init__(self):
        self.moves = 0
    
    def postorder(self, root):
        if root is None:
            return 0
        
        left_excess = self.postorder(root.left)
        right_excess = self.postorder(root.right)
        
        self.moves += abs(left_excess) + abs(right_excess)
        
        return root.data + left_excess + right_excess - 1
    
    def distributeCandy(self, root):
        # your code here
        self.moves = 0
        self.postorder(root)
        return self.moves