class Solution:
    def isBitSet(self, n):
        # code here
        binaryNum = bin(n)
        binaryStr = str(binaryNum[2:])
        if "0" in str(binaryStr):
            return False
        else:
            return True