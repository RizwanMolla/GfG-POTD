'''
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}'''
	
class Solution:
    def segregate(self, head):
        count = [0, 0, 0]
        temp = head
        
        while temp:
            count[temp.data] += 1
            temp = temp.next
        
        temp = head
        i = 0
        while temp:
            if count[i] == 0:
                i += 1
            else:
                temp.data = i
                count[i] -= 1
                temp = temp.next
        
        return head