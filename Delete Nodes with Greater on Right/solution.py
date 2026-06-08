'''
Structure of linked list node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def rev(self,head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
    def compute(self,head):
        if head.next==None:
            return head
        head1 = self.rev(head)
        prev = head1
        curr = head1.next
        while curr:
            if curr.data<prev.data:
                prev.next = curr.next
            else:
                prev=curr
            curr = curr.next
        head = self.rev(head1)
        return head
        