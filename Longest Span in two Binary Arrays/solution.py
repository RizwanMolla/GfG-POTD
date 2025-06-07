class Solution:
    def longestCommonSum(self, a1, a2):
        n = len(a1)
        # Step 1: Create a difference array
        diff = [a1[i] - a2[i] for i in range(n)]

        # Step 2: Use a hashmap to store first occurrence of each prefix sum
        prefix_sum_map = {}
        max_len = 0
        prefix_sum = 0

        for i in range(n):
            prefix_sum += diff[i]

            if prefix_sum == 0:
                max_len = i + 1  # from index 0 to i

            if prefix_sum in prefix_sum_map:
                # Subarray with zero sum exists from prefix_sum_map[prefix_sum] + 1 to i
                max_len = max(max_len, i - prefix_sum_map[prefix_sum])
            else:
                prefix_sum_map[prefix_sum] = i

        return max_len
