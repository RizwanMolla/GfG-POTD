'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def inOrder(self, root):
        result = []
        self.inOrderHelper(root, result)
        return result
    
    def inOrderHelper(self, node, result):
        if node is None:
            return
        self.inOrderHelper(node.left, result)
        result.append(node.data)
        self.inOrderHelper(node.right, result)