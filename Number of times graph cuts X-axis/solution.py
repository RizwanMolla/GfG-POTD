class Solution:
    def touchedXaxis(self, arr):
        #code here
        count = 0
        current_position = 0
        
        for change in arr:
            next_position = current_position + change
            if (current_position > 0 and next_position <= 0) or (current_position < 0 and next_position >= 0):
                count += 1
            current_position = next_position
        
        return count