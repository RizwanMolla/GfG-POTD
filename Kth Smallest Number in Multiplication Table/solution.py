class Solution(object):
    def kthSmallest(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        # Define search range
        left, right = 1, m * n
        
        # Binary search
        while left < right:
            mid = left + (right - left) // 2
            
            # Count numbers less than or equal to mid
            count = 0
            for i in range(1, m + 1):
                # For each row, count elements <= mid
                # min(mid // i, n) gives the count in current row
                count += min(mid // i, n)
            
            # Adjust search space
            if count < k:
                left = mid + 1
            else:
                right = mid
        
        return left