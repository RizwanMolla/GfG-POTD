class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        count_map = {0: -1}
        max_length = 0
        diff = 0

        for i in range(n):
            if arr[i] > k:
                diff += 1
            else:
                diff -= 1

            if diff > 0:
                max_length = max(max_length, i + 1)
            elif diff - 1 in count_map:
                max_length = max(max_length, i - count_map[diff - 1])

            if diff not in count_map:
                count_map[diff] = i

        return max_length
