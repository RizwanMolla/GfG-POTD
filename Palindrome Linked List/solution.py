#User function Template for python3
'''

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
#Function to check whether the list is palindrome.

class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        first, second = head, prev
        while second:
            if first.data != second.data:
                return False
            first = first.next
            second = second.next
        
        return True