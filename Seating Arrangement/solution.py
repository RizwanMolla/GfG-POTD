class Solution:
    def canSeat(self, k, seats):
        if ((k == 0 or seats[k - 1] == 0) and (k + 1 == len(seats) or seats[k + 1] == 0)):
            return True
        return False

    def canSeatAllPeople(self, k, seats):
        count = 0
        for i in range(len(seats)):
            if seats[i] == 0 and self.canSeat(i, seats):
                count += 1
                seats[i] = 1
        return count >= k