class Solution:
    def wifiRange(self, s, x):
        n = len(s)
        coverage = [0] * (n + 1)

        for i in range(n):
            if s[i] == '1':
                left = max(0, i - x)
                right = min(n - 1, i + x)

                coverage[left] += 1
                coverage[right + 1] -= 1

        curr = 0
        for i in range(n):
            curr += coverage[i]
            if curr <= 0:
                return False

        return True
