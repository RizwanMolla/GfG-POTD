class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


class Solution:
    def reverse(self, head):
        if not head or not head.next:
            return head
        
        curr = head
        new_head = None

        while curr:
            curr.prev, curr.next = curr.next, curr.prev
            new_head = curr
            curr = curr.prev
        
        return new_head
