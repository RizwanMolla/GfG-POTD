class Solution:
	def countWays(self, n, m):
		# Code here
		if n < m:
		    return 1
		dp = [0] * (n + 1)
		dp[0] = 1
		
		for i in range(1, n + 1):
		    dp[i] = dp[i-1] + (0 if i - m < 0 else dp[i-m])
		return dp[-1] % (10 ** 9 + 7)