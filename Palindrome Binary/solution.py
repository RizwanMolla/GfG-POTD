class Solution:
    def isBinaryPalindrome(self, n):
        # code here
        binary = bin(n)[2:]

        binS = str(binary) 
        revBin = binS[::-1]
    
        if binary == revBin:
            return True
        else:
            return False