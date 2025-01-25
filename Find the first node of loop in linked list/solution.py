#User function Template for python3

""" Node Class
    class Node:
        def __init__(self, data):   # data -> value stored in node
            self.data = data
            self.next = None
"""
class Solution:
    def findFirstNode(self, head):
        if not head or not head.next:
            return None

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                break
        
        if not fast or not fast.next:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow