from collections import deque, defaultdict

class Solution:
    def findOrder(self, n, prerequisites):
        graph = defaultdict(list)
        in_degree = [0] * n
        
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1
        
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        
        order = []
        while queue:
            task = queue.popleft()
            order.append(task)
            
            for neighbor in graph[task]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(order) == n:
            return order
        else:
            return []