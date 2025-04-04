from typing import List

class Solution:
    def isCycle(self, V: int, edges: List[List[int]]) -> bool:
        parent = [-1] * V

        def find(x):
            if parent[x] == -1:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return True
            parent[rootX] = rootY
            return False

        for u, v in edges:
            if union(u, v):
                return True

        return False