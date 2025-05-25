class Solution:
    def pythagoreanTriplet(self, arr):
        # Step 1: Square all elements and store in a set
        squares = set()
        for num in arr:
            squares.add(num * num)

        n = len(arr)
        # Step 2: Try all pairs (i, j) and check if a^2 + b^2 exists
        for i in range(n):
            for j in range(i + 1, n):
                a2 = arr[i] * arr[i]
                b2 = arr[j] * arr[j]
                if a2 + b2 in squares:
                    return True
        return False
