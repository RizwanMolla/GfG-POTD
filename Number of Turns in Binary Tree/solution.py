''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def numberOfTurns(self, root, p, q):
        def f(r,x,a):
            if not r: return False
            if r.data == x: return True
            a.append('L')
            if f(r.left,x,a): return True
            a.pop();a.append('R')
            if f(r.right,x,a): return True
            a.pop()
        a,b = [],[]
        f(root,p,a)
        f(root,q,b)

        i=0
        while i< min(len(a), len(b)) and a[i] == b[i]:
            i += 1
        a = a[i:][::-1] + b[i:]
        ans = sum(a[i] != a[i-1] for i in range(1,len(a)))
        return ans or -1
