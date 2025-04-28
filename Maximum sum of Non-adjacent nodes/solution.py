#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getMaxSum(self, root):
        def dfs(node):
            if not node:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            include = node.data + left[1] + right[1]
            
            exclude = max(left) + max(right)

            return (include, exclude)

        include, exclude = dfs(root)
        return max(include, exclude)