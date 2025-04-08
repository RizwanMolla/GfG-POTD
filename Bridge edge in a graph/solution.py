class Solution:
    def isBridge(self, V, edges, c, d):
        from collections import defaultdict
        
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        disc = [-1] * V
        low = [-1] * V
        time = [0]
        found_bridge = [False]

        def dfs(u, parent):
            disc[u] = low[u] = time[0]
            time[0] += 1

            for v in adj[u]:
                if v == parent:
                    continue
                if disc[v] == -1:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        if (u == c and v == d) or (u == d and v == c):
                            found_bridge[0] = True
                else:
                    low[u] = min(low[u], disc[v])

        for i in range(V):
            if disc[i] == -1:
                dfs(i, -1)

        return found_bridge[0]