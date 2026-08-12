class Solution:
    def __init__(self):
        self.mod = 10**9 + 7
    def rec(self, temp, grid, ind1, ind2, n):
        if ind1 >= n or ind2 >= n or ind1 < 0 or ind2 < 0:
            return [0, 0]
        
        if ind1 == n - 1 and ind2 == n - 1:
            return [1, grid[ind1][ind2]]
        
        if temp[ind1][ind2] != -1:
            return temp[ind1][ind2]
        
        
        op1 = [0, 0]
        op2 = [0, 0]
        if grid[ind1][ind2] == 1:
            op1 = self.rec(temp, grid, ind1, ind2 + 1, n)
        
        elif grid[ind1][ind2] == 2:
            op1 = self.rec(temp, grid, ind1+1, ind2, n)
        
        elif grid[ind1][ind2] == 3:
            op1 = self.rec(temp, grid, ind1, ind2 + 1, n)
            op2 = self.rec(temp, grid, ind1+1, ind2, n)
        
        
        total_paths = op1[0] + op2[0]
        if total_paths == 0:
            temp[ind1][ind2] = [0, 0]
        else:
            max_sum = grid[ind1][ind2] + max(op1[1], op2[1])
            temp[ind1][ind2] = [total_paths%self.mod, max_sum%self.mod]
        return temp[ind1][ind2]
            
    def findWays(self, grid):
        n = len(grid)
        temp = [[-1 for _ in range(n)] for _ in range(n)]
        return self.rec(temp, grid, 0, 0, n)