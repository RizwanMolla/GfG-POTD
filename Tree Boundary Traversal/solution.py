class Solution:
    def boundaryTraversal(self, root):
        if not root:
            return []
        
        result = []
        
        if not self.isLeaf(root):
            result.append(root.data)
        
        self.addLeftBoundary(root.left, result)
        
        self.addLeaves(root, result)
        
        self.addRightBoundary(root.right, result)
        
        return result
    
    def isLeaf(self, node):
        return not node.left and not node.right
    
    def addLeftBoundary(self, node, result):
        if not node or self.isLeaf(node):
            return
        result.append(node.data)
        if node.left:
            self.addLeftBoundary(node.left, result)
        else:
            self.addLeftBoundary(node.right, result)
    
    def addLeaves(self, node, result):
        if not node:
            return
        if self.isLeaf(node):
            result.append(node.data)
            return
        self.addLeaves(node.left, result)
        self.addLeaves(node.right, result)
    
    def addRightBoundary(self, node, result):
        if not node or self.isLeaf(node):
            return
        if node.right:
            self.addRightBoundary(node.right, result)
        else:
            self.addRightBoundary(node.left, result)
        result.append(node.data)