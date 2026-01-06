class Solution:
    def maxSubarrayXOR(self, arr, k):
        n = len(arr)
        curr_xor = 0
        max_xor = 0

        for i, val in enumerate(arr):
            curr_xor ^= val

            if i >= k:
                curr_xor ^= arr[i - k]

            if i >= k - 1:
                if i == k - 1 or curr_xor > max_xor:
                    max_xor = curr_xor

        return max_xor
