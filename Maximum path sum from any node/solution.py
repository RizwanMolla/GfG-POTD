'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxSum(self, root):
        self.max_sum = float('-inf')
        
        def maxPathSum(node):
            if not node:
                return 0
            left_sum = max(maxPathSum(node.left), 0)
            right_sum = max(maxPathSum(node.right), 0)
            current_sum = node.data + left_sum + right_sum
            self.max_sum = max(self.max_sum, current_sum)
            return node.data + max(left_sum, right_sum)
        
        maxPathSum(root)
        return self.max_sum