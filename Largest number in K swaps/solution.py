#User function Template for python3

class Solution:
    def findMaximumNum(self, s, k):
        s = list(s)
        n = len(s)
        
        def findMaxUtil(s, k, idx):
            if k == 0 or idx == n - 1:
                return
            
            curr_max = s[idx]
            
            for j in range(idx + 1, n):
                if s[j] > curr_max:
                    curr_max = s[j]
            
            if curr_max != s[idx]:
                for j in range(n - 1, idx, -1):
                    if s[j] == curr_max:
                        # Swap
                        s[idx], s[j] = s[j], s[idx]
                        findMaxUtil(s, k - 1, idx + 1)
                        return
            
            findMaxUtil(s, k, idx + 1)
        
        findMaxUtil(s, k, 0)
        
        return ''.join(s)