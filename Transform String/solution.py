class Solution:
    def transform(self, s1, s2):
        from collections import Counter
        if Counter(s1) != Counter(s2):
            return - 1
        n = len(s1)
        j = n - 1
        for i in reversed(range(n)):
            if s1[i] == s2[j]:
                j -= 1
        return j + 1