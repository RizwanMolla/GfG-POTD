#User function Template for python3
class Solution:
    def singleNum(self, arr):
        xor_all = 0
        for num in arr:
            xor_all ^= num

        # Find rightmost set bit in xor_all
        rightmost_set_bit = xor_all & -xor_all

        num1, num2 = 0, 0
        for num in arr:
            if num & rightmost_set_bit:
                num1 ^= num
            else:
                num2 ^= num

        return sorted([num1, num2])