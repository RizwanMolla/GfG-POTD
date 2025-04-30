#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def countNodesInLoop(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return self.getLoopLength(slow)
        
        return 0

    def getLoopLength(self, node_in_loop):
        count = 1
        current = node_in_loop.next
        while current != node_in_loop:
            count += 1
            current = current.next
        return count