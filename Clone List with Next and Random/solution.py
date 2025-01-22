class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random=None

class Solution:
    def cloneLinkedList(self, head):
        if not head:
            return None

        current = head
        while current:
            newNode = Node(current.data)
            newNode.next = current.next
            current.next = newNode
            current = newNode.next

        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        dummy = Node(0)
        copy = dummy
        current = head
        while current:
            copy.next = current.next
            current.next = current.next.next
            current = current.next
            copy = copy.next

        return dummy.next
