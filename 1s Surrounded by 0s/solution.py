from collections import deque

class Solution:
    def cntOnes(self, grid):
        n = len(grid)
        m = len(grid[0])

        q = deque()

        # Boundary cells
        for i in range(n):
            for j in [0, m - 1]:
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 0

        for j in range(m):
            for i in [0, n - 1]:
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    q.append((nx, ny))

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1

        return count