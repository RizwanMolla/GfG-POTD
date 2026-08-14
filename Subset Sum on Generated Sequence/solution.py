class Solution:
    def isPossible(self, arr, s, x):
        # code here 
        numbers = [s]
        if x== 0:
            return True
        total = s
        for i in range(len(arr)):
            numbers.append(arr[i]+total)
            total += arr[i]+total
        for n in range(len(numbers)-1, -1, -1):
            if numbers[n] < x:
                x -=numbers[n]
            elif numbers[n] ==x:
                return True
        return False