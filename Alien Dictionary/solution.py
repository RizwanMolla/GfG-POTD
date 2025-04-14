#User function Template for python3
from collections import defaultdict, deque

class Solution:
    def findOrder(words):
        graph = defaultdict(list)
        in_degree = {}
        
        for word in words:
            for char in word:
                in_degree[char] = 0
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            found_diff = False
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    in_degree[w2[j]] += 1
                    found_diff = True
                    break
            
            if not found_diff and len(w1) > len(w2):
                return ""

        q = deque([char for char in in_degree if in_degree[char] == 0])
        order = []

        while q:
            char = q.popleft()
            order.append(char)
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        
        if len(order) != len(in_degree):
            return ""
        
        return ''.join(order)