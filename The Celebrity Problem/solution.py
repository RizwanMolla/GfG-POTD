class Solution:
    def celebrity(self, mat):
        n = len(mat)
        stack = [i for i in range(n)]  
        
        while len(stack) > 1:
            A = stack.pop()
            B = stack.pop()
            
            if mat[A][B] == 1:
                stack.append(B)
            else:
                stack.append(A)

        if not stack:
            return -1
        
        candidate = stack.pop()
        
        for i in range(n):
            if i != candidate and (mat[candidate][i] == 1 or mat[i][candidate] == 0):
                return -1
        
        return candidate