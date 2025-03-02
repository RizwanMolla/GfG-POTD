class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        nge = [-1] * n  
        stack = []  
        
        for i in range(2 * n):  
            while stack and arr[stack[-1]] < arr[i % n]:
                nge[stack.pop()] = arr[i % n]
            if i < n:  
                stack.append(i)
        
        return nge