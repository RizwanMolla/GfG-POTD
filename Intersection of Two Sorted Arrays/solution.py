class Solution:
    def intersection(self,a, b):
        i, j = 0, 0
        result = []
        
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                # Ensure distinct elements
                if not result or result[-1] != a[i]:
                    result.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1
                
        return result