class Solution:
    def rearrange(self, arr, x):
        
        paired = [(abs(v - x), i, v) for i, v in enumerate(arr)]
        paired.sort()
        
        for j, (_, _, v) in enumerate(paired):
            arr[j] = v
        return arr
