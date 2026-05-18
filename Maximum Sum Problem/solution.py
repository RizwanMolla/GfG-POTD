class Solution:
    def maxSum(self, n):
        holdup = {}

        def solve(x):
            if x == 0:
                return 0

            if x in holdup:
                return holdup[x]

            holdup[x] = max(
                x,
                solve(x // 2) + solve(x // 3) + solve(x // 4)
            )

            return holdup[x]

        return solve(n)