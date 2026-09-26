class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj={i:[] for i in range(n)}
        vis=set()
        for c,p in edges:
            adj[c].append(p)
            adj[p].append(c)
        def dfs(i):
            vis.add(i)
            for j in adj[i]:
                if j not in vis:
                    dfs(j)
            return
        ans=0
        for i in range(n):
            if i not in vis:
                dfs(i)
                ans+=1
        
        return ans
        

        