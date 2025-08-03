from typing import List

class Solution:
    def maxRectSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        finalmaxi = float('-inf')

        for s in range(m):
            temp = [0] * n
            for e in range(s, m):
                for i in range(n):
                    temp[i] += mat[i][e]
                
                curr_sum = 0
                maxi = float('-inf')
                for i in range(n):
                    curr_sum += temp[i]
                    maxi = max(maxi, curr_sum)
                    if curr_sum < 0:
                        curr_sum = 0
                
                finalmaxi = max(finalmaxi, maxi)
        
        return finalmaxi
