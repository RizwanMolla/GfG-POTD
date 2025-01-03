class Solution:
    def subarrayXor(self, arr, k):
        xor_count = {0: 1}
        xor_sum = 0
        count = 0
        
        for num in arr:
            xor_sum ^= num
            if xor_sum ^ k in xor_count:
                count += xor_count[xor_sum ^ k]
            xor_count[xor_sum] = xor_count.get(xor_sum, 0) + 1
        
        return count


"""
Explanation:
The solution uses a hash map to efficiently count subarrays with a given XOR value. The variable xor_sum keeps track of the cumulative XOR of the elements. 
For each element in the array:

1. Compute the cumulative XOR.
2. Check if xor_sum ^ k exists in the hash map. If it does, add its count to the result since it indicates the presence of subarrays whose XOR is equal to k.
3. Update the count of the current xor_sum in the hash map.
This approach works in O(n) time and uses O(n) space.
"""