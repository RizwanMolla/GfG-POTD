class Solution:
    def height(self, root):
        if root is None:
            return -1
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return max(left_height, right_height) + 1