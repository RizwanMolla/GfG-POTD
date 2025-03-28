from typing import List

class Solution:
    def jobSequencing(self, deadline: List[int], profit: List[int]) -> List[int]:
        jobs = sorted(zip(profit, deadline), reverse=True)
        max_deadline = max(deadline)  
        
        parent = list(range(max_deadline + 1))  
        
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        total_jobs = 0
        total_profit = 0
        
        for p, d in jobs:
            available_slot = find(d)
            
            if available_slot > 0:
                parent[available_slot] = find(available_slot - 1)
                total_jobs += 1
                total_profit += p

        return [total_jobs, total_profit]