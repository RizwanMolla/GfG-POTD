class Solution:
    def minRemovals(self, arr, k):
        total_sum = sum(arr)
    
        if k > total_sum:
            return -1
        
        target = total_sum - k
        n = len(arr)
        left = 0
        curr_sum = 0
        max_len = -1
        
        for right in range(n):
            curr_sum += arr[right]
            
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1
            
            if curr_sum == target:
                max_len = max(max_len, right - left + 1)
        
        if max_len == -1:
            return -1

        return n - max_len
