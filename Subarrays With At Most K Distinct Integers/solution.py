class Solution:
    def atMostK(self, arr, k):
        n = len(arr)
        left = 0
        count = 0
        freq = {}
        
        for right in range(n):
            freq[arr[right]] = freq.get(arr[right], 0) + 1
            while len(freq) > k:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1
            count += right - left + 1
        
        return count

"""
atMostK calculates the number of subarrays with at most K distinct integers using a sliding window and a hash map to track frequencies.
"""