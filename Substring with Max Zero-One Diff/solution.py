class Solution:
	def maxSubstring(self, s):
		ans = -1
		ssum = 0
		
		for i in range(len(s)):
            ssum += (-1 if s[i] == '1' else 1)
            ssum = max(0, ssum)
            ans = max(ans, ssum)
		
		return ans if ans != 0 else -1