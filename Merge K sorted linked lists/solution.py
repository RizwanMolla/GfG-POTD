#User function Template for python3
class Node:
    def _init_(self,x):
        self.data = x
        self.next = None


import heapq

class Solution:
    def mergeKLists(self, arr):

        heap = []
        
        for i in range(len(arr)):
            if arr[i]:
                heapq.heappush(heap, (arr[i].data, i, arr[i]))
        
        dummy = Node(0)
        current = dummy
        
        while heap:
            
            value, index, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            
            if node.next:
                heapq.heappush(heap, (node.next.data, index, node.next))
        
        return dummy.next