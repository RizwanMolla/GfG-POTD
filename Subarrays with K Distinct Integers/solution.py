class Solution:
    def exactlyK(self, arr, k):
        def atMostK(k):
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
        
        return atMostK(k) - atMostK(k - 1)

"""
exactlyK is derived by subtracting atMostK(k - 1) from atMostK(k), as the difference gives the count of subarrays with exactly K distinct integers.
"""