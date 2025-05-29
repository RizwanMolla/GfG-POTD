'''
class Node:
    def __init__(self, val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def sumOfLongRootToLeafPath(self, root):
        if not root:
            return 0
        
        max_length = 0
        max_sum = 0
        
        def dfs(node, current_length, current_sum):
            nonlocal max_length, max_sum
            
            if not node:
                return
            
            # Include current node in the path
            current_length += 1
            current_sum += node.data
            
            # If this is a leaf node
            if not node.left and not node.right:
                # Update if we found a longer path
                if current_length > max_length:
                    max_length = current_length
                    max_sum = current_sum
                # If same length but higher sum, update sum
                elif current_length == max_length and current_sum > max_sum:
                    max_sum = current_sum
                return
            
            # Recursively explore left and right subtrees
            if node.left:
                dfs(node.left, current_length, current_sum)
            if node.right:
                dfs(node.right, current_length, current_sum)
        
        dfs(root, 0, 0)
        return max_sum