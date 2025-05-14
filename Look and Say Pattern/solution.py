class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Base case: first row is "1"
        if n == 1:
            return "1"
        
        # Get the previous row's string
        prev = self.countAndSay(n - 1)
        
        # Process the previous row to generate the current row
        result = ""
        count = 1
        
        # Iterate through the previous row's characters
        for i in range(len(prev)):
            # If we're at the last character or the next character is different
            if i == len(prev) - 1 or prev[i] != prev[i + 1]:
                # Add the count and digit to the result
                result += str(count) + prev[i]
                # Reset the count for the next group
                count = 1
            else:
                # Increment the count for consecutive same digits
                count += 1
        
        return result