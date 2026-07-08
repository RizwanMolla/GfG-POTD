from collections import deque

class Solution:
    def countCoordinates(self, a):
        n = len(a)
        m = len(a[0])

        v1 = [[False] * m for _ in range(n)]
        v2 = [[False] * m for _ in range(n)]

        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(s, v):
            q = deque(s)

            while q:
                x, y = q.popleft()

                for dx, dy in d:
                    i, j = x + dx, y + dy

                    if (0 <= i < n and 0 <= j < m and
                        not v[i][j] and
                        a[i][j] >= a[x][y]):
                        v[i][j] = True
                        q.append((i, j))

        s1 = []
        s2 = []

        for j in range(m):
            if not v1[0][j]:
                v1[0][j] = True
                s1.append((0, j))

            if not v2[n - 1][j]:
                v2[n - 1][j] = True
                s2.append((n - 1, j))

        for i in range(n):
            if not v1[i][0]:
                v1[i][0] = True
                s1.append((i, 0))

            if not v2[i][m - 1]:
                v2[i][m - 1] = True
                s2.append((i, m - 1))

        bfs(s1, v1)
        bfs(s2, v2)

        c = 0
        for i in range(n):
            for j in range(m):
                if v1[i][j] and v2[i][j]:
                    c += 1

        return c