class Solution:
    def longestPath(self, mat, xs, ys, xd, yd):
        if mat[xs][ys]!=1 or mat[xd][yd]!=1:
            return -1
        wth=len(mat)
        hth=len(mat[0])
        cur=0
        mx=-1
        def bt(x=xs,y=ys):
            nonlocal mat,hth,wth,xd,yd,cur,mx
            if x==xd and y==yd:
                mx=max(mx,cur)
                return
            cur+=1
            mat[x][y]=0
            for dx,dy in [(0,1,),(0,-1,),(1,0,),(-1,0,),]:
                nx,ny=x+dx,y+dy
                if not(0<=nx<wth and 0<=ny<hth) or mat[nx][ny]!=1:
                    continue
                bt(nx,ny)
            cur-=1
            mat[x][y]=1
        bt()
        return mx