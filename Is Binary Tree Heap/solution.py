#User Template for python3

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque

class Solution:
    def isHeap(self, root):
        if not root:
            return True
        
        queue = deque()
        queue.append(root)
        found_null = False
        
        while queue:
            current = queue.popleft()
            
            if current.left:
                if found_null or current.data < current.left.data:
                    return False
                queue.append(current.left)
            else:
                found_null = True
            
            if current.right:
                if found_null or current.data < current.right.data:
                    return False
                queue.append(current.right)
            else:
                found_null = True
        
        return True