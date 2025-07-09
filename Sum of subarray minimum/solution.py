class Solution:
    def sumSubMins(self, arr):
        MOD = 10**9 + 7
        n = len(arr)
        
        # Previous Less Element
        prev = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev[i] = i - stack[-1] if stack else i + 1
            stack.append(i)

        # Next Less Element
        next_ = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            next_[i] = stack[-1] - i if stack else n - i
            stack.append(i)

        # Calculate total sum
        result = 0
        for i in range(n):
            result = (result + arr[i] * prev[i] * next_[i]) % MOD
        
        return result
