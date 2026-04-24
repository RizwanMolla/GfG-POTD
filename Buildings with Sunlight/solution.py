class Solution:
    def visibleBuildings(self, arr):
        # code here
        cnt=1
        currmax=arr[0]
        for i in range(1,len(arr)):
            
            if currmax<=arr[i]:
                currmax=arr[i]
                cnt+=1
        return cnt
