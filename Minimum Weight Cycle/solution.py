import heapq

class Solution:
    def findMinCycle(self, V, edgeList):
        INF = float('inf')
        min_cycle = INF

        graph = [[] for _ in range(V)]
        for u, v, wt in edgeList:
            graph[u].append((v, wt))
            graph[v].append((u, wt))

        for u, v, wt in edgeList:
            dist = [INF] * V
            dist[u] = 0
            pq = [(0, u)]

            while pq:
                cur_wt, node = heapq.heappop(pq)

                for neighbor, edge_wt in graph[node]:
                    if (node == u and neighbor == v) or (node == v and neighbor == u):
                        continue

                    if dist[node] + edge_wt < dist[neighbor]:
                        dist[neighbor] = dist[node] + edge_wt
                        heapq.heappush(pq, (dist[neighbor], neighbor))

            if dist[v] != INF:
                min_cycle = min(min_cycle, dist[v] + wt)

        return min_cycle if min_cycle != INF else -1