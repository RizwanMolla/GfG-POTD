import heapq

class Solution:
    def minMeetingRooms(self, start, end):
        start.sort()
        end.sort()
        
        min_heap = []
        rooms = 0
        end_ptr = 0
        
        for s in start:
            while min_heap and min_heap[0] <= s:
                heapq.heappop(min_heap)
            
            heapq.heappush(min_heap, end[end_ptr])
            end_ptr += 1
            
            rooms = max(rooms, len(min_heap))
        
        return rooms