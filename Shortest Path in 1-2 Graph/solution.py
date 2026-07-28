class Solution:
    def shortestPath(self, V: int, src: int, dest: int, edges: list[list[int]]) -> int:
        from collections import defaultdict
        adj=defaultdict(set)
        mx=V
        for sta,sto,dis in edges:
            if dis==1:
                adj[sta].add(sto)
                adj[sto].add(sta)
                continue
            adj[sta].add(mx)
            adj[mx].add(sto)
            adj[sto].add(mx)
            adj[mx].add(sta)
            mx+=1
        tot=0
        q=[src]
        seen=set()
        while q:
            tot+=1
            nq=[]
            for cur in q:
                if cur in seen:
                    continue
                seen.add(cur)
                for nxt in adj[cur]:
                    if nxt==dest:
                        return tot
                    nq.append(nxt)
            q=nq
        return -1
