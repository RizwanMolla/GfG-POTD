#User function Template for python3

class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def maxXor(self, arr):
        def insert(num):
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]

        def findMaxXor(num):
            node = root
            xor_sum = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                toggled = 1 - bit
                if toggled in node.children:
                    xor_sum |= (1 << i)
                    node = node.children[toggled]
                else:
                    node = node.children.get(bit, node)
            return xor_sum

        root = TrieNode()
        max_result = 0
        insert(arr[0])

        for num in arr[1:]:
            max_result = max(max_result, findMaxXor(num))
            insert(num)

        return max_result