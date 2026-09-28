class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=collections.defaultdict(list)
        for src,des,w in times:
            adj[src].append((des,w))
        q=[(0,k)]
        vis=set()
        ans=0
        while q:
            w1,node=heapq.heappop(q)
            if node in vis:
                continue
            ans=w1
            vis.add(node)
            print(w1,node)
            
            for n2,w2 in adj[node]:
                if n2 not in vis:
                    heapq.heappush(q,(w1+w2,n2))
            

        if len(vis)==n:
            return ans
        return -1
        


        