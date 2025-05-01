class Solution:
	def nthRowOfPascalTriangle(self, n):
            row = [1]
            
            if n == 1:
                return row
            
            for i in range(1, n):
                new_row = [1]
                for j in range(1, i):
                    new_row.append(row[j-1] + row[j])
                new_row.append(1)
                row = new_row
            
            return row