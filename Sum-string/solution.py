class Solution:
    def isSumString(self, s):
        """
        Determine if string s can be classified as a sum-string.
        
        Args:
            s: String consisting of digits
            
        Returns:
            bool: True if s is a sum-string, False otherwise
        """
        n = len(s)
        
        def is_valid_number(num_str):
            return len(num_str) == 1 or num_str[0] != '0'
        
        def check_sum_sequence(num1, num2, remaining_str):
            if not remaining_str:
                return True
            
            expected_sum = str(int(num1) + int(num2))
            
            if not remaining_str.startswith(expected_sum):
                return False
            
            if not is_valid_number(expected_sum):
                return False
            
            next_remaining = remaining_str[len(expected_sum):]
            return check_sum_sequence(num2, expected_sum, next_remaining)
        
        for i in range(1, n):
            for j in range(i + 1, n):
                num1 = s[:i]
                num2 = s[i:j]
                remaining = s[j:]
                
                if not is_valid_number(num1) or not is_valid_number(num2):
                    continue
                
                if check_sum_sequence(num1, num2, remaining):
                    return True
        
        return False