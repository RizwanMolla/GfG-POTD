class Solution:
    def longestPalinSubseq(self, s: str) -> int:
        n = len(s)
        memo = {}

        def lps(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            
            if s[i] == s[j]:
                memo[(i, j)] = 2 + lps(i + 1, j - 1)
            else:
                memo[(i, j)] = max(lps(i + 1, j), lps(i, j - 1))
            
            return memo[(i, j)]
        
        return lps(0, n - 1)