from collections import deque

class Solution:

    def numberOfCells(self, r, c, u, d, mat):

        n = len(mat)
        m = len(mat[0])

        if mat[r][c] == '#':
            return 0

        INF = 10**9

        dist = [[INF] * m for _ in range(n)]

        dist[r][c] = 0

        # 0-1 BFS
        q = deque()
        q.append((r, c))

        while q:

            x, y = q.popleft()

            # Left
            if y - 1 >= 0 and mat[x][y - 1] == '.':
                if dist[x][y] < dist[x][y - 1]:
                    dist[x][y - 1] = dist[x][y]
                    q.appendleft((x, y - 1))

            # Right
            if y + 1 < m and mat[x][y + 1] == '.':
                if dist[x][y] < dist[x][y + 1]:
                    dist[x][y + 1] = dist[x][y]
                    q.appendleft((x, y + 1))

            # Up
            if x - 1 >= 0 and mat[x - 1][y] == '.':
                if dist[x][y] < dist[x - 1][y]:
                    dist[x - 1][y] = dist[x][y]
                    q.appendleft((x - 1, y))

            # Down
            if x + 1 < n and mat[x + 1][y] == '.':
                if dist[x][y] + 1 < dist[x + 1][y]:
                    dist[x + 1][y] = dist[x][y] + 1
                    q.append((x + 1, y))

        count = 0

        for x in range(n):
            for y in range(m):

                if mat[x][y] == '#':
                    continue

                down_used = dist[x][y]

                if down_used == INF:
                    continue

                up_used = down_used - (x - r)

                if down_used <= d and up_used <= u:
                    count += 1

        return count