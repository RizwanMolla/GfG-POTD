class Solution:
    def longestSubstr(self, s, k):
        # Code here
        mp = {}
        l = 0
        j , maxfreq = 0 , 0
        
        for i in range(len(s)):
            mp[s[i]] = mp.get(s[i], 0) + 1
            maxfreq = max(maxfreq, mp[s[i]])
            
            while((i-j+1) - maxfreq > k):
                mp[s[j]]-=1;
                if mp[s[j]] == 0:
                    del mp[s[j]]
                j+=1
            l = max(i-j+1,l)
            
        return l