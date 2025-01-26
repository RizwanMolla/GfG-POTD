class Solution:
    def removeLoop(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return
        
        slow = head
        if slow == fast:
            while fast.next != slow:
                fast = fast.next
        else:
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next
        
        fast.next = None

"""
The approach uses Floyd's cycle detection algorithm to detect the loop. Once detected, it resets one pointer to the head and moves both pointers one step at a time until they meet at the start of the loop. The loop is then removed by setting the next pointer of the last node in the loop to None. The time complexity is O(n) and space complexity is O(1).
"""