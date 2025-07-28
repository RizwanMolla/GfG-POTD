class Solution:
    def balanceSums(self, mat):
        n = len(mat)
        
        rowSum = [sum(row) for row in mat]
        colSum = [sum(mat[i][j] for i in range(n)) for j in range(n)]
        
        maxSum = max(max(rowSum), max(colSum))
        
        count = 0  # total operations
        
        # Iterate over the matrix to increment cells
        for i in range(n):
            for j in range(n):
                # Find how much can be added to mat[i][j]
                diff = min(maxSum - rowSum[i], maxSum - colSum[j])
                mat[i][j] += diff
                rowSum[i] += diff
                colSum[j] += diff
                count += diff
        
        return count
