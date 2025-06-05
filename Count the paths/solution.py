from collections import defaultdict

class Solution:
    def countPaths(self, edges, V, src, dest):
        #Code here
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        memo = {}

        def dfs(node):
            if node == dest:
                return 1
            if node in memo:
                return memo[node]
            total_paths = 0
            for neighbor in adj[node]:
                total_paths += dfs(neighbor)
            memo[node] = total_paths
            return total_paths

        return dfs(src)