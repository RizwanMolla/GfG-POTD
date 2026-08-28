class Solution:
    def minCost(self, mat):
        a,b,c=0,0,0
        for y in range(len(mat)):
            a,b,c=min(b,c)+mat[y][0],min(a,c)+mat[y][1],min(a,b)+mat[y][2]
        return min(a,b,c)