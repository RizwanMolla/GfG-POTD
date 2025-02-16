from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.data))  
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("N")  

        return result

    # Function to deserialize a list and construct the tree.
    def deSerialize(self, arr):
        if not arr:
            return None
        
        root = Node(int(arr[0]))
        queue = deque([root])
        i = 1  

        while queue and i < len(arr):
            node = queue.popleft()
            
            if arr[i] != "N":
                node.left = Node(int(arr[i]))
                queue.append(node.left)
            i += 1

            if i < len(arr) and arr[i] != "N":
                node.right = Node(int(arr[i]))
                queue.append(node.right)
            i += 1
        
        return root
