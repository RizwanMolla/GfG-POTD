class Solution:
    def minWindow(self, s1, s2):
        n, m = len(s1), len(s2)
        min_len = float('inf')
        start = -1

        i = 0
        while i < n:
            j = 0
            k = i

            while k < n:
                if s1[k] == s2[j]:
                    j += 1
                    if j == m:
                        break
                k += 1

            if j == m:
                end = k
                j -= 1

                while k >= i:
                    if s1[k] == s2[j]:
                        j -= 1
                        if j < 0:
                            break
                    k -= 1

                start_idx = k

                if end - start_idx + 1 < min_len:
                    min_len = end - start_idx + 1
                    start = start_idx

                i = start_idx

            i += 1

        return "" if start == -1 else s1[start:start + min_len]
