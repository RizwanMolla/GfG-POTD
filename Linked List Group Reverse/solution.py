class Solution:
    def reverseKGroup(self, head, k):
        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        length = get_length(head)
        final_head = None
        final_tail = None
        group_head = None
        group_tail = None
        current = head

        while length > 0:
            count = min(k, length)
            while count > 0:
                next_node = current.next
                if not group_head:
                    group_head = current
                    group_tail = current
                else:
                    current.next = group_head
                    group_head = current
                current = next_node
                count -= 1
                length -= 1

            if not final_head:
                final_head = group_head
                final_tail = group_tail
            else:
                final_tail.next = group_head
                final_tail = group_tail

            group_head = None
            group_tail = None

        if final_tail:
            final_tail.next = None

        return final_head
