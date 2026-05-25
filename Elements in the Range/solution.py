class Solution:
    def checkElements(self, start, end, arr):
        # code here
        
        for i in range(start, end):
            if i not in arr:
                return False
        
        return