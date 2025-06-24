class Solution:
    def maxSubseq(self, s, k):
        n = len(s)
        keep = n - k
        stack = []

        for c in s:
            # While we can remove characters, and the current character is better
            while stack and k > 0 and stack[-1] < c:
                stack.pop()
                k -= 1
            stack.append(c)

        # Only return the needed number of characters
        return ''.join(stack[:keep])
