class Solution:
    def wordBreak(self, s, dictionary):
        word_set = set(dictionary)
        max_len = max(len(word) for word in dictionary) if dictionary else 0
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  
        
        for i in range(1, n + 1):
            start = max(0, i - max_len) if max_len > 0 else 0
            for j in range(start, i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]
