from typing import List

class Solution:
    def getMaxArea(self, arr: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(arr)

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                height = arr[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        while stack:
            height = arr[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, height * width)

        return max_area