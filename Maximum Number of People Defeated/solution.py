class Solution:
    def maxPeopleDefeated(self, p):
        i = 1
        
        while (i * i) <= p:
            p -= (i * i)
            i += 1
            
        return i - 1