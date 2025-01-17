class Solution:
    def subCount(self, arr, k):
     
        remainder_count = {0: 1}  
        current_sum = 0
        count = 0

        for num in arr:
            current_sum += num
            
            remainder = current_sum % k
            
            if remainder < 0:
                remainder += k
            
            if remainder in remainder_count:
                count += remainder_count[remainder]
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1

        return count
