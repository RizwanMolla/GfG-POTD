from collections import deque

class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        flip = 0  
        flipped = deque()  
        flips = 0 
        for i in range(n):
            if flipped and flipped[0] == i:
                flip -= 1 
                flipped.popleft()
            if (arr[i] + flip) % 2 == 0:
                if i + k > n:
                    return -1
                
                flip += 1 
                flips += 1 
                flipped.append(i + k)
                
        return flips