'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def intersectPoint(self, head1, head2):
        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        len1, len2 = get_length(head1), get_length(head2)
        
        if len1 > len2:
            for _ in range(len1 - len2):
                head1 = head1.next
        else:
            for _ in range(len2 - len1):
                head2 = head2.next
        
        while head1 and head2:
            if head1 == head2:
                return head1
            head1 = head1.next
            head2 = head2.next
        
        return None