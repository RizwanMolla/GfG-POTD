class Solution:
    def getLongestPrefix(self, s: str) -> int:
        n = len(s)
        ans = -1
        z = [0] * n
        l = -1

        for i in range(1, n):
            if l != -1 and i < l + z[l]:
                z[i] = min(z[i - l], l + z[l] - i)
            while z[i] < n - i and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] > l + (z[l] if l != -1 else 0):
                l = i
            if i + z[i] == n:
                ans = i

        return ans
