from bisect import bisect_right

class Solution:
    def minimumCoins(self, arr, k):
        arr.sort()
        n = len(arr)

        # Prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        ans = float('inf')

        for i in range(n):
            rem_left = prefix[i]  # Remove all coins from 0 to i-1

            # Find first index where arr[j] > arr[i] + k
            upper = bisect_right(arr, arr[i] + k)

            # Remove coins beyond allowed max value
            # Remove (actual coin - allowed value) from each of them
            rem_right = prefix[n] - prefix[upper] - (n - upper) * (arr[i] + k)

            ans = min(ans, rem_left + rem_right)

        return ans
