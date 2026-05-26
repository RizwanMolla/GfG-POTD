class Solution:
    def minToggle(self, arr):
        n = len(arr)

        prefix_ones = [0] * (n + 1)
        for i in range(n):
            prefix_ones[i + 1] = prefix_ones[i] + arr[i]

        total_ones = prefix_ones[n]
        ans = n

        for k in range(n + 1):
            ones_left = prefix_ones[k]
            zeros_right = (n - k) - (total_ones - prefix_ones[k])

            ans = min(ans, ones_left + zeros_right)

        return ans