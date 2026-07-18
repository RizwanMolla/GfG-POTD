class Solution:
    def findWays(self, matrix, k):
        MOD = 10**9 + 7
        n = len(matrix)
        m = len(matrix[0])


        suff = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                suff[i][j] = (
                    matrix[i][j]
                    + suff[i + 1][j]
                    + suff[i][j + 1]
                    - suff[i + 1][j + 1]
                )


        dp = [[[0] * m for _ in range(n)] for _ in range(k + 1)]

        for r in range(n):
            for c in range(m):
                if suff[r][c] > 0:
                    dp[1][r][c] = 1

        for rem in range(2, k + 1):
            dp_sum_row = [[0] * m for _ in range(n + 1)]
            dp_sum_col = [[0] * (m + 1) for _ in range(n)]


            for r in range(n - 1, -1, -1):
                for c in range(m - 1, -1, -1):
                    dp_sum_row[r][c] = (
                        dp[rem - 1][r][c] + dp_sum_row[r + 1][c]
                    ) % MOD

                    dp_sum_col[r][c] = (
                        dp[rem - 1][r][c] + dp_sum_col[r][c + 1]
                    ) % MOD

            for r in range(n):
                for c in range(m):
                    if suff[r][c] == 0:
                        continue

                    total = 0


                    next_r = self.findNextRow(suff, r, c, n)
                    if next_r < n:
                        total = (total + dp_sum_row[next_r][c]) % MOD

                    next_c = self.findNextCol(suff, r, c, m)
                    if next_c < m:
                        total = (total + dp_sum_col[r][next_c]) % MOD

                    dp[rem][r][c] = total

        return dp[k][0][0]

    def findNextRow(self, suff, r, c, n):
        low, high = r + 1, n
        ans = n
        target = suff[r][c]

        while low <= high:
            mid = low + (high - low) // 2
            if suff[mid][c] < target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def findNextCol(self, suff, r, c, m):
        low, high = c + 1, m
        ans = m
        target = suff[r][c]

        while low <= high:
            mid = low + (high - low) // 2
            if suff[r][mid] < target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
