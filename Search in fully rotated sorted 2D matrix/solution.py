class Solution:
    def searchMatrix(self, mat, x):
        n = len(mat)
        m = len(mat[0])
        total = n * m
        
        low, high = 0, total - 1
        
        while low <= high:
            mid = (low + high) // 2
            row, col = divmod(mid, m)
            mid_val = mat[row][col]
            
            if mid_val == x:
                return True
            

            low_val = mat[low // m][low % m]
            high_val = mat[high // m][high % m]
            

            if low_val <= mid_val:
                if low_val <= x < mid_val:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if mid_val < x <= high_val:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return False
