'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
from collections import deque

class Solution:
    def isSymmetric(self, root) -> bool:
        if not root:
            return True
        
        queue = deque([(root.left, root.right)])
        
        while queue:
            left, right = queue.popleft()
            
            if not left and not right:
                continue
            if not left or not right or left.data != right.data:
                return False
            
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        
        return True