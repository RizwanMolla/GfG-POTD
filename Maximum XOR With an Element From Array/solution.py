class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        for i in reversed(range(32)):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def maxXOR(self, num):
        node = self.root
        if not node.children:
            return -1
        max_xor = 0
        for i in reversed(range(32)):
            bit = (num >> i) & 1
            toggled = 1 - bit
            if toggled in node.children:
                max_xor |= (1 << i)
                node = node.children[toggled]
            else:
                node = node.children.get(bit, None)
                if not node:
                    return -1
        return max_xor

class Solution:
    def maxXor(self, arr, queries):
        arr.sort()
        queries = sorted([(xi, mi, idx) for idx, (xi, mi) in enumerate(queries)], key=lambda x: x[1])
        
        result = [0] * len(queries)
        trie = Trie()
        idx = 0
        n = len(arr)
        
        for xi, mi, qidx in queries:
            while idx < n and arr[idx] <= mi:
                trie.insert(arr[idx])
                idx += 1
            
            result[qidx] = trie.maxXOR(xi)
        
        return result