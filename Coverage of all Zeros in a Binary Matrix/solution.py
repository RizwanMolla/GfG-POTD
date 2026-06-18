class Solution:
    def findCoverage(self, mat):
        n = len(mat)
        m = len(mat[0])

        left = [[0] * m for _ in range(n)]
        right = [[0] * m for _ in range(n)]
        up = [[0] * m for _ in range(n)]
        down = [[0] * m for _ in range(n)]

        # Left
        for i in range(n):
            seen = 0
            for j in range(m):
                left[i][j] = seen
                if mat[i][j] == 1:
                    seen = 1

        # Right
        for i in range(n):
            seen = 0
            for j in range(m - 1, -1, -1):
                right[i][j] = seen
                if mat[i][j] == 1:
                    seen = 1

        # Up
        for j in range(m):
            seen = 0
            for i in range(n):
                up[i][j] = seen
                if mat[i][j] == 1:
                    seen = 1

        # Down
        for j in range(m):
            seen = 0
            for i in range(n - 1, -1, -1):
                down[i][j] = seen
                if mat[i][j] == 1:
                    seen = 1

        ans = 0

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    ans += left[i][j] + right[i][j] + up[i][j] + down[i][j]

        return ans
