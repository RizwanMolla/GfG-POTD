class Solution:
    def makeBeautiful(self, arr: list[int]) -> list[int]:
        stack = []
        for num in arr:
            if stack and (stack[-1] >= 0 > num or stack[-1] < 0 <= num):
                stack.pop()
            else:
                stack.append(num)
        return stack