from typing import List

class Solution:
    def maxOfMins(self, arr: List[int]) -> List[int]:
        # code here
        n = len(arr)
        left, right, res = [-1] * n, [n] * n, [0] * (n + 1)
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack.clear()

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        for i in range(n):
            length = right[i] - left[i] - 1
            res[length] = max(res[length], arr[i])

        for i in range(n - 1, 0, -1):
            res[i] = max(res[i], res[i + 1])

        return res[1:]