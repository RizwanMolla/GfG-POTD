#User function Template for python3
class Solution:
    def countWays(self, s):
        symbols = []
        operators = []
        n = len(s)
        for i in range(n):
            if i % 2 == 0:
                symbols.append(s[i])
            else:
                operators.append(s[i])
        m = len(symbols)
        if m == 0:
            return 0
        
        t_dp = [[0] * m for _ in range(m)]
        f_dp = [[0] * m for _ in range(m)]
        
        for i in range(m):
            if symbols[i] == 'T':
                t_dp[i][i] = 1
                f_dp[i][i] = 0
            else:
                t_dp[i][i] = 0
                f_dp[i][i] = 1
        
        for length in range(2, m + 1):
            for i in range(m - length + 1):
                j = i + length - 1
                t_dp[i][j] = 0
                f_dp[i][j] = 0
                for k in range(i, j):
                    op = operators[k]
                    left_t = t_dp[i][k]
                    left_f = f_dp[i][k]
                    right_t = t_dp[k + 1][j]
                    right_f = f_dp[k + 1][j]
                    
                    if op == '&':
                        curr_t = left_t * right_t
                        curr_f = left_t * right_f + left_f * right_t + left_f * right_f
                    elif op == '|':
                        curr_t = left_t * right_t + left_t * right_f + left_f * right_t
                        curr_f = left_f * right_f
                    elif op == '^':
                        curr_t = left_t * right_f + left_f * right_t
                        curr_f = left_t * right_t + left_f * right_f
                    
                    t_dp[i][j] += curr_t
                    f_dp[i][j] += curr_f
        
        return t_dp[0][m - 1]