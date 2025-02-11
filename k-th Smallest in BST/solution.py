class Solution:
    def kthSmallest(self, root, k):
        self.count = 0
        self.result = -1
        
        def inOrder(node):
            if not node or self.result != -1:
                return
            inOrder(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.data
                return
            inOrder(node.right)
        
        inOrder(root)
        return self.result