#User function Template for python3
class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        n, m = len(grid), len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]

        # All 8 directions
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1), (1, 0),  (1, 1)]

        def dfs(x, y):
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] == 'L' and not visited[nx][ny]:
                        dfs(nx, ny)

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'L' and not visited[i][j]:
                    dfs(i, j)
                    count += 1
        return count
