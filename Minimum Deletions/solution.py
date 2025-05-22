class Solution:
    def minDeletions(self, s):
        """
        Find minimum deletions to make string palindrome.
        
        Approach: Find Longest Palindromic Subsequence (LPS) using LCS
        between string and its reverse.
        
        Time Complexity: O(n^2)
        Space Complexity: O(n^2) - can be optimized to O(n)
        """
        n = len(s)
        
        # Edge case
        if n <= 1:
            return 0
        
        # Get reverse of string
        reverse_s = s[::-1]
        
        # Find LCS between s and reverse_s using DP
        # dp[i][j] = length of LCS of s[0:i] and reverse_s[0:j]
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i-1] == reverse_s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # Length of longest palindromic subsequence
        lps_length = dp[n][n]
        
        # Minimum deletions = total length - LPS length
        return n - lps_length
    
    def minDeletions_optimized(self, s):
        """
        Space-optimized version using 1D DP array.
        
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        n = len(s)
        
        if n <= 1:
            return 0
        
        reverse_s = s[::-1]
        
        # Use two 1D arrays instead of 2D
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i-1] == reverse_s[j-1]:
                    curr[j] = prev[j-1] + 1
                else:
                    curr[j] = max(prev[j], curr[j-1])
            
            # Swap arrays for next iteration
            prev, curr = curr, prev
        
        lps_length = prev[n]
        return n - lps_length