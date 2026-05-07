# Definition for Node
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class Solution:
    
    def isIdentical(self, a, b):
        
        if not a and not b:
            return True
        
        if not a or not b:
            return False
        
        return (a.data == b.data and
                self.isIdentical(a.left, b.left) and
                self.isIdentical(a.right, b.right))
    
    def isSubTree(self, root1, root2):
        
        if not root2:
            return True
        
        if not root1:
            return False
        
        if self.isIdentical(root1, root2):
            return True
        
        return (self.isSubTree(root1.left, root2) or
                self.isSubTree(root1.right, root2))