class Solution:
    def maxArea(self, height):
        # code here
        i, j = 0, len(height) - 1
        maxi = -1
        while i < j:
            maxi = max(maxi, (j - i - 1) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
                
        return maxi