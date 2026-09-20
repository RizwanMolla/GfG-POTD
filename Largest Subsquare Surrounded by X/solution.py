class Solution:
    def largestSubsquare(self, mat):
        n = len(mat)

        right = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if mat[i][j] == 'X':
                    right[i][j] = 1
                    down[i][j] = 1

                    if j + 1 < n:
                        right[i][j] += right[i][j + 1]

                    if i + 1 < n:
                        down[i][j] += down[i + 1][j]

        ans = 0

        # Check squares
        for i in range(n):
            for j in range(n):

                size = min(right[i][j], down[i][j])

                while size > ans:

                    bottom = i + size - 1
                    last = j + size - 1

                    if (right[bottom][j] >= size and
                        down[i][last] >= size):

                        ans = size
                        break

                    size -= 1

        return ans