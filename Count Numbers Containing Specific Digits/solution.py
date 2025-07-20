class Solution:
    def countValid(self, n, arr):
        forbidden_digits = set(arr)

        if n == 1:
            total_n_digit_integers = 9
        else:
            total_n_digit_integers = 9 * (10**(n - 1))

        allowed_for_complement = []
        for i in range(10):
            if i not in forbidden_digits:
                allowed_for_complement.append(i)
        
        count_allowed = len(allowed_for_complement)
        
        count_non_zero_allowed = 0
        for digit in allowed_for_complement:
            if digit != 0:
                count_non_zero_allowed += 1

        count_complement_numbers = 0
        if count_allowed == 0:
            count_complement_numbers = 0
        elif n == 1:
            count_complement_numbers = count_non_zero_allowed
        else:
            count_complement_numbers = count_non_zero_allowed * (count_allowed**(n - 1))
            
        return total_n_digit_integers - count_complement_numbers