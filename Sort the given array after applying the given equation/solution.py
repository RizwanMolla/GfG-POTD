class Solution:
    def sortArray(self, arr, A, B, C):
        n = len(arr)
        
        # Apply the quadratic function A*x^2 + B*x + C to each element
        for i in range(n):
            x = arr[i]
            arr[i] = A * (x * x) + B * x + C
            
        # Sort the transformed array
        arr.sort()
        
        return arr