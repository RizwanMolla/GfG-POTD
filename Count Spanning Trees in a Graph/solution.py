import numpy as np

class Solution:
    def countSpanTree(self, n, edges):
        L = np.zeros((n, n), dtype=int)
        for u, v in edges:
            L[u][u] += 1
            L[v][v] += 1
            L[u][v] -= 1
            L[v][u] -= 1
        minor = L[:-1, :-1]
        return round(np.linalg.det(minor))