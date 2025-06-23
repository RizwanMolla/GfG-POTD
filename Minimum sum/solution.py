class Solution:
    def minSum(self, arr):
        def addStrings(num1, num2):
            i, j = len(num1) - 1, len(num2) - 1
            carry = 0
            res = []

            while i >= 0 or j >= 0 or carry:
                digit1 = int(num1[i]) if i >= 0 else 0
                digit2 = int(num2[j]) if j >= 0 else 0
                total = digit1 + digit2 + carry
                res.append(str(total % 10))
                carry = total // 10
                i -= 1
                j -= 1

            return ''.join(reversed(res))

        # Step 1: Sort the digits
        arr.sort()

        # Step 2: Distribute into two numbers for minimal sum
        num1 = []
        num2 = []
        for i, digit in enumerate(arr):
            if i % 2 == 0:
                num1.append(str(digit))
            else:
                num2.append(str(digit))

        # Step 3: Add them as strings
        sum_str = addStrings("".join(num1), "".join(num2))

        # Step 4: Strip leading zeros, but return "0" if result is empty
        return sum_str.lstrip('0') or '0'
