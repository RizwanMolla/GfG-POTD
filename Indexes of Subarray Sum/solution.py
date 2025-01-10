class Solution:
    def subarraySum(self, arr, target):
        n = len(arr)
        left = 0
        current_sum = 0

        for right in range(n):
            current_sum += arr[right]
            
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1
            
            if current_sum == target:
                return [left + 1, right + 1]  
        
        return [-1]
