class Solution:
    def isCycle(self, V, edges):
        from collections import defaultdict

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        visited = [False] * V
        recStack = [False] * V

        def dfs(node):
            visited[node] = True
            recStack[node] = True

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif recStack[neighbor]:
                    return True

            recStack[node] = False
            return False

        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return True

        return False