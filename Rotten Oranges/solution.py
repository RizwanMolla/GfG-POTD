from collections import deque

class Solution:
    def orangesRotting(self, mat):
        if not mat:
            return -1
        
        n, m = len(mat), len(mat[0])
        queue = deque()
        fresh_oranges = 0
        time = 0
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 2:
                    queue.append((i, j, 0))
                elif mat[i][j] == 1:
                    fresh_oranges += 1
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            i, j, time = queue.popleft()
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and mat[ni][nj] == 1:
                    mat[ni][nj] = 2
                    fresh_oranges -= 1
                    queue.append((ni, nj, time + 1))
        
        return time if fresh_oranges == 0 else -1