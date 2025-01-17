class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next  # Store the next node
            current.next = prev       # Reverse the link
            prev = current            # Move prev one step forward
            current = next_node       # Move current one step forward
        return prev
