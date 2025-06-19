class Solution:
    def caseSort(self, s):
        # Separate the lowercase and uppercase characters
        lower = sorted([ch for ch in s if ch.islower()])
        upper = sorted([ch for ch in s if ch.isupper()])
        
        # Pointers to track current character from each sorted list
        li = ui = 0
        result = []
        
        # Rebuild the string maintaining case positions
        for ch in s:
            if ch.islower():
                result.append(lower[li])
                li += 1
            else:
                result.append(upper[ui])
                ui += 1
                
        return ''.join(result)
