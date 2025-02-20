import heapq

class Solution:
    def nearlySorted(self, arr, k):
        n = len(arr)
        min_heap = []
        result_index = 0  

        for i in range(min(k + 1, n)):  
            heapq.heappush(min_heap, arr[i])

        for i in range(k + 1, n):
            arr[result_index] = heapq.heappop(min_heap)
            heapq.heappush(min_heap, arr[i])
            result_index += 1

        while min_heap:
            arr[result_index] = heapq.heappop(min_heap)
            result_index += 1
        
        return arr
