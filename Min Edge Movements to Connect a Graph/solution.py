class Solution:
    def minEdgesReq(self, n, edges):
        if len(edges) < n - 1:
            return -1

        representative = list(range(n))

        def get_root(node):
            while representative[node] != node:
                representative[node] = representative[representative[node]]
                node = representative[node]
            return node

        groups = n

        for first, second in edges:
            root_a = get_root(first)
            root_b = get_root(second)

            if root_a == root_b:
                continue

            representative[root_a] = root_b
            groups -= 1

        return groups - 1