class Solution:
    def calculateSpan(self, arr):
        #write code here
        n = len(arr)
        span = [0] * n
        stack = []
        
        for i in range(n):
            while stack and arr[i] >= arr[stack[-1]]:
                stack.pop()
            
            span[i] = i + 1 if not stack else (i - stack[-1])
            stack.append(i)
        
        return span