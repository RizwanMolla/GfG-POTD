#User function Template for python3
import heapq

class Solution:
    def mostBooked(self, n, meetings):
        #code here
        meetings.sort()
        
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        
        busy_rooms = []
        meeting_count = [0] * n
        
        for start, end in meetings:
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)
            
            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, room))
            else:
                end_time, room = heapq.heappop(busy_rooms)
                new_end = end_time + (end - start)
                heapq.heappush(busy_rooms, (new_end, room))
            
            meeting_count[room] += 1
        
        max_meetings = max(meeting_count)
        return meeting_count.index(max_meetings)