'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def swapKth(self, head, k):
        # Find the total number of nodes in the list
        count = 0
        current = head
        while current:
            count += 1
            current = current.next

        # If k is invalid, no swap is possible
        if k > count:
            return head

        # Find the kth node from the beginning
        first = head
        for _ in range(k - 1):
            first = first.next

        # Find the kth node from the end
        second = head
        for _ in range(count - k):
            second = second.next

        # Swap the data of the two nodes
        first.data, second.data = second.data, first.data

        return head