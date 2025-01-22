class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Solution:
    def addTwoLists(self, num1, num2):
        def reverseList(head):
            prev, curr = None, head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        num1 = reverseList(num1)
        num2 = reverseList(num2)

        dummy = Node(0)
        curr = dummy
        carry = 0

        while num1 or num2 or carry:
            sum_val = carry
            if num1:
                sum_val += num1.data
                num1 = num1.next
            if num2:
                sum_val += num2.data
                num2 = num2.next

            carry, digit = divmod(sum_val, 10)
            curr.next = Node(digit)
            curr = curr.next

        result = reverseList(dummy.next)

        while result and result.data == 0:
            result = result.next
        
        return result if result else Node(0)
