from collections import defaultdict

class Solution:
    def findMotherVertex(self, V, edges):
        # Build adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        # DFS function
        def dfs(node, visited):
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei, visited)

        # Step 1: Find candidate mother vertex
        visited = [False] * V
        candidate = -1

        for i in range(V):
            if not visited[i]:
                dfs(i, visited)
                candidate = i

        # Step 2: Verify candidate
        visited = [False] * V
        dfs(candidate, visited)

        if not all(visited):
            return -1

        # Step 3: Find smallest mother vertex
        ans = candidate
        for i in range(candidate):
            visited = [False] * V
            dfs(i, visited)
            if all(visited):
                ans = i
                break

        return ans