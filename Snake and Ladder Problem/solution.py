from collections import deque

class Solution:
    def minThrows(self, n, lad, sn):
        
        jumps = {lad[i]: lad[i + 1] for i in range(0, len(lad), 2)}
        
        jumps.update((sn[i], sn[i + 1]) for i in range(0, len(sn), 2))
        
        end = n * n
        
        visited = [False] * (end + 1)
        
        visited[1] = True
        
        q = deque([1])
        
        for step in range(end + 1):
            
            if not q:
                break
            
            for _ in range(len(q)):
                i = q.popleft()
                
                if i == end:
                    return step
                    
                for j in range(i + 1, min(i + 7, end + 1)):
                    j = jumps.get(j, j)
                    
                    if visited[j]: continue
                
                    visited[j] = True
                    
                    q.append(j)
        return - 1