class Solution:
    def maxOnes(self, arr, k):
        left = 0
        zeros = 0
        max_len = 0
        
        for right in range(len(arr)):
            if arr[right] == 0:
                zeros += 1
            
            # If more than k zeros, shrink window
            while zeros > k:
                if arr[left] == 0:
                    zeros -= 1
                left += 1
            
            # Update max length
            max_len = max(max_len, right - left + 1)
        
        return max_len
