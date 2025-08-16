from functools import cmp_to_key

class Solution:
    def findLargest(self, arr):
        arr = list(map(str, arr))
        
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        arr.sort(key=cmp_to_key(compare))
    
        # Edge case: when all numbers are zeros
        if arr[0] == "0":
            return "0"
        
        return "".join(arr)