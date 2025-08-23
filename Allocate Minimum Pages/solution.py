class Solution:
    def isPossible(self, arr, k, mid):
        students = 1
        pages_sum = 0
        
        for pages in arr:
            if pages > mid:  # A single book larger than mid → not possible
                return False
            
            if pages_sum + pages > mid:
                students += 1
                pages_sum = pages
                if students > k:
                    return False
            else:
                pages_sum += pages
        
        return True

    def findPages(self, arr, k):
        n = len(arr)
        if k > n:  # More students than books → not possible
            return -1
        
        low = max(arr)
        high = sum(arr)
        result = high
        
        while low <= high:
            mid = (low + high) // 2
            if self.isPossible(arr, k, mid):
                result = mid
                high = mid - 1  # Try for smaller max pages
            else:
                low = mid + 1   # Increase max pages
        
        return result
