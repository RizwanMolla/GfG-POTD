import heapq

class Solution:
    def findSmallestRange(self, arr):
        # Number of lists
        k = len(arr)
        
        # Initialize min heap and track the current max value
        # Format: (value, list_index, element_index)
        min_heap = []
        current_max = float('-inf')
        
        # Initialize with the first element from each list
        for i in range(k):
            if not arr[i]:  # Skip empty lists
                continue
            heapq.heappush(min_heap, (arr[i][0], i, 0))
            current_max = max(current_max, arr[i][0])
        
        # If we don't have elements from all lists, return empty range
        if len(min_heap) < k:
            return []
        
        # Initialize the result range
        result_range = [float('-inf'), float('inf')]
        
        # Process the heap
        while len(min_heap) == k:
            # Get the current minimum
            min_val, list_idx, element_idx = heapq.heappop(min_heap)
            
            # Calculate the current range
            current_range = current_max - min_val
            
            # Update the result range if the current range is smaller
            if current_range < result_range[1] - result_range[0]:
                result_range = [min_val, current_max]
            elif current_range == result_range[1] - result_range[0] and min_val < result_range[0]:
                # If ranges are equal in size, take the one with smaller left boundary
                result_range = [min_val, current_max]
            
            # Move to the next element in the list
            if element_idx + 1 < len(arr[list_idx]):
                next_val = arr[list_idx][element_idx + 1]
                heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))
                current_max = max(current_max, next_val)
            else:
                # If we've exhausted a list, we can't form a valid range anymore
                break
        
        return result_range 