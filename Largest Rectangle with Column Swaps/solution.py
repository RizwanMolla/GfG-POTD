class Solution:
    def maxArea(self, mat):
       n = len(mat)
       m = len(mat[0])
    
       ans = 0
       height = [0] * m
    
       for i in range(n):
    
           for j in range(m):
               if mat[i][j] == 1:
                   height[j] = height[j] + 1
               else:
                   height[j] = 0
    
           h = sorted(height, reverse=True)
    
           for j in range(m):
               area = h[j] * (j + 1)
    
               if area > ans:
                   ans = area
    
       return ans   