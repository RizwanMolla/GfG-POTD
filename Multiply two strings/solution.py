#User function Template for python3

class Solution:
    def multiplyStrings(self, s1, s2):
        s1 = s1.lstrip('0')
        s2 = s2.lstrip('0')
        
        if not s1 or not s2:
            return "0"
        
        negative = False
        if s1 and s1[0] == '-':
            negative = not negative
            s1 = s1[1:]
        if s2 and s2[0] == '-':
            negative = not negative
            s2 = s2[1:]
        
        n = len(s1)
        m = len(s2)
        res = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                mul = (ord(s1[i]) - ord('0')) * (ord(s2[j]) - ord('0'))
                sum = mul + res[i + j + 1]
                res[i + j + 1] = sum % 10
                res[i + j] += sum // 10

        result = ''.join(map(str, res)).lstrip('0')
        
        if not result:
            return "0"
        
        if negative:
            result = '-' + result
        
        return result