
from typing import Optional
from collections import deque

from typing import List

"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def Paths(self, root):
        # List to store all root-to-leaf paths
        all_paths = []
        
        # If the tree is empty
        if not root:
            return all_paths
        
        # Helper function to traverse the tree and collect paths
        def dfs(node, current_path):
            # Add current node to the path
            current_path.append(node.data)
            
            # If we reach a leaf node (no left and right children)
            if not node.left and not node.right:
                # Add a copy of the current path to results
                all_paths.append(current_path.copy())
                return
            
            # First traverse left subtree (to list left paths first)
            if node.left:
                dfs(node.left, current_path)
                # Backtrack - remove the last node after left subtree traversal
                current_path.pop()
            
            # Then traverse right subtree
            if node.right:
                dfs(node.right, current_path)
                # Backtrack - remove the last node after right subtree traversal
                current_path.pop()
        
        # Start DFS with empty path
        dfs(root, [])
        
        return all_paths