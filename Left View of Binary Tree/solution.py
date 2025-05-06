#User function Template for python3


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
class Solution:
    def LeftView(self, root):
        # If tree is empty, return empty list
        if not root:
            return []
        
        result = []
        
        # Using level order traversal approach
        queue = [root]
        
        while queue:
            # Get number of nodes at current level
            level_size = len(queue)
            
            # Iterate through all nodes at current level
            for i in range(level_size):
                node = queue.pop(0)
                
                # Add the first node of current level to result
                if i == 0:
                    result.append(node.data)
                
                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result