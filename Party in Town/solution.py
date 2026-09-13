from collections import deque

class Solution:
    def partyHouse(self, adj: list[list[int]]) -> int:
        def f(node):
            q = deque([(node, 0)])
            vis = {node}
            end = node
            cntt = 0

            while q:
                nodee, cnt = q.popleft()

                if cnt > cntt:
                    cntt = cnt
                    end = nodee

                for it in adj[nodee - 1]:
                    if it not in vis:
                        vis.add(it)
                        q.append((it, cnt + 1))

            return (end, cntt)

        end, cnt = f(1)
        end1, cnt = f(end)

        return (cnt + 1) // 2