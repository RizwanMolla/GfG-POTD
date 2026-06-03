import bisect

from collections import defaultdict

class Solution:
    def freqInRange(self, arr, queries):
        graph = defaultdict(list)
        res = []
        
        for idx, num in enumerate(arr):
            graph[num].append(idx)
        
        for st, end, x in queries:
            idxs = graph[x]
            
            i = bisect.bisect_left(idxs, st)
            j = bisect.bisect_right(idxs, end)
            
            res.append(j - i)
        
        return res