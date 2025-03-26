class Solution:
    def subseqCount(self, txt, pat):
        n, m = len(txt), len(pat)
        prev = [0] * (m + 1)
        prev[0] = 1

        for i in range(1, n + 1):
            curr = prev[:]
            for j in range(1, m + 1):
                if txt[i - 1] == pat[j - 1]:
                    curr[j] = prev[j - 1] + prev[j]
                else:
                    curr[j] = prev[j]
            prev = curr

        return prev[m]