class Solution:
    def maxWater(self, arr):
        left, right = 0, len(arr) - 1
        max_area = 0
        
        while left < right:
            height = min(arr[left], arr[right])
            width = right - left
            max_area = max(max_area, height * width)
            
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
