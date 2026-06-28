class Solution:
    def countStrings(self, n, k):
        MOD = 1000000007

        dp0 = [[0] * (k + 1) for _ in range(n + 1)]
        dp1 = [[0] * (k + 1) for _ in range(n + 1)]

        dp0[1][0] = 1
        dp1[1][0] = 1

        for i in range(2, n + 1):
            for j in range(k + 1):
                dp0[i][j] = (dp0[i - 1][j] + dp1[i - 1][j]) % MOD

                dp1[i][j] = dp0[i - 1][j]

                if j > 0:
                    dp1[i][j] = (
                        dp1[i][j] + dp1[i - 1][j - 1]
                    ) % MOD

        return (dp0[n][k] + dp1[n][k]) % MOD