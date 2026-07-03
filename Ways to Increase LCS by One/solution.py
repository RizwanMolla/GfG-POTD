class Solution:
    def waysToIncreaseLCSBy1(self, s1, s2):
        n1 = len(s1)
        n2 = len(s2)

        # Prefix LCS
        pref = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    pref[i][j] = pref[i - 1][j - 1] + 1
                else:
                    pref[i][j] = max(pref[i - 1][j], pref[i][j - 1])

        L = pref[n1][n2]

        # Suffix LCS
        suff = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                if s1[i] == s2[j]:
                    suff[i][j] = suff[i + 1][j + 1] + 1
                else:
                    suff[i][j] = max(suff[i + 1][j], suff[i][j + 1])

        ans = 0

        for i in range(n1 + 1):
            used = set()

            for j in range(n2):
                ch = s2[j]

                if ch in used:
                    continue

                if pref[i][j] + 1 + suff[i][j + 1] == L + 1:
                    ans += 1
                    used.add(ch)

        return ans