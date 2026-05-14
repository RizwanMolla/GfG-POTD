class Solution:
     def search(self, a, b):
        # code here
        def make_lsp(b):
            n = len(b)
            dp = [0]*n
            for i in range(1, n):
                j = dp[i-1]
                while j > 0 and b[j] != b[i]:
                    j = dp[j-1]
                if b[i] == b[j]:
                    j += 1
                dp[i] = j
            return dp
        
        lsp = make_lsp(b)
        matched = []
        i = j = 0
        while i < len(a):
            if a[i] == b[j]:
                i += 1
                j += 1
                if j == len(b):
                    matched.append(i-j)
                    j = lsp[j-1]
            else:
                if j != 0:
                    j = lsp[j-1]
                else:
                    i += 1
        return matched
        