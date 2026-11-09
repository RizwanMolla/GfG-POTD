class Solution:
    def minTime(self, n: int, s1: int, s2: int) -> int:
        # code here
        return min(max(i*s1, (n-i)*s2) for i in range(n+1)) 