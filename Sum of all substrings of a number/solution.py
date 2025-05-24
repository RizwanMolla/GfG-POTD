class Solution:
    def sumSubstrings(self,s):
        
        total_sum = 0
        n = len(s)
        
        for i in range(n):
            current_num = 0
            
            for j in range(i, n):
                current_num = current_num * 10 + int(s[j])
                total_sum += current_num
        
        return total_sum