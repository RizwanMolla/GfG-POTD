'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def __init__(self):
        self.vaccine_count = 0
    
    def supplyVaccine(self, root):
        def dfs(node):
            if not node:
                return 2
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left == 0 or right == 0:
                self.vaccine_count += 1
                return 1
            
            if left == 1 or right == 1:
                return 2
            
            return 0
        
        if dfs(root) == 0:
            self.vaccine_count += 1
        
        return self.vaccine_count