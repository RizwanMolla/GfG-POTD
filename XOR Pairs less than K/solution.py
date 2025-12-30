class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.count = 0

class Solution:
    B = 16

    def insert(self, root, num):
        curr = root
        for i in range(self.B - 1, -1, -1):
            bit = (num >> i) & 1
            if not curr.children[bit]:
                curr.children[bit] = TrieNode()
            curr = curr.children[bit]
            curr.count += 1

    def countSmaller(self, root, x, k):
        curr = root
        count = 0
        for i in range(self.B - 1, -1, -1):
            if not curr:
                return count
            bit_x = (x >> i) & 1
            bit_k = (k >> i) & 1
            target_bit_y_for_zero_xor = bit_x
            target_bit_y_for_one_xor = 1 - bit_x
            if bit_k == 1:
                node_for_zero_xor = curr.children[target_bit_y_for_zero_xor]
                if node_for_zero_xor:
                    count += node_for_zero_xor.count
                curr = curr.children[target_bit_y_for_one_xor]
            else:
                curr = curr.children[target_bit_y_for_zero_xor]
        return count

    def cntPairs(self, arr, k):
        root = TrieNode()
        total_pairs = 0
        for x in arr:
            total_pairs += self.countSmaller(root, x, k)
            self.insert(root, x)
        return total_pairs
