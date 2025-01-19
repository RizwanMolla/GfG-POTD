# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        #code here
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        k %= length
        if k == 0:  
            return head
        
        current = head
        for _ in range(k - 1):
            current = current.next
        
        new_head = current.next
        current.next = None  
        tail = new_head
        while tail.next:
            tail = tail.next
        
        tail.next = head
        
        return new_head