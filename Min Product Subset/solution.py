class Solution:
    def minProd(self, arr):
        prod_min, prod_max = arr[0], arr[0]
    
        for x in arr[1:]:
            a = x * prod_min
            b = x * prod_max
    
            new_min = min(prod_min, x, a, b)
            new_max = max(prod_max, x, a, b)
    
            prod_min = new_min
            prod_max = new_max
    
        return prod_min