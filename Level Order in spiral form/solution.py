'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''        

class Solution:
    def findSpiral(self, root):
        # Base case: if root is None, return empty list
        if not root:
            return []
        
        result = []
        
        queue = [root]
        right_to_left = True
        
        while queue:
            level_size = len(queue)
            
            current_level = []
            
            for _ in range(level_size):
                node = queue.pop(0)
                
                current_level.append(node.data)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if right_to_left:
                result.extend(current_level[::-1])
            else:
                result.extend(current_level)
            
            right_to_left = not right_to_left
        
        return result