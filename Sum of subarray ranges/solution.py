class Solution:
    def subarrayRanges(self, arr):
        n = len(arr)

        prev_smaller = [-1] * n
        next_smaller_eq = [n] * n
        prev_greater = [-1] * n
        next_greater_eq = [n] * n

        stack = []

        # Previous Smaller
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        # Next Smaller or Equal
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            next_smaller_eq[i] = stack[-1] if stack else n
            stack.append(i)

        stack.clear()

        # Previous Greater
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            prev_greater[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        # Next Greater or Equal
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            next_greater_eq[i] = stack[-1] if stack else n
            stack.append(i)

        result = 0

        for i in range(n):
            max_count = (i - prev_greater[i]) * (next_greater_eq[i] - i)
            min_count = (i - prev_smaller[i]) * (next_smaller_eq[i] - i)
            result += arr[i] * (max_count - min_count)

        return result
