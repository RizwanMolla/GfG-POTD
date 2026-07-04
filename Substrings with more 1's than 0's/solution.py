class Solution():
    def countSubstring(self, S):
        # code here
        lenS = len(S)
        timesOfValue = [0]*(2*lenS + 1)
        i0 = lenS
        substrs = 0 
        currValue = 0
        ended = 0
        timesOfValue[i0] = 1
        for i in range(lenS):
            if(S[i]=='1'):
                ended += timesOfValue[i0+currValue]
                currValue += 1
            else:
                ended -= timesOfValue[i0+currValue-1]
                currValue -= 1            
            substrs += ended    
            timesOfValue[i0+currValue] +=1    
        return substrs