#User function Template for python3
import heapq

class Solution:
    def minimumPlatform(self, arr, dep):
        arr.sort()
        dep.sort()
        
        min_heap = [] 
        max_platforms = 0
        
        for i in range(len(arr)):
            while min_heap and min_heap[0] < arr[i]:
                heapq.heappop(min_heap)
            
            heapq.heappush(min_heap, dep[i])
            
            max_platforms = max(max_platforms, len(min_heap))
        
        return max_platforms