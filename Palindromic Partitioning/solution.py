#User function Template for python3

class Solution:
    def palPartition(self, s: str) -> int:
        n = len(s)
        if n == 1 or s == s[::-1]:
            return 0  
        
        isPalindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            isPalindrome[i][i] = True  
        
        for length in range(2, n+1):  
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length == 2 or isPalindrome[i + 1][j - 1]):
                    isPalindrome[i][j] = True

        dp = [float('inf')] * n  
        for j in range(n):
            if isPalindrome[0][j]:
                dp[j] = 0  
            else:
                for i in range(j):
                    if isPalindrome[i + 1][j]:  
                        dp[j] = min(dp[j], 1 + dp[i])  

        return dp[n-1]