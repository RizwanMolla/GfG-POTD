class Solution:
    def articulationPoints(self, V, edges):
        from collections import defaultdict
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        disc = [-1] * V
        low = [-1] * V        
        parent = [-1] * V
        ap = [False] * V      
        time = [0]           

        def dfs(u):
            children = 0
            disc[u] = low[u] = time[0]
            time[0] += 1

            for v in graph[u]:
                if disc[v] == -1:
                    parent[v] = u
                    children += 1
                    dfs(v)
                    
                    low[u] = min(low[u], low[v])

                    if parent[u] == -1 and children > 1:
                        ap[u] = True

                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap[u] = True
                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])

        for i in range(V):
            if disc[i] == -1:
                dfs(i)

        result = [i for i, is_ap in enumerate(ap) if is_ap]
        return result if result else [-1]