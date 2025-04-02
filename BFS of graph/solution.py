#User function Template for python3
from collections import deque
from typing import List

class Solution:
    def bfs(self, adj: List[List[int]]) -> List[int]:
        n = len(adj)
        visited = [False] * n
        queue = deque([0])
        visited[0] = True
        bfs_traversal = []
        
        while queue:
            node = queue.popleft()
            bfs_traversal.append(node)
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return bfs_traversal