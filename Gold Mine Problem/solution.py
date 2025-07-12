class Solution:
    def maxGold(self, mat):
        if not mat or not mat[0]:
            return 0
        
        n = len(mat)
        m = len(mat[0])

        dp = [[0 for _ in range(m)] for _ in range(n)]

        for col in range(m - 1, -1, -1):
            for row in range(n):
                if col == m - 1:
                    right = 0
                else:
                    right = dp[row][col + 1]

                if row > 0 and col < m - 1:
                    right_up = dp[row - 1][col + 1]
                else:
                    right_up = 0

                if row < n - 1 and col < m - 1:
                    right_down = dp[row + 1][col + 1]
                else:
                    right_down = 0

                dp[row][col] = mat[row][col] + max(right, right_up, right_down)

        return max(dp[i][0] for i in range(n))
