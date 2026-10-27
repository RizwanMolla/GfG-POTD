class Solution:
    def getMaxWeight(self, s):
        a, b = 0, 1
        for i in range(1, len(s)):
            need_change = int(s[i] == s[i - 1])
            a, b = b, max(b + 1, a + 4 - need_change)
        return b