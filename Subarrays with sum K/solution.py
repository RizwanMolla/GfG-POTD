class Solution:
    def countSubarrays(self, arr, k):
        #code here
        count = 0
        prefix_sum = 0
        prefix_map = {0: 1}
        
        for num in arr:
            prefix_sum += num
            if prefix_sum - k in prefix_map:
                count += prefix_map[prefix_sum - k]
            if prefix_sum in prefix_map:
                prefix_map[prefix_sum] += 1
            else:
                prefix_map[prefix_sum] = 1
        
        return count
    
"""
Explanation:
The solution uses a prefix sum approach with a hash map to efficiently count the number of subarrays with a sum equal to k. It maintains the running sum of the elements and checks if the difference between the current prefix sum and k exists in the hash map. If it does, the count of such subarrays is incremented by the value stored in the hash map. This ensures O(n) time complexity and O(n) space complexity.
"""
