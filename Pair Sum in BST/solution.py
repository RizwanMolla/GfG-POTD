class Solution:
    def findTarget(self, root, target):
        def inorder(node, values):
            if not node:
                return
            inorder(node.left, values)
            values.append(node.data)
            inorder(node.right, values)
        
        values = []
        inorder(root, values)
        
        left, right = 0, len(values) - 1
        while left < right:
            current_sum = values[left] + values[right]
            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1
                
        return False
