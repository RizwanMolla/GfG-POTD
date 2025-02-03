class Solution:
    def diameter(self, root):
        self.max_diameter = 0
        
        def height(node):
            if node is None:
                return -1
            left_height = height(node.left)
            right_height = height(node.right)
            self.max_diameter = max(self.max_diameter, left_height + right_height + 2)
            return max(left_height, right_height) + 1
        
        height(root)
        return self.max_diameter