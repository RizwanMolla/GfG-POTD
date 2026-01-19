class Solution:
    def removeKdig(self, s, k):
        stack = []

        for ch in s:
            while stack and k > 0 and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        while k > 0:
            stack.pop()
            k -= 1

        result = ''.join(stack).lstrip('0')

        return result if result else "0"
