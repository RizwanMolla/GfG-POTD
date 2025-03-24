class Solution:
    def matrixMultiplication(self, arr):
        N = len(arr)
        dp = [[0] * N for _ in range(N)]

        for length in range(2, N):
            for i in range(1, N - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')

                for k in range(i, j):
                    cost = dp[i][k] + dp[k+1][j] + arr[i-1] * arr[k] * arr[j]
                    dp[i][j] = min(dp[i][j], cost)

        return dp[1][N-1]