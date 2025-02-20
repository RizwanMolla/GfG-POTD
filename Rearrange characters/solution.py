import heapq
from collections import Counter

class Solution:
    def rearrangeString(self, s):
        #code here
        freq = Counter(s)
        max_freq = max(freq.values())
        if max_freq > (len(s) + 1) // 2:
            return ""
        
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)

        result = []
        prev = (0, '')

        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)

            if prev[0] < 0:
                heapq.heappush(max_heap, prev)
            
            prev = (count + 1, char)

        return "".join(result)