import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, arr, k):
        freq_map = Counter(arr)
        return [num for num, _ in heapq.nlargest(k, freq_map.items(), key=lambda x: (x[1], x[0]))]