class Solution:
    def longestSubarray(self, arr, k):
        prefix_sum = 0
        max_len = 0
        prefix_map = {}

        for i in range(len(arr)):
            prefix_sum += arr[i]

            if prefix_sum == k:
                max_len = i + 1

            if prefix_sum - k in prefix_map:
                max_len = max(max_len, i - prefix_map[prefix_sum - k])

            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i

        return max_len
