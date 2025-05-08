#User function Template for python3
class Solution:
    def findMissing(self, arr):
        n = len(arr)
    
        option1_valid = True
        if (arr[-1] - arr[0]) % (n - 1) == 0:
            d1 = (arr[-1] - arr[0]) // (n - 1)
            
            for i in range(1, n):
                if arr[i] - arr[i-1] != d1:
                    option1_valid = False
                    break
                    
            if option1_valid:
                return arr[-1] + d1
        
        if (arr[-1] - arr[0]) % n == 0:
            d2 = (arr[-1] - arr[0]) // n
            
            expected = arr[0]
            for num in arr:
                if num != expected:
                    return expected
                expected += d2

            return arr[-1] + d2

        
        differences = [arr[i] - arr[i-1] for i in range(1, n)]
        freq = {}
        for d in differences:
            freq[d] = freq.get(d, 0) + 1
            
        most_common_diff = min(differences) 
        max_count = 0
        for d, count in freq.items():
            if count > max_count:
                max_count = count
                most_common_diff = d
                
        expected = arr[0]
        for num in arr:
            if num != expected:
                return expected
            expected += most_common_diff
            
        return arr[-1] + most_common_diff