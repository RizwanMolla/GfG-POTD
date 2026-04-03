class Solution:
    def diagView(self, mat):
        n=len(mat)
        ret=[]
        for c in range(2*n):
            for y in range(n):
                x=c-y
                if 0<=x<n:
                    ret.append(mat[y][x])
                elif x<0:
                    break
        return ret