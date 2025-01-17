class Solution:
    def longestSubarrayDivK(self, arr, k):
        remainder_map = {0: -1}
        current_sum = 0
        max_length = 0

        for i in range(len(arr)):
            current_sum += arr[i]
            remainder = current_sum % k
            if remainder < 0:
                remainder += k
            if remainder in remainder_map:
                max_length = max(max_length, i - remainder_map[remainder])
            else:
                remainder_map[remainder] = i

        return max_length
