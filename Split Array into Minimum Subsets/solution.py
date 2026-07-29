class Solution:
    def minSubsets(self, arr):
        #code here
        c = 0 
        b = sorted(arr)
        for i in range(len(b)-1):
            if b[i] + 1 != b[i+1]:
                c += 1
        return c+1