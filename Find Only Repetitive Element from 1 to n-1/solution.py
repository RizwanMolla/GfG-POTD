#User function Template for python3
class Solution:
    def findDuplicate(self, arr):
        slow = arr[0]
        fast = arr[0]

        while True:
            slow = arr[slow]
            fast = arr[arr[fast]]
            if slow == fast:
                break

        slow = arr[0]
        while slow != fast:
            slow = arr[slow]
            fast = arr[fast]

        return slow
#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        print(ob.findDuplicate(arr))
        print("~")

# } Driver Code Ends#User function Template for python3
class Solution:
    def findDuplicate(self, arr):
        slow = arr[0]
        fast = arr[0]

        while True:
            slow = arr[slow]
            fast = arr[arr[fast]]
            if slow == fast:
                break

        slow = arr[0]
        while slow != fast:
            slow = arr[slow]
            fast = arr[fast]

        return slow