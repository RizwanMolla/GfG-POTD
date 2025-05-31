import heapq

class Solution:
    def kthSmallest(self, matrix, k):
        """
        Approach : Min-Heap (Priority Queue)
        Time: O(k * log(min(k, n)))
        Space: O(min(k, n))
        
        This is optimal when k is small compared to n²
        """
        n = len(matrix)
        
        # Min heap: (value, row, col)
        heap = [(matrix[0][0], 0, 0)]
        visited = {(0, 0)}
        
        for _ in range(k):
            val, row, col = heapq.heappop(heap)
            
            # Add right neighbor if exists and not visited
            if col + 1 < n and (row, col + 1) not in visited:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
                visited.add((row, col + 1))
            
            # Add bottom neighbor if exists and not visited
            if row + 1 < n and (row + 1, col) not in visited:
                heapq.heappush(heap, (matrix[row + 1][col], row + 1, col))
                visited.add((row + 1, col))
        
        return val
    