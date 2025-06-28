from bisect import bisect_right

class Solution:
    def countLessEq(self, a, b):
        # Step 1: Sort array b
        b.sort()
        
        # Step 2: Result array
        result = []
        
        # Step 3: For each element in a, count elements in b less than or equal to it
        for num in a:
            count = bisect_right(b, num)
            result.append(count)
        
        return result