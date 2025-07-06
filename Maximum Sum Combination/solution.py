import heapq

class Solution:
    def topKSumPairs(self, a, b, k):
        a.sort(reverse=True)
        b.sort(reverse=True)

        n = len(a)
        result = []
        visited = set()

        # Max heap using negative values
        heap = [(-(a[0] + b[0]), 0, 0)]
        visited.add((0, 0))

        for _ in range(k):
            current_sum, i, j = heapq.heappop(heap)
            result.append(-current_sum)

            if i + 1 < n and (i + 1, j) not in visited:
                heapq.heappush(heap, (-(a[i + 1] + b[j]), i + 1, j))
                visited.add((i + 1, j))

            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(heap, (-(a[i] + b[j + 1]), i, j + 1))
                visited.add((i, j + 1))

        return result
