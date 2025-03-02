class Solution:
    def sumOfMax(self, arr):
        n = len(arr)
        ple = [0] * n
        nge = [0] * n
        stack = []  

        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            ple[i] = i - stack[-1] if stack else i + 1
            stack.append(i)

        stack = []

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] <= arr[i]:  
                stack.pop()
            nge[i] = stack[-1] - i if stack else n - i
            stack.append(i)

        total_sum = sum(arr[i] * ple[i] * nge[i] for i in range(n))
        return total_sum