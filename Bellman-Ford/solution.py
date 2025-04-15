#User function Template for python3
class Solution:
    def bellmanFord(self, V, edges, src):
        dist = [float('inf')] * V
        dist[src] = 0

        for _ in range(V - 1):
            for u, v, w in edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                return [-1]

        for i in range(V):
            if dist[i] == float('inf'):
                dist[i] = 100000000
        return dist