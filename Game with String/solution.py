import heapq
from collections import Counter

class Solution:
    def minValue(self, s, k):
        freq = Counter(s)

        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)

        while k > 0 and max_heap:
            max_count = heapq.heappop(max_heap)
            max_count += 1
            k -= 1
            if max_count < 0:
                heapq.heappush(max_heap, max_count)

        return sum((count * count) for count in map(lambda x: -x, max_heap))
