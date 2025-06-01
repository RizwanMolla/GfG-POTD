class Solution:
    def countPairs(self, mat1, mat2, x):
        """
        Count pairs (a, b) where a from mat1, b from mat2, and a + b = x
        
        Approach: Since both matrices are sorted in a special way where each row
        is sorted and last element of row < first element of next row, we can
        treat each matrix as a single sorted array and use two pointers.
        
        Time Complexity: O(n²) - we traverse both flattened arrays once
        Space Complexity: O(1) - only using pointers
        """
        n = len(mat1)
        
        # Convert 2D indices to 1D and vice versa
        def get_element(matrix, index):
            """Get element at 1D index from 2D matrix"""
            row = index // n
            col = index % n
            return matrix[row][col]
        
        # Two pointers approach
        left = 0  # pointer for mat1 (start from smallest)
        right = n * n - 1  # pointer for mat2 (start from largest)
        count = 0
        
        while left < n * n and right >= 0:
            val1 = get_element(mat1, left)
            val2 = get_element(mat2, right)
            current_sum = val1 + val2
            
            if current_sum == x:
                count += 1
                left += 1
                right -= 1
            elif current_sum < x:
                # Need larger sum, move left pointer forward (increase val1)
                left += 1
            else:
                # Sum too large, move right pointer back (decrease val2)
                right -= 1
        
        return count