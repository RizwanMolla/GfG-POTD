class Solution:
    def palinParts(self, s):
        result = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                prefix = s[start:end]
                if is_palindrome(prefix):
                    path.append(prefix)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return result
