class Solution:
    def isBST(self, root):
        def validate(node, min_val, max_val):
            if not node:
                return True
            if node.data <= min_val or node.data >= max_val:
                return False            
            return (validate(node.left, min_val, node.data) and
                    validate(node.right, node.data, max_val))    
        return validate(root, float('-inf'), float('inf'))
