class Solution:
    def minSwaps(self, arr):
        # Count total number of 1s
        ones = sum(arr)

        # If no 1s are present
        if ones == 0:
            return -1

        # Count zeros in the first window of size 'ones'
        zero_count = arr[:ones].count(0)
        min_swaps = zero_count

        # Slide the window across the array
        for i in range(ones, len(arr)):
            # Remove the outgoing element
            if arr[i - ones] == 0:
                zero_count -= 1

            # Add the incoming element
            if arr[i] == 0:
                zero_count += 1

            # Update minimum swaps
            min_swaps = min(min_swaps, zero_count)

        return min_swaps