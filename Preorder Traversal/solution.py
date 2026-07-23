class Solution:
    def preOrder(self, root):
        result = []

        def dfs(node):
            if not node:
                return
            result.append(node.data)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result