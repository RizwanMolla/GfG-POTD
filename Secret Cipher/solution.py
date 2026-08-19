class Solution:
    def compress(self, s):
        n = len(s)

        lps = [0] * n

        for i in range(1, n):
            j = lps[i - 1]

            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]

            if s[i] == s[j]:
                j += 1

            lps[i] = j

        ans = []
        i = n - 1

        while i >= 0:
            length = i + 1

            if i % 2 == 1:
                period = length - lps[i]

                if (lps[i] >= length // 2 and
                        length % (2 * period) == 0):

                    ans.append('*')

                    i = i // 2 + 1
                else:
                    ans.append(s[i])
            else:
                ans.append(s[i])

            i -= 1

        return ''.join(reversed(ans))