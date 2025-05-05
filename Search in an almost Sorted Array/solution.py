class Solution:
    def findTarget(self, arr, target):
        """
        Find the index of target in an almost sorted array where elements may be at
        their correct position or at adjacent positions.
        
        Args:
            arr: A list of distinct integers that are almost sorted
            target: The integer to search for
            
        Returns:
            The index of target if found, -1 otherwise
        """
        if not arr:
            return -1
            
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Check if the middle element is the target
            if arr[mid] == target:
                return mid
                
            # Check if the element to the left is the target
            if mid > left and arr[mid-1] == target:
                return mid - 1
                
            # Check if the element to the right is the target
            if mid < right and arr[mid+1] == target:
                return mid + 1
                
            # If target is smaller, search in the left half
            if arr[mid] > target:
                right = mid - 2  # Skip the already checked mid-1
            else:
                # If target is larger, search in the right half
                left = mid + 2   # Skip the already checked mid+1
                
        return -1