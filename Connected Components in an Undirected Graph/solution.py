from collections import defaultdict

class Solution:
    def getComponents(self, V, edges):
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * V
        components = []
        
        def dfs(node, component):
            visited[node] = True
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component)
        
        for i in range(V):
            if not visited[i]:
                component = []
                dfs(i, component)
                components.append(sorted(component))
        
        return sorted(components)