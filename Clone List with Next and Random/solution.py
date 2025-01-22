class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random=None

class Solution:
    def cloneLinkedList(self, head):
        if not head:
            return None

        curr = head
        while curr:
            newNode = Node(curr.data)
            newNode.next = curr.next
            curr.next = newNode
            curr = newNode.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        dummy = Node(0)
        copy = dummy
        curr = head
        while curr:
            copy.next = curr.next
            curr.next = curr.next.next
            curr = curr.next
            copy = copy.next

        return dummy.next
