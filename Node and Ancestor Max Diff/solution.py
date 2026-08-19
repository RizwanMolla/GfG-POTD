''' Structure of Binary Tree Node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
        def maxDiff(self, root):
            def dfs(cur=root):
                if not cur:
                    return -float('inf'),float('inf')
                lmx,lmn=dfs(cur.left)
                rmx,rmn=dfs(cur.right)
                mx=max(lmx,rmx,cur.data-min(lmn,rmn))
                mn=min(cur.data,lmn,rmn)
                return mx,mn
            return dfs()[0]