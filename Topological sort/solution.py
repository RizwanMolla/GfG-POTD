from collections import deque, defaultdict

class Solution:
    def topoSort(self, V, edges):
        adj = defaultdict(list)
        in_degree = [0] * V

        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1

        queue = deque()
        for i in range(V):
            if in_degree[i] == 0:
                queue.append(i)

        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return topo_order if len(topo_order) == V else []