class Solution:
    def maxLen(self, arr):
        prefix_sum = 0
        hashmap = {0: -1}
        max_length = 0

        for i in range(len(arr)):
            prefix_sum += 1 if arr[i] == 1 else -1

            if prefix_sum in hashmap:
                max_length = max(max_length, i - hashmap[prefix_sum])
            else:
                hashmap[prefix_sum] = i

        return max_length

"""
Overview: The solution uses the concept of a prefix sum, where 1 is added for 1 and -1 for 0. A hashmap keeps track of the first occurrence of each prefix sum. If the same prefix sum is encountered again, it indicates that the subarray between these indices has an equal number of 0s and 1s. The length of such subarrays is calculated, and the maximum length is returned. Time complexity is O(n), and space complexity is O(n).
"""