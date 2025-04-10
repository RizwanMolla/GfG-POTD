import heapq

class Solution:
    def minCost(self, houses):
        n = len(houses)
        in_mst = [False] * n
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        heap = [(0, 0)]
        total_cost = 0

        while heap:
            cost, u = heapq.heappop(heap)
            if in_mst[u]:
                continue
            in_mst[u] = True
            total_cost += cost

            for v in range(n):
                if not in_mst[v]:
                    dist = abs(houses[u][0] - houses[v][0]) + abs(houses[u][1] - houses[v][1])
                    if dist < min_dist[v]:
                        min_dist[v] = dist
                        heapq.heappush(heap, (dist, v))

        return total_cost