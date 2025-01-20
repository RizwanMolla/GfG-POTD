class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sortedMerge(self, head1, head2):
        dummy = Node(0)
        current = dummy
        while head1 and head2:
            if head1.data < head2.data:
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            current = current.next
        current.next = head1 if head1 else head2
        return dummy.next

"""
Overview:
The solution iterates through both linked lists simultaneously, comparing nodes and attaching the smaller node to the result. A dummy node is used to simplify edge cases, and the remaining elements of the longer list are appended at the end. The overall time complexity is O(n+m) and space complexity is O(1).
"""