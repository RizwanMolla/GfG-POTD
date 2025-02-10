from collections import defaultdict

class Solution:
    def sumK(self, root, k):
        self.count = 0
        self.prefix_sums = defaultdict(int)
        self.prefix_sums[0] = 1
        
        def dfs(node, current_sum):
            if not node:
                return
            current_sum += node.data
            self.count += self.prefix_sums.get(current_sum - k, 0)
            self.prefix_sums[current_sum] += 1
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            self.prefix_sums[current_sum] -= 1
        
        dfs(root, 0)
        return self.count