class Solution:
    def maximumSum(self, grid, k):
        size = len(grid)

        prefix = [[0] * (size + 1) for _ in range(size + 1)]

        for row in range(1, size + 1):
            running = 0
            for col in range(1, size + 1):
                running += grid[row - 1][col - 1]
                prefix[row][col] = prefix[row - 1][col] + running

        best = float("-inf")

        for bottom in range(k, size + 1):
            for right in range(k, size + 1):
                top = bottom - k
                left = right - k

                current = (
                    prefix[bottom][right]
                    - prefix[top][right]
                    - prefix[bottom][left]
                    + prefix[top][left]
                )

                if current > best:
                    best = current

        return best