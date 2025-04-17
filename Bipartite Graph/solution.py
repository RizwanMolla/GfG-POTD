from collections import deque, defaultdict

class Solution:
    def isBipartite(self, V, edges):
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        color = [-1] * V
        
        def bfs(start):
            queue = deque([start])
            color[start] = 0
            
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
            return True
        
        for i in range(V):
            if color[i] == -1:
                if not bfs(i):
                    return False
        
        return True