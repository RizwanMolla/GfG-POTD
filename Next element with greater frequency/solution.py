from collections import Counter

class Solution:
    def findGreater(self, arr):
        n = len(arr)
        result = [-1] * n
        freq = Counter(arr)
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and freq[arr[stack[-1]]] <= freq[arr[i]]:
                stack.pop()
            
            if stack:
                result[i] = arr[stack[-1]]

            stack.append(i)

        return result
