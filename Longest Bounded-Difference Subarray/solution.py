from typing import List
from collections import deque

class Solution:
    def longestSubarray(self, arr: List[int], x: int) -> List[int]:
        minDeque, maxDeque = deque(), deque()
        l, max_len, start = 0, 0, 0
        
        for r in range(len(arr)):

            while minDeque and arr[minDeque[-1]] > arr[r]:
                minDeque.pop()
            minDeque.append(r)
            
            while maxDeque and arr[maxDeque[-1]] < arr[r]:
                maxDeque.pop()
            maxDeque.append(r)

            while arr[maxDeque[0]] - arr[minDeque[0]] > x:
                l += 1
                if minDeque[0] < l:
                    minDeque.popleft()
                if maxDeque[0] < l:
                    maxDeque.popleft()

            if r - l + 1 > max_len:
                max_len = r - l + 1
                start = l

        return arr[start:start + max_len]