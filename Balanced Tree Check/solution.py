class Solution:
    def isBalanced(self, root) -> bool:
        def checkHeight(node):
            if not node:
                return 0

            left_height = checkHeight(node.left)
            if left_height == -1:
                return -1

            right_height = checkHeight(node.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1
            
            return max(left_height, right_height) + 1

        return checkHeight(root) != -1
