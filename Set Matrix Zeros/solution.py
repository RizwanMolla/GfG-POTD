class Solution:
    def setMatrixZeroes(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        rows_to_zero = set()
        cols_to_zero = set()
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)
        
        for i in range(n):
            for j in range(m):
                if i in rows_to_zero or j in cols_to_zero:
                    mat[i][j] = 0
        
        return mat
