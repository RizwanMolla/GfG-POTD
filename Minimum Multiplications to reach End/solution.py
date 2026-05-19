class Solution:
    def minSteps(self, arr, start, end):
        from collections import deque
        if start == end:
            return 0
        MOD = 1000
        visited = [False] * MOD
        visited[start] = True
        q = deque([start])
        steps = 1
        while q:
            for _ in range(len(q)):
                i = q.popleft()
                for a in arr:
                    j = (i * a) % MOD
                    if visited[j]:
                        continue
                    visited[j] = True
                    if j == end:
                        return steps
                    q.append(j)
            steps += 1
        return -1
